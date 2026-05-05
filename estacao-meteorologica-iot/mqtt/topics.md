# Miguel IoT Project

Projeto IoT com ESP32, sensores ambientais, display OLED e envio de dados via MQTT para a nuvem.

## Visão geral

Este projeto lê dados de temperatura, umidade, luminosidade e gás, exibe as informações no OLED e publica tudo em um tópico MQTT.

A imagem abaixo mostra a interface do HiveMQ Cloud Web Client com o projeto já conectado e recebendo mensagens no tópico configurado.

![Dashboard MQTT](2026-05-05-025652_hyprshot.jpg)

## Componentes

- ESP32 DevKit C V4
- Display OLED SSD1306
- Sensor DHT22
- Sensor de luminosidade LDR
- Sensor de gás MQ2
- 2 botões
- Breadboard
- Resistor de 10k

## Tópicos MQTT

O projeto publica os dados no seguinte tópico:

- `besp32miguelestacao`

### Estrutura da mensagem

As mensagens enviadas usam JSON, com campos como:

- `temperatura`
- `umidade`
- `luminosidade`
- `gas`
- `timestamp`

### Exemplo de payload

```json
{
  "temperatura": 24.5,
  "umidade": 61.0,
  "luminosidade": 1820,
  "gas": 950,
  "timestamp": 1710000000
}
```

### QoS

O projeto usa `QoS 1`, o que aumenta a confiabilidade da entrega das mensagens.

## Conexão MQTT

Configuração usada no firmware:

- Broker: `3157a291b3a543f4825306043bdca95d.s1.eu.hivemq.cloud`
- Porta: `8883`
- Usuário: `Santana`
- Senha: `Santana1`
- Cliente: `esp32miguel`

A conexão é feita com SSL habilitado.

## Estrutura do firmware

O código foi organizado em classes para facilitar manutenção e expansão:

- `HardwareConfig` → inicializa display, sensores e botões.
- `SensorDHT` → leitura de temperatura e umidade.
- `SensorLDR` → leitura de luminosidade.
- `SensorMQ2` → leitura de gás.
- `CalculadoraClima` → define estados e cálculos do ambiente.
- `DataCollector` → junta todos os dados em um único JSON.
- `MQTTManager` → conecta e publica no broker.
- `DisplayManager` → controla as telas do OLED.

## Telas do display

- Tela 0: temperatura, umidade e conforto térmico.
- Tela 1: luminosidade e gás, com alerta.
- Tela 2: status geral do sistema.

## Como funciona

1. O ESP32 conecta no WiFi.
2. O cliente MQTT autentica no broker.
3. Os sensores são lidos em loop.
4. Os dados são convertidos para JSON.
5. O payload é publicado no tópico MQTT.
6. O OLED mostra os valores em tempo real.
7. Os botões alternam entre as telas.

## Arquivo do Wokwi

O projeto de simulação está disponível em:

[Projeto no Wokwi](https://wokwi.com/projects/463136220390971393)

## Observações

- A imagem usada no README está no mesmo diretório do arquivo.
- O sensor DHT22 pode retornar falhas ocasionais; o código trata esse caso.
- O projeto pode ser expandido com novos tópicos, alarmes ou dashboard web.
