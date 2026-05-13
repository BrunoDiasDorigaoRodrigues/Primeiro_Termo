# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontercer (como ler 10 sensores ou processar uma lisa de peças).
# Exemplo: Relatorio de produção Diaria
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1,6):
#     print(f"Processando lote número{lote}...")
#     print("Qualidade Verificada. [OK]")
#     print("Produção do dia finalizada!")

#     # Exemplo 2
# for b in range(10):
#         print(f"Quantidade total {b} foi...")

# # Exemplo 3 
# # Imagine o seguinte cenario, iremos produzir 20 discos de vinil.
# for vinil in range(1,21):
#         print(f"produção de {vinil},diaria")
    
# Exemplo 4 

# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
# itempecas = ["Cilindra", "Duplo", "prego", "orelha", "redondo", "Philips", "Universal"]

# for item in pecas:
#         print(f"Item em estoque: {item}")

# Exemplo 5 
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja a partir da seleção ele listar os produtos
# print("Menu de opções")
# print("Escolha um das opções:")
# print("Jogos J e S para Sair da compra")

# escolha = input("Digite sua escolha:")

# if escolha == "J":
#    print("Você escolheu Jogos")
# jogo = ["god of war", "Fortnite", "Hollow Knight", "Resident Evil", "Minecraft", "Roblox", "Call of Duty"]

# for jogo in jogo:
#         print(f"Jogos em estoque: {jogo}")
# Compra = float(input("Digite sua escolha:"))

# print("Você escolheu:", Compra)

# elif: escolha == "S"
# print("")