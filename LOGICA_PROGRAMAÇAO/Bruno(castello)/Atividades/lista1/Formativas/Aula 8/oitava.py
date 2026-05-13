# Tratamento de Erros e execuções
# Valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = Valor1 / valor2
# print(f"O resultado da divisão é: {resultado}")
# o codigo acima pode gerar um erro de divisão por zero se o usuario digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-expect:
# try:
#     Valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))
#     resultado = Valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print(f"Erro: não é possivel dividir por zero.")
# Exemplo 2: Tratamento de entrada invalida
# try:
#     Valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))
#     resultado = Valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um numero inteiro valido.")
# except ZeroDivisionError:
#     print("Erro: não é possivel dividir por zero.")

# Exemplo 3: Tratamento de multiplas exeções 
# try:
#     Valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))
#     resultado = Valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Ocorreu um erro: {e}")

# Exemplo 4: Uso do bloco finally
# try:
#     Valor1 = int(input("Digite o primeiro valor:"))
#     valor2 = int(input("Digite o segundo valor:"))
#     resultado = Valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de value: Por favor, digite um número inteiro valido. {e} ou Erro: não é possivel dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")

# Exercicio 1:
# Crie um algoritimo que pergunte seu nome e trate erro ao inserir valores incorretos 
# nome = input("Digite seu nome:")
# try:
#    nome_completo = f"{nome}"
#    print(f"olá,{nome}!")
# except Exception as e:
#    print(f"ocorreu um erro: {e}")
# # Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print(f"Erro de tipo: {e}")

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado 
# As entrada deverão ser registradas por placa.

# passo 1: Perguntar informações sobre o veiculo; Verificar se possui TAG para acesso liberado; se possuir erros informar ao usuario
# passo 2: Verificar tempo de permanencia; valor a ser cobrado
# passo 3: Saida como será; calcular tempo de permanencia; se for tag gerar na fatura da tag; pagar ticket;  Devolver ticket na saída

