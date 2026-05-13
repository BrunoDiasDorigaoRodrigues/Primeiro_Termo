# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

#corrigido
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")
# elif idade >= 16:
#     print("Você não é de maior")

# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

#Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#Corrigido
# numero = 10
# if numero > 5:
#  print("O número é maior que cinco.")
# else:
#  print("O número é menor ou igual a cinco.")

# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

#Corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#   print("Login realizado com sucesso.")

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#Corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")


# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

#Corrigido
# pontos = 50
# print(f"Parabéns! Você fez + {pontos} pontos.")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

#Corrigido
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
#  print("Aprovado")
# elif nota >= 9:
#  print("Excelente!")


#
#  8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

#Corrigido
#  Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
for i in range(5,1):
    print(f"{i}")


# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas
# 
# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")