# Tratamento de Erros e Depuração
# try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. 
# O código dentro do bloco try é executado normalmente, mas se ocorrer um erro,
# o controle é passado para o bloco expect, onde podemos lídar com a situação de fora apropriada.

# try:
#     numero = int(input("Digite um número:"))
#     resultado = 10 / numero
#     print("O resultado é:", resultado)

# except ValueError:
#     print("Erro: você deve digitar um número válido.")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero")

# except KeyboardInterrupt:
#     print("\n programa interrompido")

# except TypeError:
#     print("Erro: Tipo de dado inválido.")

# except Exception as erro:
#     print("Erro inesperado:", erro)     

# Exercicio 1
# Escreva um programa que solicite ao usuário calcule a média de três números.
# O programa deve lidar com possíveis erros, como a entrada de valores não numericos ou a divisão por zero.
# while True:
#  try:
#     numero1 = int(input("Digite o primeiro número:"))
#     numero2 = int(input("Digite o segundo número:"))
#     numero3 = int(input("Digite o terceiro número:"))
#     resultado = 2 / numero1 + numero2 + numero3
#     print("O resultado é:", resultado)

#  except ZeroDivisionError:
#     print("você não deve dividir um número por zero")

#  except ValueError:
#     print("você deve digitar um número válido.")    

# Explicação de def: A palavra-chave "def" é usada para definir uma função em python. Uma função é um bloco de código reutilizar que
# realiza uma tarefa específica.
# return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a 
# função foi chamada. O valor retornando pode ser usado posteriormente no código.

# def nome_de_funcao(parametro1, parametro2):
#     Corpo da função (Codígo que será executado)
#     resultando = parametro1 + parametro2
#     return resultado

# Exemplo 1:
# def saudacao(nome, idade):
#     nome = input("Digite seu nome:")
#     idade = int(input("Digite sua idade:"))
#     return f"olá, {nome}, {idade}!"
# print(saudacao("",""))

# Exemplo 2:
# def calcular_media(num1, num2, num3):
#     try:
#         media = (num1 + num2 + num3) / 3
#         return media
#     except TypeError:
#         return "Erro: Todos os valores evem ser números."
#     except ZeroDivisionError:
#         return "Erro: Não é possivel dividir por zero"

# print(f"calcula_media {(calcular_media(10,20,30))}")

# Exemplo 3:
# def valores():
#     print("Digite três valores:")
#     a = int(input("Digite o primeiro valor:"))
#     b = int(input("Digite o segundo valor:"))
#     c = int(input("Digite o terceiro valor:"))
#     return a,b, c
# print(f"O maior valor é: {(valores())}")

# Exemplo 4:
# calcule o dobro de um número fornecido pelo úsuario, tratando erros de entrada inválida.
def calcular_dobro():
    try:
        valor_digitado = int(input("Digite o valor que deseja:)"))
        total_dobro = valor_digitado * 2
        return total_dobro

    except ValueError:
        print("Digite um número válido")
print(f"O calculo é: {calcular_dobro()}")