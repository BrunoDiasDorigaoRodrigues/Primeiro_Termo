# Exerciico 1 
# tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (Simulando uma falha de sensor especifica no item 5)

# for sensor in range(1,11):
#     if sensor == 5: 
#      print(f"sensor nº{sensor}com falha")
#     print(f"sensor {sensor} sem falha")
#     continue
# print("fim! :)")

# Exercicio 2
# Simule um semaforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o continue para pular a cor amarela (Simulando um semaforo com defeito que não acende a luz amarela)

# cores = ["verde", "Amarelo", "Vermelho"]

# for cor in cores:
#     if cor == "Amarelo":
#         print(f"O sinal está com {cor} defeito")
#     print(f"O sinal está em funcionamente {cor}")

# Exercicio 3 - soma de cargas de Energia (for)
# Uma fabrica tem 5 maquinas. peça ao usuario (Via input dentro do loop) o consumo em KWh de uma das maquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# for maq in range(1,6):
#     maquina = float(input("Digite o valor que deseja da {maq} nº"))
#     total = maq * 5
# print("o total de consumo e de", total)

# Exercicio 4 - indentificar de peças Defeituosas (for + if)
# percorra uma lista de medidas de peças:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cda peça, diga se ela está "Aprovada" ou "Rejeitada"

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for med in medidas:
#     if med >= 50.0:
#         print(f"peça Aprovada {med}")
#     elif med <= 50.00:
#         print(f"peça Reprovada {med}")
# print("\nFim da avaliação")
# Exercicio 5 - Uma balança industrial está pensando um lote de 6 sacos de insumos.
# peso ideal de cada saco é de 50kg, mas o sistema aceita cariações.
# Crie um programa que peça ao usuario o peso de cada saco (Via input dentro do loop) e,
# para cada um, informe se ele está "Dentro do limite" (Entre 48kg e 52kg) ou "fora do limite".
 
# Escolha = float(input("qual e o peso de cada saco?: "))
# pesos = [50.0, 48.00, 52]
# for peso in pesos:
#     if 48 < Escolha <= 52.0:
#         print(f"peso Aprovado {peso}")
#     else:
#         print(f"peso fora do limite {peso}")

# O desafio: gestão de ciclo termico
# você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças 
# Regras do sistema: O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuario a temperatura atual (input).
# Filtro de Erro (continue): Se o usuario digita uma temperatura negativa, exiba "Erro de leitura no sensor" 
# e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergencia (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRITICO: Risco de Explosão!", 
# interromper o loop imediatamente e encerrar o programa

