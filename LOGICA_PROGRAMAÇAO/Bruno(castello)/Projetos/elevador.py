# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# while True:
#     try:
#         print("Bem-vindo ao elevador")
#         andar_atual = 0

#         chamar = input("Você deseja chamar o elevador?: ")

#         if chamar == "N" or chamar == "n":
#             print("Você desejou não chamar o elevador")
#             break

#         elif chamar == "S" or chamar == "s":
#             print("O elevador está se locomovendo ao seu andar")

#             destino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#             pergunta_andar = input("Qual andar deseja se mover?: ")
#             quantidade = input("Quantas pessoas estão entrando?: ")

#             if quantidade >= "5":
#                 print("O peso está acima da capacidade\nO elevador deve fazer uma parada")
#                 break

#             elif quantidade <= "5":
#                 print("A capacidade está ok")

#             if pergunta_andar == "1":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 2):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "2":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 3):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "3":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 4):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "4":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 5):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "5":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 6):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "6":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 7):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "7":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 8):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "8":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 9):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "9":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 10):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#             if pergunta_andar == "10":
#                 print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
#                 print("Tela de Andar atual:")

#                 for andar in range(0, 11):
#                     print(f"Andar {andar}º")

#                 print("Você chegou ao seu destino")

#     except ValueError:
#         print("Ocorreu um erro")