# Funções são blocos de código reutilizáveis.
#o "f" no python, usado antes das aspas de uma string(com f"texto (variavel)"}, indice que se trata de uma f-string(ou formatted string literal). Ele informa ao Pyhon que as string contem expressoes entre chaves {} que devem ser avaliadas em um tempo de execução e substituidas pelos seus valores reais.
# def saudacao(nome):
#     return f"olá, {nome}!"

# mensagem = saudacao("Bruno")
# print(mensagem)

# def age(idade):
#     return f"sua idade é, {idade}!"
# mensagem = age("16")
# print(mensagem)

def boas_vindas(nome, cargo):
    print(f"olá, {nome}! você é o novo {cargo}.")
          
boas_vindas("Bruno", "desenvolvedor")
boas_vindas("Cris", "gerente")
boas_vindas("joão", "professor")

# Conversões

nome = input("Seu nome: ")
idade = int(input("sua idade: ")) #converte texto para inteiro
print(f"{nome} tem {idade} anos.")
