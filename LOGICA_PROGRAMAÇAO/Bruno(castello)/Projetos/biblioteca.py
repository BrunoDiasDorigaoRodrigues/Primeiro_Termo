# import tkinter as tk
# from tkinter import messagebox, ttk

# def biblioteca():
#     livro_aluno = aluno_livro.get()

#     if livro_aluno == "":
#         messagebox.showwarning("Tipo de usuario")
#     else:
#         messagebox.showinfo("Bem-vindo", f"Olá {livro_aluno}")
# # janela
# janela_biblioteca = tk.Tk()
# janela_biblioteca.title("Biblioteca")
# janela_biblioteca.geometry("1920x1080")

# # labels
# lbl_messagem_aluno = tk.Label(janela_biblioteca, text="Tipo de Usuário: ")
# lbl_messagem_aluno.grid(row=0,column=1,pady=10,padx=10)

# lbl_messagem_aluno = tk.Label(janela_biblioteca, text="Título do Livro : ")
# lbl_messagem_aluno.grid(row=1, column=1, pady=10, padx=10)

# lbl_messagem_aluno = tk.Label(janela_biblioteca, text="nome de usuario: ")
# lbl_messagem_aluno.grid(row=2, column=1, pady=10, padx=10)

# lbl_messagem_aluno = tk.Label(janela_biblioteca, text=" Categoria do Livro: ")
# lbl_messagem_aluno.grid(row=0, column=3, pady=10, padx=10)

# lbl_messagem_aluno = tk.Label(janela_biblioteca, text="Regras de Negócio\nAlunos: até 14 dias de graça\nomunidade: até 7 dias de graça\nTaxa adicional: R$ 5,00 por dia extra\nLivros Raros: apenas para alunos")
# lbl_messagem_aluno.grid(row=2, column=3, pady=10, padx=10)

# lbl_messagem_aluno = tk.Label(janela_biblioteca, text=" Dias de Empréstimo: ")  
# lbl_messagem_aluno.grid(row=1, column=3, pady=10, padx=10)


# #Entrys
# titulo_livro = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# titulo_livro.grid(row=1,column=2,pady=10,padx=10)

# nome_usuario = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# nome_usuario.grid(row=2,column=2,pady=10,padx=10)

# aluno_emprestimo = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# aluno_emprestimo.grid(row=1,column=4,pady=10,padx=10)


# # componentes
# como_nivel = tk.ttk.Combobox(janela_biblioteca, values=["Aluno", "comunidade"], width=30)
# como_nivel.grid(row=0,column=2,pady=10,padx=10)

# como_nivel = tk.ttk.Combobox(janela_biblioteca, values=["comum", "raro"], width=30)
# como_nivel.grid(row=0,column=4,pady=10,padx=10)




# # botões
# btn_enviar_mensagem = tk.Button(janela_biblioteca, text="Validar emprestimo")

# janela_biblioteca.mainloop()