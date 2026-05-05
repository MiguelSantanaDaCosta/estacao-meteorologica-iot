## Sensores do projeto

### DHT22
O DHT22 é o sensor responsável por medir temperatura e umidade do ambiente. No projeto, ele é lido pelo ESP32 via um único pino de dados, usando a biblioteca `dht` do MicroPython.

Documentação no Wokwi: [wokwi-dht22 Reference](https://docs.wokwi.com/parts/wokwi-dht22)

### LDR / Photoresistor
O LDR é usado para medir a luminosidade do ambiente. No Wokwi, o módulo de photoresistor já vem com um resistor de 10k em série, e a saída analógica deve ser conectada a um pino ADC do ESP32.

Documentação no Wokwi: [wokwi-photoresistor-sensor Reference](https://docs.wokwi.com/parts/wokwi-photoresistor-sensor)

### MQ2
O sensor MQ2 é usado para detectar gases combustíveis, como GLP, propano e metano. A leitura é analógica e deve ser conectada a um pino ADC do ESP32.

Documentação de componentes suportados no Wokwi: [Supported Hardware](https://docs.wokwi.com/getting-started/supported-hardware)

### OLED SSD1306
O display OLED mostra os dados coletados pelos sensores em tempo real. Ele se comunica com o ESP32 por I2C.

### Botões
Os botões são usados para trocar as telas do display e navegar entre as informações mostradas no OLED.

## Como ver a documentação no Wokwi

Para consultar a documentação de cada componente:

1. Abra a página do componente no Wokwi.
2. Procure a seção **Reference** ou **Supported Hardware**.
3. Leia os pinos, funcionamento e exemplos de uso.
4. Compare com as conexões do seu `diagram.json`.

### Links úteis do Wokwi

- [DHT22 Reference](https://docs.wokwi.com/parts/wokwi-dht22)
- [Photoresistor Sensor Reference](https://docs.wokwi.com/parts/wokwi-photoresistor-sensor)
- [Supported Hardware](https://docs.wokwi.com/getting-started/supported-hardware)
- [Wokwi Docs](https://docs.wokwi.com)

## Instalar MicroPython em um ESP32 real

Para instalar MicroPython em um ESP32 físico, use a documentação oficial e um IDE como Thonny.

### Guia oficial
- [MicroPython Documentation](https://docs.micropython.org/)
- [ESP32 Quick Reference](https://docs.micropython.org/en/latest/esp32/quickref.html)

### Passos básicos

1. Baixe o firmware MicroPython correto para ESP32.
2. Conecte o ESP32 ao computador via USB.
3. Abra o Thonny IDE.
4. Selecione o interpretador MicroPython para ESP32.
5. Escolha a porta serial correta.
6. Clique em **Install or update MicroPython**.
7. Reinicie a placa após a instalação.

### Alternativa com ferramenta de instalação
O processo de instalação também é suportado por IDEs como o Thonny, que facilita gravar o firmware no ESP32.

## Observação

No Wokwi você não precisa instalar firmware no hardware real, mas no ESP32 físico a gravação do MicroPython é obrigatória para executar arquivos como `main.py`.
