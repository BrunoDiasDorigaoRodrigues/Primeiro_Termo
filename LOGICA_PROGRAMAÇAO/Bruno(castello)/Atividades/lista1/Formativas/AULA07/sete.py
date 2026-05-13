# #clean code
# # para que Usar?
# # como usar?
# # print("Clena code - Aula 7")
# # aula = 7
# # print(f"Estamos na aula {aula} de clean code")

# # 1.
# Seu_NickName = input("Digite seu nickname:")
# Seu_Nivel = input("Digite o seu nivel:")
# print(f"O jogador {Seu_NickName} está no nível {Seu_Nivel} e está pronto para a partida!")

# # 2.
# Valor_Mesada = int(input("Digite o valor da sua mesada:"))
# total_da_Mesada = Valor_Mesada * 4
# print("Então no final do mês você terá:", total_da_Mesada)

# # Manipulação de arquivos e Texto
# manipular_Texto = " Python é Muito legal! "
# print(manipular_Texto.strip().upper()) # "Python"
# print(manipular_Texto.strip().lower()) # "python"
# print(manipular_Texto.strip().startswith("A")) # "Começar com Letras Inicial"
# print(manipular_Texto.strip().capitalize()) # "Letra Inicial"
# print(manipular_Texto.strip().title()) # "Titulo"
# print(manipular_Texto.strip().replace(" ","_")) # "Prencher Vazios"
# print(manipular_Texto.strip().split()) # "Separar palavras"


# #Exercicio 1
# # Crie um programa que peça ai usuario para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações;
# # - Deixe o texto em letras minúsculas

# Texto = input("Digite uma frase:")
# print(Texto.strip().lower())

# # Manipular Arquivos:
# # Escrevendo
# with open("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code")
#     texto.write("\n Estamos evoluindo")

# # Lendo 
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# Exemplo 1:
# Crie um programa que leia o conteudo de um arquivo de texto e conte quantas vezes a palavra "Python" 
# aparece no arquivo. Exiba o resultado para o usuario
# print("Contagem de palavras em arquivo")
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("Python") #contar a palavra "Python"
#     # palavra "Python"
#     contagem = conteudo.lower().count("python")
# print(f"A contagem de palavras {contagem} é de ...")

# interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# onde estou?
print(os.getcwd())

print(os.listdir())
print(os.listdir("c:/users"))

# Criar pastas
os.mkdir("Bruno")
# Criar arquivos

# Renomear pastas
os.rename("Nova_Pasta", "Minha_Pasta")

# apagar pastas
os.rmdir("Bruno")


