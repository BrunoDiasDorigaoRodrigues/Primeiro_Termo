
# 🐧 Sistemas Operacionais (SO)
Este material serve como guia teórico e prático para o entendimento do funcionamento interno dos sistemas operacionais, gerenciamento de recursos de hardware e execução de processos.
---## 🏗️ 1. Visão Geral e Arquitetura do SO
O Sistema Operacional atua como uma camada de abstração entre o hardware do computador e as aplicações do usuário.


[ Aplicações do Usuário (Navegador, Editores, Jogos) ]
│ (System Calls / Chamadas de Sistema)
▼
[ Kernel do SO (Gerenciamento de Processos, Memória, Arquivos) ]
│ (Drivers de Dispositivos)
▼
[ Hardware Físico (Processador, Memória RAM, Armazenamento) ]


### 1.1. O Kernel (Núcleo)
*   **Modo Usuário:** Modo de execução restrito onde rodam os aplicativos comuns. Impede o acesso direto ao hardware por segurança.
*   **Modo Kernel:** Modo de execução com privilégios totais de acesso ao hardware.
*   **Chamadas de Sistema (System Calls):** A interface de programação que permite a um programa em Modo Usuário solicitar serviços ao Kernel.

---

## 🔄 2. Gerenciamento de Processos e Threads

*   **Processo:** Um programa em execução na memória, possuindo seu próprio espaço de endereçamento isolado.
*   **Thread:** A menor unidade de execução dentro de um processo. Múltiplas threads dentro do mesmo processo compartilham os mesmos recursos de memória.

### 💻 Prática: Criando Múltiplas Threads em Python
O Python permite simular a concorrência de tarefas em um sistema operacional através do módulo `threading`.

```python
import threading
import time

def tarefa_sistema(nome, tempo):
    print(f"[Thread {nome}] Iniciada.")
    time.sleep(tempo) # Simula o processamento/espera de E/S (I/O)
    print(f"[Thread {nome}] Finalizada após {tempo}s.")

# Criando instâncias de threads simulando processos concorrentes
thread_1 = threading.Thread(target=tarefa_sistema, args=("A", 3))
thread_2 = threading.Thread(target=tarefa_sistema, args=("B", 1))

# Inicializando as threads (O SO agenda a execução)
thread_1.start()
thread_2.start()

# Aguarda ambas terminarem para fechar o programa principal
thread_1.join()
thread_2.join()
print("⚠️ Todas as tarefas do SO foram concluídas.")
```

---

## 📅 3. Escalonamento de Processos

O Escalonador do SO decide qual processo utilizará a CPU a cada instante de tempo (Multiprogramação).

### Algoritmos Principais
1.  **FIFO / FCFS (First-In, First-Out):** O primeiro processo a chegar é o primeiro a ser servido. Não é preemptivo.
2.  **SJF (Shortest Job First):** Executa primeiro o processo que demanda menor tempo de CPU.
3.  **Round Robin (Alternância Circular):** Cada processo recebe um tempo fixo de CPU (Quantum). Se não terminar, volta para o fim da fila. É a base dos sistemas de tempo compartilhado.

---

## 🧠 4. Gerenciamento de Memória

O SO precisa alocar e proteger a memória RAM para que um processo não mude os dados de outro.

*   **Memória Virtual:** Técnica que utiliza o armazenamento em disco para simular memória RAM extra.
*   **Paginamento:** Divisão da memória física em blocos de tamanho fixo (frames/quadros) e a memória lógica em blocos de mesmo tamanho (páginas).
*   **Thrashing:** Fenômeno que ocorre quando o sistema passa mais tempo trocando páginas entre a RAM e o disco (Swap) do que executando instruções úteis.

---

## 🔒 5. Concorrência e Deadlocks

Quando múltiplos processos compartilham recursos escassos (arquivos, impressoras, variáveis), podem ocorrer conflitos.

*   **Condição de Corrida (Race Condition):** Ocorre quando dois ou mais processos modificam dados compartilhados simultaneamente, tornando o resultado imprevisível.
*   **Deadlock (Impasse):** Situação em que dois ou mais processos ficam permanentemente bloqueados, pois cada um espera por um recurso que está retido pelo outro.

### As 4 Condições de Coffman para ocorrer Deadlock:
1.  **Exclusão Mútua:** O recurso só pode ser usado por um processo por vez.
2.  **Posse e Espera:** Um processo retém um recurso enquanto espera por outro.
3.  **Não Preempção:** Um recurso não pode ser tomado à força de um processo.
4.  **Espera Circular:** Uma cadeia de processos onde cada um espera por um recurso do próximo.

---

## 📝 Atividade de Fixação

**Simulação Teórica:**
Imagine um cenário com três processos ($P_1, P_2, P_3$) que chegam ao mesmo tempo no escalonador com tempos de execução de $8ms$, $4ms$ e $2ms$, respectivamente.

Calcule o **Tempo Médio de Espera** caso o algoritmo utilizado pelo Sistema Operacional seja:
1.  **FCFS (Ordem: P1, P2, P3)**
2.  **SJF (Shortest Job First)**



