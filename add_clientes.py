import tkinter as tk
import psycopg2
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de Clientes")

largura = 400
altura = 500
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int(largura_tela / 2 - largura / 2)
pos_y = int(altura_tela / 2 - altura / 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.resizable(False, False)

frame_campos = tk.Frame(janela)
frame_campos.pack(pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10)

def salvar_cliente():
    try:
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()

        if nome == "" or email == "" or telefone == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        conexao = psycopg2.connect(
            host="localhost",
            database="clientes_db",
            user="postgres",
            password="1010"
        )

        cursor = conexao.cursor()

        comando = """
        INSERT INTO clientes (nome, email, telefone)
        VALUES (%s, %s, %s)
        """

        cursor.execute(comando, (nome, email, telefone))

        conexao.commit()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)

    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao salvar: {erro}")

def listar_clientes():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="clientes_db",
            user="postgres",
            password="1010"
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        lista_clientes.delete(0, tk.END)

        for cliente in clientes:
            lista_clientes.insert(tk.END, cliente)
    except Exception as erro:
        print("Erro ao listar>", erro)

def deletar_cliente():
    try:
        cliente_selecionado = lista_clientes.get(tk.ACTIVE)
        id_cliente = cliente_selecionado[0]

        conexao = psycopg2.connect(
            host="localhost",
            database="clientes_db",
            user="postgres",
            password="1010"
        )
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")

        listar_clientes()

    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao deletar: {erro}")

def selecionar_cliente(event):
    try:
        cliente = lista_clientes.get(tk.ACTIVE)
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, cliente[1])

        entry_email.delete(0, tk.END)
        entry_email.insert(0, cliente[2])

        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(0, cliente[3])
    
    except Exception as erro:
        print("Erro ao selecionar:", erro)

def atualizar_cliente():
    try:
        cliente_selecionado = lista_clientes.get(tk.ACTIVE)
        id_cliente = cliente_selecionado[0]

        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()

        conexao = psycopg2.connect(
            host="localhost",
            database="clientes_db",
            user="postgres",
            password="1010"
        )
        cursor = conexao.cursor()
        comando = """
        UPDATE clientes
        SET nome = %s, email = %s, telefone = %s
        WHERE id = %s
        """
        cursor.execute(comando, (nome, email, telefone, id_cliente))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

        listar_clientes()

    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar: {erro}")

label_nome = tk.Label(frame_campos, text="Nome")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_campos, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_email = tk.Label(frame_campos, text="Email")
label_email.grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_campos, width=30)
entry_email.grid(row=1, column=1, padx=5, pady=5)

label_telefone = tk.Label(frame_campos, text="Telefone")
label_telefone.grid(row=2, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_campos, width=30)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

botao_salvar = tk.Button(frame_botoes, text="Cadastrar Cliente", width=15, command=salvar_cliente)
botao_salvar.grid(row=0, column=0, padx=5, pady=5)

botao_listar = tk.Button(frame_botoes, text="Listar Clientes", width=15, command=listar_clientes)
botao_listar.grid(row=0, column=1, padx=5, pady=5)

botao_deletar = tk.Button(frame_botoes, text="Deletar Cliente", width=15, command=deletar_cliente)
botao_deletar.grid(row=1, column=0, padx=5, pady=5)

botao_atualizar = tk.Button(frame_botoes, text="Atualizar Cliente", width=15, command=atualizar_cliente)
botao_atualizar.grid(row=1, column=1, padx=5, pady=5)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_clientes = tk.Listbox(frame_lista, width=50, height=10, yscrollcommand=scrollbar.set)
lista_clientes.pack()
scrollbar.config(command=lista_clientes.yview)

lista_clientes.bind("<<ListboxSelect>>", selecionar_cliente)

janela.mainloop()