# Fluxo de Dados do Projeto

Este documento descreve o fluxo de dados do projeto IoT com ESP32, MQTT, Node-RED e HiveMQ Cloud.

## Visão geral

O sistema coleta dados de sensores no ESP32, publica essas informações em um tópico MQTT e o Node-RED consome esse tópico para exibir, processar ou encaminhar os dados.

## Caminho dos dados

1. Os sensores capturam os valores físicos do ambiente.
2. O ESP32 lê esses sensores e organiza os dados em JSON.
3. O ESP32 publica o JSON no broker HiveMQ Cloud.
4. O Node-RED assina o tópico MQTT.
5. O fluxo no Node-RED transforma o payload em objeto.
6. Os dados são enviados para debug, dashboard ou outras automações.

## Dados enviados pelo ESP32

O payload publicado no MQTT contém:

- `temperatura`
- `umidade`
- `luminosidade`
- `gas`
- `timestamp`

### Exemplo de mensagem

```json
{
  "temperatura": 24.5,
  "umidade": 61.0,
  "luminosidade": 1820,
  "gas": 950,
  "timestamp": 1710000000
}
```

## Fluxo no Node-RED

O fluxo recomendado é:

- `mqtt in` → recebe os dados do tópico `besp32miguelestacao`
- `json` → converte o texto JSON em objeto
- `function` → separa e trata os campos
- `debug` → mostra o conteúdo bruto e tratado
- `dashboard` → exibe os valores em gauges, gráficos e textos

## Origem e destino dos dados

- **Origem:** sensores conectados ao ESP32.
- **Processamento:** firmware em MicroPython.
- **Transporte:** MQTT via HiveMQ Cloud.
- **Consumo:** Node-RED.
- **Saída final:** dashboard, logs, gráficos ou automações.

## Regras do fluxo

- Cada leitura deve virar uma mensagem JSON válida.
- O tópico MQTT deve ser o mesmo no ESP32 e no Node-RED.
- O broker precisa estar configurado com TLS quando usar HiveMQ Cloud.
- O Node-RED deve receber o payload em `QoS 1` para maior confiabilidade.

## Resumo do comportamento

O projeto funciona em tempo real: o ESP32 mede o ambiente, publica os dados e o Node-RED recebe e distribui essas informações para visualização e análise. Esse padrão é típico de sistemas de fluxo contínuo de dados em IoT [web:60][web:62].

## Representação simplificada

```text
Sensores -> ESP32 -> MQTT HiveMQ Cloud -> Node-RED -> Dashboard / Debug / Automação
```
