# Estação Meteorológica IoT

Este projeto é uma estação meteorológica IoT baseada em ESP32 com MicroPython, desenvolvida para coletar dados de sensores, exibir informações em um OLED e publicar leituras via MQTT para o HiveMQ Cloud. Os dados também podem ser consumidos no Node-RED para visualização em dashboard e análise em tempo real.

O objetivo do projeto é integrar hardware embarcado, comunicação MQTT, simulação no Wokwi e visualização de dados em uma arquitetura modular e fácil de expandir.

## Sobre o projeto

A estação lê temperatura, umidade, luminosidade e gás, organiza os valores em JSON e envia as mensagens para um tópico MQTT. No firmware, o código foi estruturado com orientação a objetos para separar responsabilidades e facilitar manutenção, testes e evolução futura do sistema.

Além da comunicação com a nuvem, o ESP32 exibe dados no display OLED e permite alternar telas por botões físicos. No Node-RED, os mesmos dados podem ser tratados e exibidos em painéis de monitoramento.

## O que o sistema faz

- Lê sensores ambientais.
- Calcula estados e alertas.
- Exibe informações no OLED.
- Publica dados em MQTT.
- Recebe os dados no Node-RED.
- Permite simulação no Wokwi.
- Pode ser adaptado para hardware real.

## Documentação do projeto

A documentação foi dividida por assunto para facilitar o estudo e a manutenção:

- [Fluxo de dados](./docs/fluxo-dados.md)
- [Explicação dos sensores](./docs/explicacao-sensores.md)
- [Requisitos funcionais e não funcionais](./docs/requisitos.md)
- [Arquitetura do código](./docs/arquitetura.png)
- [Tópicos MQTT](./mqtt/topics.md)
- [Node-RED](./node-red/README.md)
- [Wokwi / ESP32](./wokwi-esp32/README.md)

## Estrutura do repositório

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

## Tecnologias usadas

- ESP32
- MicroPython
- Wokwi
- MQTT
- HiveMQ Cloud
- Node-RED
- SSD1306 OLED
- DHT22
- LDR
- MQ2
- Python orientado a objetos

## Como o projeto funciona

1. Os sensores coletam os dados do ambiente.
2. O ESP32 lê e processa as informações.
3. O firmware monta um JSON com os dados.
4. O JSON é publicado no tópico MQTT.
5. O Node-RED recebe e trata os dados.
6. O display OLED mostra o estado local do sistema.

## Arquitetura do software

O código foi organizado em classes para separar claramente as responsabilidades:

- inicialização de hardware;
- leitura dos sensores;
- cálculos e regras de estado;
- coleta de dados;
- conexão MQTT;
- controle do display.

Essa estrutura reduz acoplamento, melhora legibilidade e facilita a evolução do projeto em cenários embarcados.

## Demonstração

O vídeo de demonstração do projeto está disponível localmente no repositório:

[Assistir demonstração](./mostrando.mp4)

## Links úteis

- [Wokwi](https://wokwi.com/projects/463136220390971393)
- [Documentação do Wokwi](https://docs.wokwi.com)
- [Node-RED](https://nodered.org/)
- [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/)
- [MicroPython](https://docs.micropython.org/)

## Licença

Este projeto está licenciado sob os termos do arquivo `LICENSE`.
