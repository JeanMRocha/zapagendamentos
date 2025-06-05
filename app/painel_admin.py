
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_PATH = "data/zap.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def buscar_categorias():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("SELECT nome FROM categorias ORDER BY nome")
        return [row[0] for row in c.fetchall()]

def buscar_tipos(categoria_nome):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM categorias WHERE nome = ?", (categoria_nome,))
        cat_id = c.fetchone()
        if not cat_id:
            return []
        c.execute("SELECT nome FROM tipos_servico WHERE categoria_id = ?", (cat_id[0],))
        return [row[0] for row in c.fetchall()]

def salvar_servico(dados):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            INSERT INTO produtos_servicos (nome, descricao, preco, tipo, cidade, categoria, disponivel_hoje, patrocinado)
            VALUES (?, ?, ?, ?, ?, ?, 1, 0)
        """, (
            dados["nome"], dados["descricao"], dados["preco"], dados["tipo"],
            dados["cidade"], dados["categoria"]
        ))
        conn.commit()

def cadastrar():
    try:
        preco = float(preco_entry.get().replace('.', '').replace(',', '.'))
    except ValueError:
        messagebox.showerror("Erro", "Preço inválido.")
        return
    dados = {
        "nome": nome_entry.get(),
        "descricao": descricao_entry.get(),
        "preco": preco,
        "tipo": tipo_var.get(),
        "cidade": cidade_entry.get(),
        "categoria": categoria_var.get()
    }
    salvar_servico(dados)
    messagebox.showinfo("Sucesso", "Serviço cadastrado com sucesso.")

def atualizar_tipos(event):
    tipos = buscar_tipos(categoria_var.get())
    tipo_combo["values"] = tipos
    if tipos:
        tipo_var.set(tipos[0])

# Interface
root = tk.Tk()
root.title("Cadastro de Serviço - ZapAgendamentos")
root.geometry("600x500")

tk.Label(root, text="Nome").pack()
nome_entry = tk.Entry(root, width=60)
nome_entry.pack()

tk.Label(root, text="Descrição").pack()
descricao_entry = tk.Entry(root, width=60)
descricao_entry.pack()

tk.Label(root, text="Preço").pack()
preco_entry = tk.Entry(root, width=20)
preco_entry.pack()

tk.Label(root, text="Cidade").pack()
cidade_entry = tk.Entry(root, width=40)
cidade_entry.insert(0, "Santa Maria Madalena")
cidade_entry.pack()

tk.Label(root, text="Categoria").pack()
categoria_var = tk.StringVar()
categoria_combo = ttk.Combobox(root, textvariable=categoria_var, state="readonly")
categoria_combo["values"] = buscar_categorias()
categoria_combo.bind("<<ComboboxSelected>>", atualizar_tipos)
categoria_combo.pack()

tk.Label(root, text="Tipo").pack()
tipo_var = tk.StringVar()
tipo_combo = ttk.Combobox(root, textvariable=tipo_var, state="readonly")
tipo_combo.pack()

tk.Button(root, text="Cadastrar Serviço", command=cadastrar).pack(pady=10)

root.mainloop()
