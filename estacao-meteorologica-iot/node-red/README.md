# Node-RED MQTT - ESP32 HiveMQ Cloud

Fluxo do Node-RED para receber mensagens MQTT publicadas pelo ESP32 no tópico `besp32miguelestacao`.

## Objetivo

Este projeto recebe dados enviados pelo ESP32 via MQTT, conecta no HiveMQ Cloud e permite visualizar as mensagens no Node-RED.

As mensagens esperadas são JSON contendo campos como temperatura, umidade, luminosidade, gás e timestamp.

## Tópico MQTT

- **Topic:** `besp32miguelestacao`
- **QoS:** `1`

## Fluxo Node-RED

O fluxo possui:

- `mqtt in` para assinar o tópico.
- `mqtt-broker` para conectar ao HiveMQ Cloud.
- nós de saída para debug/visualização, se adicionados ao fluxo completo.

### JSON do fluxo

```json
[
    {
        "id": "cdbfc7144dfb78d0",
        "type": "mqtt in",
        "z": "c06037e233e49bb7",
        "name": "ESP32",
        "topic": "besp32miguelestacao",
        "qos": "1",
        "datatype": "auto",
        "broker": "hive",
        "inputs": 0,
        "x": 70,
        "y": 320,
        "wires": [
            [
                "9595d22618c847af",
                "7b51d6762495fd0f"
            ]
        ]
    },
    {
        "id": "hive",
        "type": "mqtt-broker",
        "name": "HiveMQ",
        "broker": "3157a291b3a543f4825306043bdca95d.s1.eu.hivemq.cloud",
        "port": "8883",
        "tls": "",
        "clientid": "",
        "autoConnect": true,
        "usetls": true,
        "protocolVersion": 4,
        "keepalive": "120",
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    }
]
```

## Como importar no Node-RED

1. Abra o Node-RED no navegador.
2. Clique no menu no canto superior direito.
3. Selecione **Import**.
4. Cole o JSON do fluxo.
5. Clique em **Import** novamente.
6. Clique em **Deploy**.

Se o fluxo vier com referências a nós que não existem ainda, crie os nós de debug ou visualização manualmente.

## Como configurar o HiveMQ Cloud

Abra o nó `mqtt-broker` e preencha:

- **Server:** `3157a291b3a543f4825306043bdca95d.s1.eu.hivemq.cloud`
- **Port:** `8883`
- **Username:** `Santana`
- **Password:** `Santana1`
- **TLS:** habilitado

Use TLS/SSL porque a porta `8883` é a porta segura padrão do HiveMQ Cloud.

## Problema comum: erro de TLS

Se aparecer erro como:

- `TypeError: Cannot read properties of undefined (reading 'trim')`
- `Circular config node dependency detected: hive`
- `missing broker configuration`

isso normalmente indica que:

- o nó TLS foi criado incompleto,
- alguma credencial ficou vazia,
- o broker foi referenciado de forma duplicada,
- ou o fluxo foi importado com dependências quebradas.

### Como corrigir

1. Abra o nó `mqtt-broker`.
2. Remova a configuração TLS antiga, se estiver quebrada.
3. Crie uma nova configuração TLS manualmente.
4. Marque **Use TLS**.
5. Preencha corretamente os campos de certificado apenas se necessário.
6. Se não usar certificado próprio, deixe a configuração TLS simples e só ative o SSL do broker.

## Como rodar localmente com Docker

A forma recomendada para rodar Node-RED localmente é com Docker, porque o diretório `/data` fica persistente e você não perde flows ao reiniciar o container [web:28][web:2].

### Comando básico

```bash
docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red
```

### O que esse comando faz

- `-p 1880:1880` expõe o Node-RED na porta 1880.
- `-v node_red_data:/data` salva seus flows e credenciais.
- `--name mynodered` dá nome fixo ao container.
- `nodered/node-red` usa a imagem oficial.

### Acessar no navegador

Depois de subir o container, abra:

```text
http://localhost:1880
```

ou o IP da máquina onde o container estiver rodando.

## Como parar e iniciar

```bash
docker stop mynodered
docker start mynodered
```

Para ver os logs novamente:

```bash
docker attach mynodered
```

## Rodando com Docker Compose

Exemplo simples:

```yaml
version: "3.7"

services:
  node-red:
    image: nodered/node-red:latest
    ports:
      - "1880:1880"
    volumes:
      - node-red-data:/data

volumes:
  node-red-data:
```

Suba com:

```bash
docker compose up -d
```

## Problemas ao usar sem Docker

Rodar Node-RED diretamente na máquina também é possível, mas costuma dar mais trabalho de ambiente.

### Possíveis problemas

- diferença de versão do Node.js.
- dependências faltando.
- conflitos de permissões.
- perda de flows se a pasta de dados não estiver bem configurada.
- dificuldade maior para manter o ambiente igual em outra máquina.

### Quando vale usar sem Docker

- testes rápidos.
- ambientes já preparados com Node-RED instalado via npm.
- máquinas onde Docker não pode ser usado.

## Estrutura esperada do projeto

- `flow.json` → fluxo do Node-RED.
- `flow_cred.json` → credenciais do broker, se exportadas.
- `README.md` → documentação.
- opcionalmente `docker-compose.yml` → ambiente local.

## Documentação original

- [Node-RED Get Started](https://nodered.org/#get-started)
- [Node-RED Docker Docs](https://nodered.org/docs/getting-started/docker)
