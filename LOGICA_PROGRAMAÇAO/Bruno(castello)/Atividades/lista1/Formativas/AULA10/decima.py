# Tratamento de Erros e Depuração
# try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. 
# O código dentro do bloco try é executado normalmente, mas se ocorrer um erro,
# o controle é passado para o bloco expect, onde podemos lídar com a situação de fora apropriada.

try:
    numero = int(input("Digite um número:"))
    resultado = 10 / numero
    print("O resultado é:", resultado)

except ValueError:
    print("Erro: você deve digitar um número válido.")

except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")

except KeyboardInterrupt:
    print("\n programa interrompido")

except TypeError:
    print("Erro: Tipo de dado inválido.")

except Exception as erro:
    print("Erro inesperado:", erro)     





