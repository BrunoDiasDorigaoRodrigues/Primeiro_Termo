# # # Exercicio 1
# # # 1. contador de produção (for)
# # # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada numero, imprima: 
# # # "Peça nº X processa com sucesso". No final, exiba "Ciclo de produção concluido".

# # for ciclo in range(1,11):
# #     print(f" peça nº{ciclo}...")
# #     print("processada com sucesso")
# #     print("Ciclo de produção concluido")

# # Exercicio 2 
# # Imaginea produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 banaas, 5 mangas, 10 melancias e 13 abacaxi.

# #No fim da produção gostaria de ter um total das produções

# # print("Está e sua lista de compras:")
# # for banana in range(1,11):
# #     print(f"Banana nº{banana}")
# # print("------------")
# # for manga in range(1,6):
# #     print(f"Manga nº{manga}")
# # print("------------")
# # for melancia in range(1,11):
# #     print(f"Malancia nº{melancia}")   
# # print("------------")
# # for abacaxi in range(1,14):
# #     print(f"abacaxi nº{abacaxi}")   

# # total = banana + manga + melancia + abacaxi
# # print("Foram produzidos: \n", round(total,2))

# # Exercicio 3 
# # Montar uma tabuada pode ser usado por um valor fixo e depois usar a pergunta 

# print("Tabuada")
# tab = int(input("Digite qual tabuada você quer:"))
# for numero in range(1,11):
#     resultado = tab * numero
#     print(f"{tab} x {numero} = {resultado}")

