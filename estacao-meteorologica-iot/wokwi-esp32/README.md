# Miguel IoT Project

Projeto de simulação no Wokwi com ESP32, OLED SSD1306, DHT22, LDR, sensor de gás e botões de controle.

## Componentes

- ESP32 DevKit C V4
- Display OLED SSD1306
- Sensor DHT22
- Photoresistor (LDR)
- Gas Sensor
- 2 Push Buttons
- Breadboard half
- Resistor de 10k

## Estrutura do projeto

- `diagram.json` → define os componentes e as conexões da simulação.
- `code.py` ou `main.py` → código MicroPython do ESP32.
- `README.md` → descrição básica do projeto.

## Ligações principais

- OLED via I2C:
  - SDA → GPIO 21
  - SCL → GPIO 22
  - VCC → 3V3
  - GND → GND

- DHT22:
  - SDA → GPIO 4
  - VCC → 3V3
  - GND → GND

- LDR:
  - AO → GPIO 34
  - VCC → 3V3
  - GND → GND, com resistor de 10k no divisor de tensão

- Gas Sensor:
  - AOUT → GPIO 35
  - VCC → 5V
  - GND → GND

- Botões:
  - BTN1 → GPIO 18
  - BTN2 → GPIO 19

## Observações

- O projeto usa o editor `wokwi`.
- As conexões foram organizadas para simular leitura de sensores e interação por botões.
- O monitor serial está ligado ao ESP32 para depuração.

## Objetivo

Simular um painel IoT com leitura de temperatura/umidade, luminosidade, presença de gás e controle por botões, exibindo informações no OLED.

## Código do projeto

O firmware foi escrito em MicroPython para o ESP32 e organiza o sistema em classes para facilitar manutenção e expansão.

### Bibliotecas usadas

- `machine` → controle de GPIO, ADC e I2C.
- `dht` → leitura do sensor DHT22.
- `ssd1306` → controle do display OLED.
- `time` → delays, timestamps e controle do loop.
- `network` → conexão WiFi.
- `ujson` → serialização dos dados em JSON.
- `umqtt.simple.MQTTClient` → publicação dos dados no broker MQTT.

### Configuração de rede

O projeto conecta na rede `Wokwi-GUEST` e envia dados para um broker MQTT na nuvem com TLS/SSL habilitado.

- SSID: `Wokwi-GUEST`
- MQTT Broker: HiveMQ Cloud
- Porta: `8883`
- Cliente: `esp32miguel`
- Tópico: `besp32miguelestacao`

### Organização do código

O código foi dividido em blocos:

- `HardwareConfig` → inicializa OLED, DHT22, LDR, sensor de gás e botões.
- `SensorBase` → classe base abstrata para sensores.
- `SensorDHT`, `SensorLDR`, `SensorMQ2` → classes específicas de leitura.
- `CalculadoraClima` → faz cálculos e define estados do ambiente.
- `DataCollector` → junta todas as leituras em um único dicionário.
- `MQTTManager` → cuida da conexão e do envio para a nuvem.
- `DisplayManager` → controla as telas do OLED.
- `main()` → orquestra o ciclo principal do sistema.

### Funcionalidades implementadas

- Leitura de temperatura e umidade pelo DHT22.
- Leitura de luminosidade pelo LDR.
- Leitura de gás pelo sensor MQ2.
- Exibição das informações no OLED.
- Troca de telas por botões.
- Publicação dos dados em JSON via MQTT.
- Reconexão automática do MQTT quando a conexão cai.

### Estrutura das telas

- Tela 0: clima, temperatura, umidade e conforto térmico.
- Tela 1: luminosidade e gás, com alerta quando o gás está ruim.
- Tela 2: status geral do sistema, WiFi e MQTT.

### Fluxo de execução

1. Inicializa os periféricos.
2. Conecta no WiFi.
3. Conecta no broker MQTT.
4. Lê os sensores em loop.
5. Monta um JSON com os dados.
6. Publica no tópico MQTT.
7. Atualiza o OLED.
8. Verifica os botões para trocar de tela.

### Observações técnicas

- O DHT22 pode retornar erro em algumas leituras, então o código trata falhas e devolve valores padrão.
- O ADC do ESP32 é configurado com atenuação de 11 dB para aceitar melhor sinais analógicos.
- O uso de classes deixa o projeto mais modular e fácil de adaptar para novos sensores.

### Exemplo da saída JSON

```json
{
  "temperatura": 24.5,
  "umidade": 61.0,
  "luminosidade": 1820,
  "gas": 950,
  "timestamp": 1710000000
}
```

### Evoluções possíveis

- Adicionar gráfico histórico no OLED ou em dashboard web.
- Publicar dados separados por tópico MQTT.
- Incluir calibragem do MQ2.
- Adicionar LEDs de alerta ou buzzer.
- Salvar dados em banco de dados via Node-RED ou API.

## Link do projeto no Wokwi

Você pode abrir a simulação completa aqui:

[Projeto no Wokwi](https://wokwi.com/projects/463136220390971393)

## Como compartilhar manualmente

Se quiser gerar o link manualmente no Wokwi, siga estes passos:

1. Abra o projeto no Wokwi.
2. Clique em **Save** para garantir que o projeto foi salvo.
3. No topo da tela, clique em **Share**.
4. Copie o link gerado.
5. Envie esse link para quem quiser visualizar o projeto.

## Observações

- O link compartilhado permite abrir a simulação exatamente como ela foi salva.
- Se você alterar o projeto depois, lembre-se de salvar novamente antes de compartilhar.
- Esse método funciona tanto para compartilhar com colegas quanto para usar em atividades ou documentação.
