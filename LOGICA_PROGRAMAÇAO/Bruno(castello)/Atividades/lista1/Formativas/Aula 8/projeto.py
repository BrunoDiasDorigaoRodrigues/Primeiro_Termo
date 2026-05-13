print("Liberação de entrada")
print("Menu de opções\nTicket = T\nCartão = C")
escolha = input("Qual escolha de opção você deseja?:")

if escolha == "T".upper() or escolha == "t".lower():
    print("Você escolheu a opção de Ticket")
elif escolha == "C".upper() or escolha == "c".lower():
    print("Você escolheu a opção de cartão de acesso ")
else:
     print("Você não pode entrar no shopping")

if escolha == "T".upper() or escolha == "t".lower():
    modelo = input("Digite o modelo do seu veiculo:")
    placa = input("Digite a placa do seu veiculo:")
    tempo = input("Digite o tempo em que você ficou:")
    total = tempo*2
    print(f"Ok muito obrigado pelas informações!!\ninformações recebidas\nmodelo do veiculo: {modelo}\nPlaca do veiculo: {placa}")
    print(f"E você pagou",total)
    
elif escolha == "C".upper() or escolha == "c".lower():
    placa = input("Digite a placa do seu veiculo:")
    print(f"Então sua placa é: {placa}")
    print(f"Você possui tag?:")



