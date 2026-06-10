# 1

# import tkinter as tk
# from tkinter import messagebox, ttk

# def registro():
#     nome_operador = operador_registro.get()
#     nome_turno = turno_reg.get()
    
#     if nome_operador == "" and turno_reg == "":
#         messagebox.showwarning("Por favor, digite seu nome!!")
#     else:
#         messagebox.showinfo("Bem-vindo", f"Olá {nome_operador} seu setor é {nome_turno}")

# janela_Bemvindo = tk.Tk()
# janela_Bemvindo.title("REGISTRO")
# janela_Bemvindo.geometry("720x600")

# lbl_mensagem_operador = tk.Label(janela_Bemvindo, text="Digite seu nome :")
# lbl_mensagem_operador.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem_turno = tk.Label(janela_Bemvindo, text="Selecione seu turno: ")
# lbl_mensagem_turno.grid(row=0, column=2, pady=10, padx=10)

# operador_registro = tk.Entry(janela_Bemvindo, font=("Arial", 12), width=20)
# operador_registro.grid(row=1, column=0, pady=10, padx=10)

# turno_registro = tk.Entry(janela_Bemvindo, font=("Arial", 12), width=20)
# operador_registro.grid(row=1, column=1, pady=10, padx=10)

# turno_reg = tk.ttk.Combobox(janela_Bemvindo, values=["A", "B", "C"], width=30)
# turno_reg.grid(row=1, column=2, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_Bemvindo, text="Enviar mensagem", command=registro, bg="#ffe600" , fg="black")
# btn_enviar_mensagem.grid(row=3, column=1, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_Bemvindo, text="Fechar janela", command=janela_Bemvindo.destroy,  bg="#ff1100" , fg="black")
# btn_fechar_janela.grid(row=3, column=2, pady=10, padx=10) 

# janela_Bemvindo.mainloop()

# 2

# import tkinter as tk
# from tkinter import messagebox, ttk

# def Cálculo_de_Produção():
#     qntd_produção = int(produção_qntd.get())
#     peças_produção = int(produção_peças.get())
    
#     if  qntd_produção == "" and  peças_produção == "":
#         messagebox.showwarning("Por favor, digite seu nome!!")
#     else:
#         total = qntd_produção * peças_produção
#         messagebox.showinfo("Bem-vindo", f"A quantidade de horas produzidas é de {qntd_produção} o total de horas e de {total} horas")

# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações Usuarios")
# janela_bemvindo.geometry("500x500")

# lbl_mensagem_produção = tk.Label(janela_bemvindo, text="Digite a quantidade de peças em 1 hora:")
# lbl_mensagem_produção.grid(row=1, column=0, pady=10, padx=10)

# lbl_mensagem_qntd = tk.Label(janela_bemvindo, text="Selecione a quantidade de horas produzidas :")
# lbl_mensagem_qntd.grid(row=0, column=0, pady=10, padx=10)

# produção_qntd = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# produção_qntd.grid(row=0, column=1, pady=10, padx=10)

# produção_peças = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# produção_peças.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Eviar Mensagem", command=Cálculo_de_Produção)
# btn_enviar_mensagem.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy,  bg="#ff0000" , fg="black")
# btn_fechar_janela.grid(row=3, column=2, pady=10, padx=10)



# janela_bemvindo.mainloop()

# 3 

# import tkinter as tk
# from tkinter import messagebox

# def registrar_conversor():
#     bar = entry_bar.get()
#     psi = float(bar) * 14.5 
#     if bar and psi is not None:
#         messagebox.showinfo("Conversor de Unidade", f"Pressão em Bar: {bar}. Quantidade em PSI: {psi}.")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha o campo corretamente.")
    
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Conversor de Unidade")
# janela.geometry("300x200")

# # # Widgets
# label_hora = tk.Label(janela, text="Pressão em Bar:")
# label_hora.pack(pady=5)
# entry_bar = tk.Entry(janela)
# entry_bar.pack(pady=5)
# button_registrar = tk.Button(janela, text="Converter", command=registrar_conversor)
# button_registrar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()

# 4
# import tkinter as tk
# from tkinter import messagebox, ttk

# def Cálculo_de_media():
#     primeira_nota = int(nota_primeira.get())
#     segunda_nota = int(nota_segunda.get())
#     terceira_nota = int(nota_terceira.get())

#     if  primeira_nota == "" and  segunda_nota == "":
#         messagebox.showwarning("")
#     else:
#         total = (primeira_nota + segunda_nota + terceira_nota) /3
#         messagebox.showinfo("Bem-vindo", f"A media e de {total}")

# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações Usuarios")
# janela_bemvindo.geometry("500x500")

# lbl_mensagem_produção = tk.Label(janela_bemvindo, text="Digite o Primeiro numero:")
# lbl_mensagem_produção.grid(row=1, column=0, pady=10, padx=10)

# lbl_mensagem_qntd = tk.Label(janela_bemvindo, text="Digite o Segundo numero :")
# lbl_mensagem_qntd.grid(row=2, column=0, pady=10, padx=10)

# lbl_mensagem_qntd = tk.Label(janela_bemvindo, text="Digite o Terceiro numero :")
# lbl_mensagem_qntd.grid(row=3, column=0, pady=10, padx=10)

# nota_primeira = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# nota_primeira.grid(row=1, column=1, pady=10, padx=10)

# nota_segunda = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# nota_segunda.grid(row=2, column=1, pady=10, padx=10)

# nota_terceira = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
# nota_terceira.grid(row=3, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Eviar Mensagem", command=Cálculo_de_media)
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy,  bg="#ff0000" , fg="black")
# btn_fechar_janela.grid(row=4, column=2, pady=10, padx=10)

# janela_bemvindo.mainloop()

# 5 
# import tkinter as tk
# from tkinter import messagebox, ttk

# def temperatura():
#     temperatura_motor = motor_temperatura.get()

#     if temperatura_motor <= "40°C":
#         messagebox.showinfo("Aviso!", "Baixa Carga!")

#     elif temperatura_motor > "40°C" and temperatura_motor < "70°C":
#         messagebox.showinfo("Aviso", "Carga Normal!")

#     else:
#         messagebox.showinfo("ALERTA",  "Resfriamento Ativado!")

# janela_temperatura = tk.Tk()
# janela_temperatura.title("Termostato")
# janela_temperatura.geometry("300x300")

# lbl_mensagem_temp = tk.Label(janela_temperatura, text="Qual a temperatura do motor? ")
# lbl_mensagem_temp.grid(row=1, column=1, pady=10, padx=10)
# motor_temperatura = tk.Entry(janela_temperatura, font= ("Arial", 12), width=30)
# motor_temperatura.grid(row=2, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_temperatura, text="Enviar", command=temperatura, bg = "#ffffff", fg= "Black")
# btn_enviar_mensagem.grid(row=6, column=1, pady=10, padx=10)

# btn_clicar_fechar = tk.Button(janela_temperatura, text="Fechar Janela", command=janela_temperatura.destroy, bg = "#ff0000", fg = "Black")
# btn_clicar_fechar.grid(row=7, column=1, pady=10, padx=10)

# janela_temperatura.mainloop()

# 6.
# import tkinter as tk
# from tkinter import messagebox, ttk

# def lotes():
#     produto_lote = lote_produto.get()

#     if produto_lote == "A":
#         messagebox.showinfo("Alimentos", "Você escolheu alimentos!")

#     elif produto_lote == "E":
#         messagebox.showinfo("Eletrônicos", "Você escolheu Eletrônicos!")

#     else:
#         messagebox.showwarning("ALERTA!", "Produto Desconhecido!!!")
    
# janela_lotes = tk.Tk()
# janela_lotes.title("Classificador de Lotes")
# janela_lotes.geometry("400x200")

# lbl_mensagem_lote = tk.Label(janela_lotes, text="Insira o código do produto: ")
# lbl_mensagem_lote.grid(row=1, column=1, pady=10, padx=10)
# lote_produto = tk.Entry(janela_lotes, font= ("Arial", 12), width=40)
# lote_produto.grid(row=2, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_lotes, text="Enviar Mensagem", command=lotes, bg = "#64ff50", fg= "Black")
# btn_enviar_mensagem.grid(row=6, column=1, pady=10, padx=10)

#7
