## Requisitos funcionais

O sistema deve:

1. Ler temperatura e umidade usando o sensor DHT22.
2. Ler luminosidade usando o sensor LDR.
3. Ler presença/nível de gás usando o sensor MQ2.
4. Exibir as leituras no display OLED.
5. Permitir troca de telas por botões físicos.
6. Conectar na rede WiFi.
7. Conectar no broker MQTT HiveMQ Cloud.
8. Publicar os dados dos sensores em JSON no tópico MQTT.
9. Reconectar automaticamente ao MQTT em caso de falha.
10. Enviar mensagens em intervalo periódico.
11. Mostrar status do sistema no display.
12. Tratar falhas de leitura dos sensores sem interromper o loop principal.

## Requisitos não funcionais

O sistema deve:

1. Ser modular e fácil de manter.
2. Ter código organizado por responsabilidade.
3. Ser compatível com ESP32 executando MicroPython.
4. Ter baixo consumo de memória e processamento.
5. Funcionar de forma estável em loop contínuo.
6. Suportar comunicação segura com MQTT via TLS.
7. Ser fácil de expandir com novos sensores e telas.
8. Manter o código legível para futuras manutenções.
9. Ter tempo de resposta rápido para atualização de telas e envio MQTT.
10. Permitir execução em ambiente de simulação no Wokwi e em hardware real.

## Arquitetura do código

O `main.py` foi estruturado em um modelo orientado a objetos para separar responsabilidades e facilitar a evolução do sistema. Em vez de concentrar tudo em um único bloco de código, cada parte do sistema ficou isolada em uma classe com uma função bem definida.

### Organização adotada

- `HardwareConfig` inicializa e centraliza o hardware.
- `SensorBase` define um contrato comum para sensores.
- `SensorDHT`, `SensorLDR` e `SensorMQ2` implementam a leitura de cada sensor.
- `CalculadoraClima` concentra a lógica de regras e classificação do ambiente.
- `DataCollector` reúne os dados de vários sensores em um único payload.
- `MQTTManager` abstrai conexão, envio e reconexão MQTT.
- `DisplayManager` controla toda a interface do OLED.
- `main()` faz a orquestração do sistema.

### Por que usei essa arquitetura

Essa separação foi feita para aplicar o princípio de responsabilidade única: cada classe faz uma coisa só. Isso deixa o código mais fácil de testar, corrigir e ampliar sem quebrar o restante do projeto [web:76][web:79][web:82].

### Vantagens em projetos embarcados

Em embarcados, essa abordagem ajuda porque:

- reduz acoplamento entre módulos;
- facilita trocar sensores sem reescrever o sistema inteiro;
- melhora a leitura e manutenção do firmware;
- permite reaproveitar partes do código em outros projetos;
- torna mais simples adicionar novos estados, alarmes ou telas;
- organiza melhor a lógica mesmo com recursos limitados.

### Como o Python ajudou

O Python, por ser uma linguagem com suporte natural à orientação a objetos, permitiu criar classes pequenas e reutilizáveis, usando métodos para encapsular comportamento e abstração para esconder detalhes de implementação. Isso é útil em firmware porque o código fica mais expressivo e próximo da lógica do domínio do projeto [web:74][web:77][web:80].

### Exemplo prático da abstração

Em vez de tratar leitura de sensor, exibição e envio MQTT no mesmo fluxo, cada parte ficou isolada. Assim, o sistema inteiro passa a se comportar como uma composição de blocos independentes: sensores coletam dados, a classe de coleta junta tudo, o MQTT publica, e o display mostra o resultado.

## Resumo da estrutura

```text
Hardware -> Sensores -> Coleta -> Regras -> MQTT -> Display
```

Essa estrutura foi pensada para facilitar expansão futura, como adicionar novos sensores, novas telas ou até integração com dashboard web sem refazer o firmware inteiro.
