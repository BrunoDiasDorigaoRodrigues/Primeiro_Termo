# Primeiro_Termo
Material de aula para o 1ºTermo - LOPAL - SOP - ARI - LER

## LOPAL
logica de programação em python

## SOP
Sistemas Operacionais


# 📑 Resumo Integrado das Disciplinas (Foco: Python)
Este documento consolida os conceitos fundamentais abordados nas disciplinas de Lógica de Programação, Arquitetura de IoT e Sistemas Operacionais.
---## 1. 🐍 Lógica de ProgramaçãoA base para o desenvolvimento de algoritmos estruturados e resolução de problemas computacionais.

*   **Estruturas Fundamentais:** Uso de variáveis (`str`, `int`, `float`), operadores lógicos (`and`, `or`, `not`) e condicionais (`if/elif/else`) para ditar o fluxo do software.
*   **Laços de Repetição:** Controle de iterações através de estruturas baseadas em condições (`while`) ou sequências definidas (`for` com `range`).*   **Engenharia de Requisitos:** Divisão entre o que o sistema faz (**Requisitos Funcionais**) e restrições de desempenho ou segurança (**Requisitos Não Funcionais**).
---## 2. 🌐 Arquitetura de IoT (Internet das Coisas)A infraestrutura que conecta o mundo físico ao ambiente digital por meio de redes de dados.
*   **Modelo em 4 Camadas:**
    1.  *Percepção:* Sensores e atuadores físicos (ex: DHT11).
    2.  *Processamento de Borda (Edge):* Tratamento local dos dados (ex: ESP32, Raspberry Pi).
    3.  *Rede/Conectividade:* Protocolos de transporte leves de dados (ex: MQTT, Wi-Fi, LoRaWAN).
    4.  *Aplicação/Nuvem:* Armazenamento e exibição de dashboards (ex: AWS IoT, TagoIO).
*   **Implementação:** Uso da biblioteca `paho-mqtt` em Python para simular um dispositivo de borda enviando dados em tempo real para a nuvem.
---## 3. 🐧 Sistemas Operacionais (SO)O software que gerencia o hardware e fornece a base de execução para programas e aplicativos.
*   **Arquitetura do Kernel:** Separação entre o Modo Usuário (aplicações seguras) e Modo Kernel (acesso direto ao hardware) via Chamadas de Sistema (*System Calls*).
*   **Concorrência e Paralelismo:** Divisão de tarefas através de Processos (espaço isolado) e Threads (memória compartilhada), simulados em Python com o módulo `threading`.*   **Gerenciamento de Recursos:** Algoritmos de escalonamento de CPU (como *Round Robin*) e controle de conflitos de hardware que podem gerar travamentos mútuos (**Deadlocks**).
---## 🔗 Mapa de Conexão entre as Disciplinas
No mercado de tecnologia atual, estas três áreas atuam de forma totalmente integrada:


[ Lógica de Programação ] ──► Cria os algoritmos e regras de negócio do sistema.
│
▼
[ Sistemas Operacionais ] ──► Agenda e executa esses algoritmos na CPU via Threads.
│
▼
[ Arquitetura de IoT ] ──► Conecta múltiplos sistemas operacionais leves na rede.


