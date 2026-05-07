from machine import Pin, ADC, I2C
import dht
import ssd1306
import time
import network
import ujson
from umqtt.simple import MQTTClient

#======>>atualização PARTE2
from emails import RelatoriosManager
relatorios = RelatoriosManager()

# =========================
# CONFIGURAÇÕES
# =========================

SSID = "Wokwi-GUEST"
PASSWORD = ""

MQTT_BROKER = "3157a291b3a543f4825306043bdca95d.s1.eu.hivemq.cloud"
MQTT_PORT = 8883

MQTT_USER = "Santana"
MQTT_PASSWORD = "Santana1"

CLIENT_ID = "esp32miguel"
MQTT_TOPIC = "besp32miguelestacao"

# =========================
# HARDWARE
# =========================

class HardwareConfig:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c)

        self.dht = dht.DHT22(Pin(4))

        self.ldr = ADC(Pin(34))
        self.ldr.atten(ADC.ATTN_11DB)

        self.gas = ADC(Pin(35))
        self.gas.atten(ADC.ATTN_11DB)

        self.btn1 = Pin(18, Pin.IN, Pin.PULL_UP)
        self.btn2 = Pin(19, Pin.IN, Pin.PULL_UP)

# =========================
# SENSORES
# =========================

class SensorBase:
    def ler(self):
        raise NotImplementedError()

class SensorDHT(SensorBase):
    def __init__(self, dht):
        self.sensor = dht

    def ler(self):
        try:
            self.sensor.measure()
            return {
                "temperatura": self.sensor.temperature(),
                "umidade": self.sensor.humidity()
            }
        except:
            return {
                "temperatura": 0,
                "umidade": 0
            }

class SensorLDR(SensorBase):
    def __init__(self, adc):
        self.adc = adc

    def ler(self):
        return {"luminosidade": self.adc.read()}

class SensorMQ2(SensorBase):
    def __init__(self, adc):
        self.adc = adc

    def ler(self):
        return {"gas": self.adc.read()}


# CÁLCULOS


class CalculadoraClima:

    def conforto_termico(self, t, h):
        return t - (0.55 - 0.0055 * h) * (t - 14.5)

    def estado_temperatura(self, t):
        if t < 18:
            return "FRIO"
        elif t < 30:
            return "OK"
        else:
            return "QUENTE"

    def estado_gas(self, g):
        if g < 1000:
            return "BOM"
        elif g < 3000:
            return "MODERADO"
        else:
            return "RUIM"

    def estado_luz(self, l):
        if l < 1000:
            return "BAIXA"
        elif l < 3000:
            return "MEDIA"
        else:
            return "ALTA"

    def qualidade_ar(self, gas):
        if gas < 1000:
            return "AR BOM"
        elif gas < 3000:
            return "AR MODERADO"
        else:
            return "AR RUIM"

# =========================
# COLETA
# =========================

class DataCollector:
    def __init__(self, sensores):
        self.sensores = sensores

    def coletar(self):
        dados = {}
        for s in self.sensores:
            dados.update(s.ler())

        dados["timestamp"] = time.time()
        return dados

# =========================
# MQTT
# =========================

class MQTTManager:
    def __init__(self, client, topic):
        self.client = client
        self.topic = topic
        self.conectado = False
        self.ultima_tentativa = 0

    def conectar(self):
        try:
            self.client.connect()
            self.conectado = True
            print("MQTT OK")
        except Exception as e:
            self.conectado = False
            print("MQTT ERRO:", e)

    def verificar_conexao(self):
        if not self.conectado and (time.time() - self.ultima_tentativa > 10):
            print("Tentando reconectar MQTT...")
            self.ultima_tentativa = time.time()
            self.conectar()

    def enviar(self, msg):
        if not self.conectado:
            return

        try:
            self.client.publish(self.topic, msg, qos=1)
        except:
            print("Perdeu conexão MQTT")
            self.conectado = False

# =========================
# WIFI
# =========================

def conectar_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    if not wifi.isconnected():
        print("Conectando WiFi...")
        wifi.connect(SSID, PASSWORD)

        tentativas = 0
        while not wifi.isconnected() and tentativas < 10:
            time.sleep(1)
            tentativas += 1

    if wifi.isconnected():
        print("WiFi OK:", wifi.ifconfig())
        return True
    else:
        print("WiFi FALHOU")
        return False

# =========================
# DISPLAY
# =========================

class DisplayManager:
    def __init__(self, oled):
        self.oled = oled
        self.tela = 0

    def proxima_tela(self):
        self.tela = (self.tela + 1) % 3

    def ir_status(self):
        self.tela = 2

    def mostrar(self, dados, calc, mqtt_status):

        self.oled.fill(0)

        # =========================
        # TELA 0 → CLIMA COMPLETO
        # =========================
        if self.tela == 0:
            t = dados["temperatura"]
            h = dados["umidade"]
            ic = calc.conforto_termico(t, h)

            self.oled.text(f"T:{t:.1f}C", 0, 0)
            self.oled.text(f"H:{h:.1f}%", 0, 10)
            self.oled.text(f"IC:{ic:.1f}", 0, 20)

            self.oled.text(calc.estado_temperatura(t), 0, 35)
            self.oled.text(calc.qualidade_ar(dados["gas"]), 0, 45)

        # =========================
        # TELA 1 → LUZ + GÁS + ALERTA
        # =========================
        elif self.tela == 1:
            luz = dados["luminosidade"]
            gas = dados["gas"]

            self.oled.text(f"Luz:{luz}", 0, 0)
            self.oled.text(calc.estado_luz(luz), 0, 10)

            self.oled.text(f"Gas:{gas}", 0, 30)
            estado = calc.estado_gas(gas)
            self.oled.text(estado, 0, 40)

            if estado == "RUIM":
                self.oled.text("ALERTA!", 0, 55)

        # =========================
        # TELA 2 → STATUS COMPLETO
        # =========================
        elif self.tela == 2:
            self.oled.text("STATUS SISTEMA", 0, 0)

            self.oled.text("MQTT:", 0, 15)
            self.oled.text("OK" if mqtt_status else "OFF", 50, 15)

            self.oled.text("WiFi:", 0, 30)
            self.oled.text("OK", 50, 30)

            self.oled.text("ESP32 OK", 0, 50)

        self.oled.show()
# =========================
# MAIN
# =========================

def main():

    hw = HardwareConfig()

    sensor_dht = SensorDHT(hw.dht)
    sensor_ldr = SensorLDR(hw.ldr)
    sensor_gas = SensorMQ2(hw.gas)

    collector = DataCollector([
        sensor_dht,
        sensor_ldr,
        sensor_gas
    ])

    calc = CalculadoraClima()
    display = DisplayManager(hw.oled)

    wifi_ok = conectar_wifi()

    mqtt = None

    if wifi_ok:
        try:
            client = MQTTClient(
                client_id=CLIENT_ID,
                server=MQTT_BROKER,
                port=MQTT_PORT,
                user=MQTT_USER,
                password=MQTT_PASSWORD,
                ssl=True,
                ssl_params={"server_hostname": MQTT_BROKER}
            )

            mqtt = MQTTManager(client, MQTT_TOPIC)
            mqtt.conectar()

        except Exception as e:
            print("Erro MQTT:", e)

    while True:

        dados = collector.coletar()
        msg = ujson.dumps(dados)

        print(msg)

        if mqtt:
            mqtt.verificar_conexao()
            mqtt.enviar(msg)
            dados_completo = collector.coletar()
            #preferi deixar a parte do email aqui pois não sabia como seria a parte dois
            #se tivesse estruturado de uma forma melhor poderia ter separado mais as responsabilidades
            #para não ser necessario mecher na função do loop principal afim de evitar falhas
            #porem adicionando no if do mqtt que ja sei que funciona garante que sei posso identificar falhas no fluxo de execução
            dados_completo["timestamp"] = time.time()
            status = relatorios.processar_dados(dados_completo)
            print(f"Sheets: {'OK' if status['sheets_ok'] else 'ERRO'}")
        
        # Botões
        if not hw.btn1.value():
             display.proxima_tela()
             time.sleep(0.3)

        if not hw.btn2.value():
             display.tela = 2
             time.sleep(0.3) 

        display.mostrar(
            dados,
            calc,
            mqtt.conectado if mqtt else False
        )

        time.sleep(2)

# START
main()


