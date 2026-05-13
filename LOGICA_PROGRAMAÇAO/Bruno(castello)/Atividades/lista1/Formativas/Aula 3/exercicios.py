# Exercicio 1 
# Criar um algoritimo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você devera perguntar o nome do cliente do filme ou serie e quantidade que deseja assim como o valor de aluguel
# para filmes R$ 5,00 e para séries R$ 10,00

# print("Você esta na sessão de Filmes")
# nome = input("Digite seu nome")
# filmes = input("qual filme deseja")
# qtde = int(input("Qual quantidade deseja?"))
# valor = 5
# total = qtde * valor
# #print("parabens pela sua locação de filmes", nome,"E seu filme foi:", filmes, "A quantidade foi", qtde, "E sua locação custou", valor)
# print("Parabens pela locação:", nome, "E seu filme foi:", filmes, "A quantidade foi", qtde, "E, sua locação custou", valor)

# series = input("Qual serie deseja?")
# qtde = int(input("Qual quantidade deseja?"))
# valor = 5
# total = qtde * valor
# print("Parabens pela locação:", nome, "E sua serie foi:", series, "A quantidade foi", qtde, "E, sua locação custou", valor)

# Exercicios 2
# loja de comidas e doces
# criar um algoritimo para compra de produtos
# 1 - Comida
# 2 - Bebida
# 3 - Doces
# Ao escolher as opções cada um terá um valor de porcentegem, comida = 10%, bebida = 5%, doces = 2%

# print("Você está em uma loja de doces" "\n Este e o menu de opção \n 1 - Comida \n 2 - bebida \n 3 - Doces")
# opcao = int(input("Digite uma opção:"))

# if opcao == 1:
    
#     qtde = int(input("digite a quantidade:"))
#     print("Você está em comida")
#     print("temos PF, La Carte")
#     comida = input("O que deseja?")
#     valor = float(input("Digite o valor da comida:"))
#     desconto = valor * (10 / 100)
#     total = valor - desconto
#     print("Sua compra total foi de:", total)

# if opcao == 2:
    
#     qtde = int(input("digite a quantidade:"))
#     print("Você está em Bebida")
#     print("temos coca é pepsi")
#     comida = input("O que deseja?")
#     valor = float(input("Digite o valor da Bebida:"))
#     desconto = valor * (10 / 100)
#     total = valor - desconto
#     print("Sua compra total foi de:", total)

# if opcao == 3:
    
#     qtde = int(input("digite a quantidade:"))
#     print("Você está em Doce")
#     print("temos brigadeiro é beijinho")
#     comida = input("O que deseja?")
#     valor = float(input("Digite o valor da Doces:"))
#     desconto = valor * (10 / 100)
#     total = valor - desconto
#     print("Sua compra total foi de:", total)

# else:
#     print("Obrigado")

# # Exercicio 3 
# # calculadora com operadores 
# # Sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados.
 
# print("Qual o valor que voce deseja colocar? \nQual o segundovalor que voce deseja colocar? ")
# valor1 = int(input("Digite o primeiro valor:"))
# valor2 = int(input("Digite o segundo valor:"))

# Escolha = input("Qual operador deseja calcular?")

# if Escolha == ("+"):
#     ptotal = (valor1 + valor2)
#     print("o valor é: \n", round(ptotal,2))

# if Escolha == ("-"):
#     ptotal = (valor1 - valor2)
#     print("o valor é: \n", round(ptotal,2))

# if Escolha == ("*"):
#     ptotal = (valor1 * valor2)
#     print("o valor é: \n", round(ptotal,2))

# if Escolha == ("/"):
#     ptotal = (valor1 / valor2)
#     print("o valor é: \n", round(ptotal,2))

# else:
#     print("Isso não e um operador")

# Exercicio 4
# calculo de notas
# nossas atividades são por base de calculo em somativa 1 e somativa 2, no final temos um media. Acima ou igual a 50 o aluno será aprovado caso contrario reprovado
# o programa deverá perguntar o nome e as notas e apresentar o resultado final do aluno

# print("calculo de notas senai")
# nota1 = float(input("digite sua nota da somativa 1: \n "))
# nota2 = float(input("digite sua nota da somativa 2: \n "))
# ptotal = (nota1 + nota2) / 2
# print("as somativas doprimeiro semestre são: \n", round(ptotal,2))

# if ptotal >= 50:
#     print("Sua Somativa está na media")

# elif ptotal <= 50:
#         print("Sua Somativa está abaixo da media")

# # Exercicio 5 
# # Criar um algoritimo para calcular uma viagem de carro, ônibus e avião
# viagens de carro: deve ser feito um abastecimento e deve cobrar o valor do pedagio
# ônibus: deve ser cobrado o valor do seguro de 3,88
# avião: cobrar o valor da viagem e valor da taxa de embraque 55,20
# print("Você viajara" "\n Com qual veiculo? \n 1 - Carro \n 2 - Avião \n 3 - ônibus")
# opcão = int(input("Digite uma opção:"))

# if opcao == 1:

# pv1 = int(input("você tem que abastecer o valor será? \n"))
# pv2 = int(input("você está passando por um pedágio o valor será? \n"))
# print ("o valor gasto total foi de:", pv1+pv2)