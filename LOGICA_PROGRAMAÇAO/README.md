# 🐍 Curso de Lógica de Programação com Python

Este material serve como guia prático e teórico para o aprendizado de lógica estruturada utilizando a linguagem Python.

---

## 1. Introdução à Lógica e Variáveis

A lógica de programação consiste em organizar instruções passo a passo para resolver um problema. No Python, armazenamos dados na memória usando **variáveis**.

### Conceitos Chave
*   **Tipos de Dados:** `str` (texto), `int` (inteiro), `float` (decimal), `bool` (Verdadeiro/Falso).
*   **Comando de Saída:** `print()` exibe dados na tela.
*   **Comando de Entrada:** `input()` captura o que o usuário digita (sempre retorna texto).

### Exemplo Prático
```python
# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) # Convertendo texto para número inteiro

# Saída de dados com f-string
print(f"Olá {nome}, você tem {idade} anos.")
```

---

## 2. Operadores Matemáticos e Lógicos

Servem para realizar cálculos e comparações que guiam o fluxo do programa.

### Operadores Aritméticos
*   `+` (Adição) | `-` (Subtração) | `*` (Multiplicação) | `/` (Divisão)
*   `//` (Divisão Inteira) | `%` (Resto da Divisão) | `**` (Potência)

### Operadores de Comparação (Resultam em True ou False)
*   `>` (Maior) | `<` (Menor) | `==` (Igual) | `!=` (Diferente)

### Operadores Lógicos
*   `and`: Retorna `True` se **todas** as condições forem verdadeiras.
*   `or`: Retorna `True` se pelo menos **uma** condição for verdadeira.
*   `not`: Inverte o valor lógico.

---

## 3. Estruturas Condicionais (Tomada de Decisão)

Permitem que o programa execute blocos de código diferentes dependendo de uma condição. Em Python, a indentação (espaçamento) define o que está dentro do bloco.

### Estrutura `if`, `elif` e `else`
```python
nota = float(input("Digite a nota do aluno: "))

if nota >= 7.0:
    print("Aprovado!")
elif nota >= 5.0:
    print("Recuperação.")
else:
    print("Reprovado.")
```

---

## 4. Estruturas de Repetição (Loops)

Utilizadas para executar o mesmo bloco de código várias vezes sem duplicar linhas.

### Loop `while` (Baseado em uma condição)
Executa enquanto a condição for verdadeira. Requer atenção para evitar loops infinitos.
```python
contador = 1
while contador <= 5:
    print(f"Número: {contador}")
    contador += 1 # Incremento
```

### Loop `for` com `range()` (Baseado em uma sequência)
Ideal para repetir um bloco um número definido de vezes.
```python
# Executa de 0 até 4 (5 vezes)
for i in range(5):
    print(f"Repetição número {i}")
```

---

## 5. Listas (Estruturas de Dados)

Variáveis especiais que conseguem armazenar múltiplos valores de forma organizada.

```python
# Criando uma lista
frutas = ["Maçã", "Banana", "Laranja"]

# Adicionando item
frutas.append("Uva")

# Percorrendo a lista com o laço for
for fruta in frutas:
    print(f"Eu gosto de: {fruta}")
```

---

## 📝 Desafio de Aula (Projeto Integrado)

**Problema:** Crie um programa que simule uma calculadora de tabuada interativa. O sistema deve pedir um número ao usuário e exibir a tabuada de 1 a 10 deste número usando um laço de repetição.

```python
numero = int(input("Quer ver a tabuada de qual número? "))

print(f"\n--- Tabuada do {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```
