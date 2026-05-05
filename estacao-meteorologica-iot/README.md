# 🌦️ Estação Meteorológica IoT — ESP32 + MQTT + Node-RED

![IoT](https://img.shields.io/badge/IoT-ESP32-blue)
![MQTT](https://img.shields.io/badge/MQTT-HiveMQ-green)
![Node-RED](https://img.shields.io/badge/Node--RED-4.1.8-red)
![Dashboard](https://img.shields.io/badge/Dashboard-Realtime-orange)
![Status](https://img.shields.io/badge/Status-Online-brightgreen)

---

## 📌 Visão Geral

Sistema de monitoramento ambiental em tempo real utilizando ESP32 (Wokwi), MQTT (HiveMQ Cloud) e Node-RED Dashboard.

---

## 🧠 Arquitetura

ESP32 (Wokwi) → MQTT → HiveMQ Cloud → Node-RED → Dashboard

---

## 📊 Sensores

- Temperatura (°C)
- Umidade (%)
- Luminosidade (lux)
- Gás (ppm)

---

## 🚨 Alertas do Sistema

- ≥ 38°C → 🔥 Crítico
- ≥ 3500 ppm gás → ☠️ Perigoso
- Combinação → 🚨 Alerta Geral
- Normal → OK

---

## 🖥️ Dashboard

- Gauges (temperatura e umidade)
- Donut (gás)
- Compass (luminosidade)
- Status de conforto
- Qualidade do ar
- Toast alerts

---

## ⚙️ Tecnologias

- ESP32 (Wokwi)
- MQTT (HiveMQ Cloud)
- Node-RED 4.1.8
- node-red-dashboard 3.6.6
- @flowfuse/node-red-dashboard 1.30.2
- Node.js 18+

---

## 📦 Instalação

```bash
npm install node-red-dashboard
npm install @flowfuse/node-red-dashboard
npm install node-red-contrib-uibuilder
npm install node-red-node-ui-table

📡 MQTT
Broker: HiveMQ Cloud
Porta: 8883 (TLS)
Topic: besp32miguelestacao
Payload
{
  "temperatura": 24,
  "umidade": 40,
  "luminosidade": 1000,
  "gas": 1200
}
🧪 Execução
ESP32 (Wokwi)
Simular envio MQTT
Node-RED
Importar flow.json
Instalar dependências
Rodar dashboard
Dashboard
http://localhost:1880/ui
📁 Estrutura
estacao-iot/
├── wokwi/
├── node-red/
├── mqtt/
├── docs/
└── README.md
📈 Funcionalidades
Tempo real
Dashboard web
Alertas automáticos
Processamento MQTT
Visualização de sensores# 🌦️ Estação Meteorológica IoT — ESP32 + MQTT + Node-RED

![IoT](https://img.shields.io/badge/IoT-ESP32-blue)
![MQTT](https://img.shields.io/badge/MQTT-HiveMQ-green)
![Node-RED](https://img.shields.io/badge/Node--RED-4.1.8-red)
![Dashboard](https://img.shields.io/badge/Dashboard-Realtime-orange)
![Status](https://img.shields.io/badge/Status-Online-brightgreen)

---

## 📌 Visão Geral

Sistema de monitoramento ambiental em tempo real utilizando ESP32 (Wokwi), MQTT (HiveMQ Cloud) e Node-RED Dashboard.

---

## 🧠 Arquitetura

ESP32 (Wokwi) → MQTT → HiveMQ Cloud → Node-RED → Dashboard

---

## 📊 Sensores

- Temperatura (°C)
- Umidade (%)
- Luminosidade (lux)
- Gás (ppm)

---

## 🚨 Alertas do Sistema

- ≥ 38°C → 🔥 Crítico
- ≥ 3500 ppm gás → ☠️ Perigoso
- Combinação → 🚨 Alerta Geral
- Normal → OK

---

## 🖥️ Dashboard

- Gauges (temperatura e umidade)
- Donut (gás)
- Compass (luminosidade)
- Status de conforto
- Qualidade do ar
- Toast alerts

---

## ⚙️ Tecnologias

- ESP32 (Wokwi)
- MQTT (HiveMQ Cloud)
- Node-RED 4.1.8
- node-red-dashboard 3.6.6
- @flowfuse/node-red-dashboard 1.30.2
- Node.js 18+

---

## 📦 Instalação

```bash
npm install node-red-dashboard
npm install @flowfuse/node-red-dashboard
npm install node-red-contrib-uibuilder
npm install node-red-node-ui-table


📡 MQTT
Broker: HiveMQ Cloud
Porta: 8883 (TLS)
Topic: besp32miguelestacao
Payload
{
  "temperatura": 24,
  "umidade": 40,
  "luminosidade": 1000,
  "gas": 1200
}
🧪 Execução
ESP32 (Wokwi)
Simular envio MQTT
Node-RED
Importar flow.json
Instalar dependências
Rodar dashboard
Dashboard
http://localhost:1880/ui
📁 Estrutura
estacao-iot/
├── wokwi/
├── node-red/
├── mqtt/
├── docs/
└── README.md
📈 Funcionalidades
Tempo real
Dashboard web
Alertas automáticos
Processamento MQTT
Visualização de sensores


