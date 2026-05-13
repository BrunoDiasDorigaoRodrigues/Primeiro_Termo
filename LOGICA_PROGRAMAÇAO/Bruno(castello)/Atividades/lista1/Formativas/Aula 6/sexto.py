#1.
#print("Registro de veiculo")
#modelo = input("Qual o modelo do veículo?...")
#placa = input("Qual e a placa do veículo?...")
#print(f"Veículo {modelo} de placa {placa} registrando no sistema.Boa viagem")

#2.
#print("Cálculo de Autonomia")
#tanque = float(input("Qual é a capacidade de seu tanque em Litros"))
#consumo = float(input("Digite o consumo médio por caminhão em Km/L"))
#total = tanque / consumo
#print(f"Seu caminhão pode percorrer {total:.2f} em Km/l")
#print("Seu caminhão pode percorrer", round(total,2), "em Km/l")

#3.
# print("Conversor de Moeda (Frete Internacional)")
# valor = float(input("Qual é o valor em reais ue será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa?..."))
# total = valor_reais / taxa_dolar
# print(f"O valor total convertido é... {total:.2f}")

#4.
# print("Media de Entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) / 3
# print(f"A média {media:.2f} de tempo das entregas")

#5.
# print("Monitor de carga")
# peso = float(input("Qual é o peso atual do seu caminhão?..."))

# if peso <10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("Carga padrão")
# else:
#     print("Alerta excesso de peso")

#6.
# print("Classificador de Destino")
# print("Regiões = N - Região Norte, S - Região Sul, Qualquer outra - Inernacional")
# regiao = input("Inserir o código da Região:").lower()
# if regiao == "N".upper() or regiao == "n".lower():
#     print("Região Norte")
# elif regiao == "S".upper() or regiao == "s".lower():
#     print("Região Sul")
# else: 
#     print("Região Internacional")

#7.
# print("Liberação de Saída")
# checklist = input("O checklist foi concluído [Concluído]")
# motorista = input("O motorista foi indentificado? [Sim ou Não]")
# if checklist == "concluído" or motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else:
#     print("Veículo não autorizado a iniciar a rota. Verificar checklist e indentificação do motorista.")

#8.
# print("Calculo de atraso")
# total_entregas = int(input("Total de Entregas Agendadas:..."))
# total_atrasos = int(input("Total de Entregas em Atrasos:..."))
# if total_atrasos > total_entregas * 0.1:
# else:
#     print("Logística Eficiente")
     
#9.
# print("Validação de Calibragem")
# pressao = float(input("Digite a presão do pneu em PSI:...."))
# if 100 <= pressao <= 100:
#     print("Dentro do padrão")
# elif pressao< 100:
#     print("Abaixo do recomendado")
# else:
#     print("Acima do recomendado")  

# 10.

# print("Contagem de Embarque")
# import time
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("Portão Trancado")

# 11.
# print("Somatorio de frete (Acumulador)")
# total = 0
# while True:
#     valor = float(input("Valor do Frete: "))
#     if valor == 0:
#         total += valor
#         print(f"Total acumulado {total} do frete")
#  print("Somatorio de Frete (Acumulador) - versão 2 ")
# faturamento_total = 0
# valor_frete = -1

# while valor_frete !=0:
#     valor_frete = float(input("Valor do frete ou 0 para encerrar"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado: R$ {faturamento_total}")
# print("Somatorio de Frete (Acumulador) - versão 3 ")

# b = 0
# while True:
#     t = int(input("Valor Frete..."))
#     c = int(input("Quer continuar s/n"))
#     b += t
#     if c == "s":
#         continue
#     else:
#         break
# print(f"Faturamento total {b}acumulado")

# 12.
# print("Monitoramento de Frota")
# maior_Km = 0
# for frota in range(1,6):
#     km = float(input(f"Digite a quilometragem do veiculo {frota}:"))
# if km > maior_Km:
#     maior_Km
# print(f"A maior quilometragem registrada é: {maior_Km} km.")

# 13.
# print("Sistema de Rastreio")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativas = 3
# while tentativas < max_tentativas:
#    codigo_input = input("Código de acesso para o rastreador:")
#    if codigo_input == codigo_correto:
#        print("Acesso permitido. Iniciando rastreamento...")
#        break
#    else:
#        tentativas += 1
#        print("Acesso negado")
#        if tentativas < max_tentativas:
#            print(f"Tentativas restantes: {max_tentativas}")
        
# else:
#     print("Rastreamento Bloqueado")\


