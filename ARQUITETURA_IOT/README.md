
# 🌐 Curso de Arquitetura de Internet das Coisas (IoT)
Este material serve como guia teórico e prático para o entendimento das camadas, protocolos e integração de ecossistemas IoT.
---## 🏗️ 1. A Arquitetura IoT em 4 Camadas
A arquitetura de um sistema IoT é dividida em camadas para separar as responsabilidades desde a captura do dado físico até a tomada de decisão.


[ Camada de Aplicação (Nuvem / Dashboards) ]
▲
│ (HTTP / MQTT / AMQP)
[ Camada de Redes e Conectividade (Gateways / Roteadores) ]
▲
│ (Wi-Fi / LoRaWAN / BLE / Zigbee)
[ Camada de Processamento de Borda (Edge Computing) ]
▲
│ (GPIO / I2C / SPI / UART)
[ Camada de Percepção (Sensores e Atuadores) ]


### 1.1. Camada de Percepção (Sensoriamento)
*   **Hardware:** Sensores (capturam dados do ambiente) e Atuadores (executam ações físicas).
*   **Exemplos:** Sensor de temperatura (DHT11), Sensor de presença (PIR), Relés, Motores.

### 1.2. Camada de Processamento de Borda (Edge Computing)
*   **Hardware:** Microcontroladores e Microprocessadores que tratam o dado localmente antes do envio.
*   **Exemplos:** ESP32, Arduino, Raspberry Pi.

### 1.3. Camada de Rede e Conectividade
*   **Protocolos de Longo Alcance:** LoRaWAN, NB-IoT, 4G/5G (Células).
*   **Protocolos de Curto Alcance:** Wi-Fi, Bluetooth Low Energy (BLE), Zigbee.

### 1.4. Camada de Aplicação e Nuvem
*   **Serviços:** Processamento pesado, armazenamento em bancos de dados e exibição em dashboards.
*   **Exemplos:** AWS IoT Core, Azure IoT Hub, TagoIO, ThingSpeak.

---

## 📡 2. Protocolos de Comunicação de Dados

Diferente da web tradicional (HTTP), o IoT exige protocolos leves devido à restrição de energia e banda dos dispositivos.


| Protocolo | Modelo | Consumo | Uso Principal |
| :--- | :--- | :--- | :--- |
| **MQTT** | Publish/Subscribe | Muito Baixo | Redes instáveis, telemetria de sensores |
| **HTTP/REST** | Request/Response | Médio/Alto | Integração de APIs na nuvem, envio de arquivos |
| **CoAP** | Request/Response | Baixo | Dispositivos extremamente limitados (UDP) |

---

## 💻 3. Prática: Simulando Arquitetura IoT com Python

Exemplo prático de um script em Python que simula a **Camada de Borda** capturando dados de um sensor e publicando em um Broker MQTT (**Camada de Nuvem**).

### Pré-requisito
```bash
pip install paho-mqtt
```

### Código do Dispositivo IoT (Edge)
```python
import time
import random
import paho.mqtt.client as mqtt

# Configurações do Broker MQTT (Nuvem Pública de Testes)
BROKER = "hivemq.com"
PORT = 1883
TOPICO_TELEMETRIA = "escola/iot/sala1/temperatura"

# Inicializa o cliente MQTT
cliente = mqtt.Client()
cliente.connect(BROKER, PORT, 60)

print("📡 Dispositivo IoT Iniciado. Enviando dados...")

try:
    while True:
        # Simulando a Camada de Percepção (Leitura de um sensor DHT22)
        temperatura_simulada = round(random.uniform(20.0, 30.0), 2)
        
        # Publicando os dados na nuvem (Camada de Rede -> Aplicação)
        print(f"Enviando: {temperatura_simulada}°C para o tópico {TOPICO_TELEMETRIA}")
        cliente.publish(TOPICO_TELEMETRIA, payload=str(temperatura_simulada), qos=1)
        
        # Intervalo de leitura
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Dispositivo desconectado.")
    cliente.disconnect()
```

---

## 🛡️ 4. Desafios de Segurança em IoT

A superfície de ataque em IoT é ampla devido à distribuição geográfica dos dispositivos.

*   **Camada Física:** Roubo ou adulteração do hardware do sensor.
*   **Camada de Rede:** Ataques do tipo *Man-in-the-Middle* (MitM). Solução: Uso de TLS/SSL (MQTTS).
*   **Camada de Aplicação:** Falha na autenticação. Solução: Uso de chaves de criptografia e tokens (X.509 certificates).

---

## 📝 Projeto de Fixação da Disciplina

**Objetivo:** Desenhar o diagrama arquitetural de um sistema de Monitoramento Agrícola Inteligente.
O aluno deve especificar por escrito em seu relatório técnico:
1. Qual sensor será usado na terra (Percepção).
2. Qual microcontrolador processará os dados (Borda).
3. Qual tecnologia de rádio enviará o dado da fazenda para a cidade (Rede).
4. Como os dados serão visualizados pelo fazendeiro (Aplicação).



