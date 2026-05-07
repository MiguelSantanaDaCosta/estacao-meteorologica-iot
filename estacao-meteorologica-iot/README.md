# Estação Meteorológica IoT

Este projeto é uma estação meteorológica IoT desenvolvida com ESP32, MicroPython, MQTT, Node-RED e Wokwi. Ele coleta dados de temperatura, umidade, luminosidade e gás, trata as informações no firmware e envia tudo para o broker HiveMQ Cloud, onde o Node-RED pode consumir, processar e exibir os dados em um dashboard.

O objetivo do projeto é demonstrar uma arquitetura completa de IoT, desde a simulação até a integração com a nuvem, incluindo visualização local no OLED, publicação MQTT e tratamento dos dados em um fluxo modular e fácil de expandir.

## Sobre o projeto

A estação foi criada para monitorar o ambiente em tempo real e servir como base para projetos embarcados mais completos. O ESP32 faz a leitura dos sensores, monta um JSON com os dados, publica no tópico MQTT e também mostra o estado do sistema em um display OLED. O Node-RED recebe essas mensagens e pode transformar os dados em indicadores, gráficos e alertas.

O firmware foi estruturado em orientação a objetos para separar responsabilidades, melhorar a manutenção e facilitar a criação de novas funcionalidades. Essa abordagem é útil em embarcados porque reduz acoplamento, organiza melhor o fluxo e torna o código mais legível.

## O que o sistema faz

- Lê temperatura e umidade com o DHT22.
- Lê luminosidade com o LDR.
- Lê gás com o sensor MQ2.
- Mostra informações no display OLED.
- Permite trocar telas por botões físicos.
- Publica os dados via MQTT.
- Recebe os dados no Node-RED.
- Pode ser simulado no Wokwi.
- Pode ser adaptado para um ESP32 físico.

## Tecnologias usadas

- ESP32
- MicroPython
- MQTT
- HiveMQ Cloud
- Node-RED
- Wokwi
- SSD1306 OLED
- DHT22
- LDR
- MQ2
- Python orientado a objetos

## Estrutura do projeto

```text
estacao-meteorologica-iot/
├── docs/
├── mqtt/
├── node-red/
├── wokwi-esp32/
├── mostrando.mp4
├── README.md
└── LICENSE
```

## Documentação interna

Cada parte do projeto foi separada em arquivos próprios para facilitar o estudo:

- [Fluxo de dados](./docs/fluxo-dados.md)
- [Explicação dos sensores](./docs/explicacao-sensores.md)
- [Requisitos funcionais e não funcionais](./docs/requisitos.md)
- [Tópicos MQTT](./mqtt/topics.md)
- [Node-RED](./node-red/README.md)
- [Wokwi / ESP32](./wokwi-esp32/README.md)

## Como instalar e executar

### No Wokwi

1. Abra o projeto no Wokwi.
2. Verifique o arquivo `diagram.json`.
3. Abra o `main.py`.
4. Execute a simulação.
5. Observe as leituras no OLED e o envio via MQTT.

### Em um ESP32 real

1. Baixe o firmware MicroPython para ESP32.
2. Grave o firmware na placa.
3. Envie os arquivos `main.py` e `ssd1306.py`.
4. Configure WiFi e MQTT.
5. Conecte os sensores conforme o diagrama.
6. Reinicie a placa e acompanhe a saída serial.

### No Node-RED

1. Abra o Node-RED.
2. Importe o `flow.json`.
3. Configure o broker HiveMQ Cloud.
4. Faça o deploy.
5. Verifique os dados chegando pelo tópico `besp32miguelestacao`.

## Fluxo geral do sistema

1. Os sensores capturam os dados do ambiente.
2. O ESP32 lê e organiza as informações.
3. Os dados são convertidos para JSON.
4. O payload é publicado em MQTT.
5. O Node-RED consome o tópico.
6. Os dados são exibidos e analisados.
7. O OLED mostra o estado local da estação.

## Arquitetura do código

O código foi dividido em classes para manter cada responsabilidade isolada:

- `HardwareConfig` inicializa os periféricos.
- `SensorBase` define a interface dos sensores.
- `SensorDHT`, `SensorLDR` e `SensorMQ2` fazem a leitura dos sensores.
- `CalculadoraClima` calcula estados e classificações.
- `DataCollector` reúne os dados.
- `MQTTManager` gerencia conexão e envio.
- `DisplayManager` controla o OLED.
- `main()` coordena toda a execução.

Essa arquitetura foi escolhida porque favorece manutenção, reaproveitamento e expansão. Em vez de concentrar tudo em um único bloco, cada classe cuida de uma parte do sistema, o que facilita corrigir, testar e crescer o projeto.

## Demonstração

O vídeo de demonstração está disponível no repositório:

[Abrir demonstração em vídeo](./Kooha-2026-05-05-05-19-57.webm)

Se o GitHub não exibir o player, basta abrir o arquivo diretamente ou baixá-lo.

## Prévia da demonstração
```md
[Abrir demonstração em vídeo](./Kooha-2026-05-05-05-19-57.webm)
```
[./docs/demo.gif]```

## Links úteis

- [Wokwi](https://wokwi.com/projects/463136220390971393)
- [Documentação do Wokwi](https://docs.wokwi.com)
- [Node-RED](https://nodered.org/)
- [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/)
- [MicroPython](https://docs.micropython.org/)

## Licença

Este projeto está licenciado sob os termos do arquivo `LICENSE`.
# 🌤️ Estação Meteorológica ESP32 - ETAPA 2

**MQTT + Sheets + Email** direto do ESP32.

## Arquivos Etapa 2
- `wokwi-esp32/umail.py` ✅
- `docs/03-google-sheets.md` ✅
- `docs/04-email-smtp.md` ✅

## Teste
1. Apps Script ← [Guia](docs/03-google-sheets.md)
2. ESP32 ← main.py + emails.py + umail.py
3. Terminal: `Sheets OK`
