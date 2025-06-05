# export_trechos.py
from datetime import datetime
import os

def exportar_codigo(nome_arquivo, conteudo, tipo='codigo'):
    data = datetime.now().strftime("%Y-%m-%d")
    pasta = f"revisoes/{data}"
    os.makedirs(pasta, exist_ok=True)
    nome_completo = f"{pasta}/{nome_arquivo}.{tipo}.txt"
    
    with open(nome_completo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    
    print(f"✅ Exportado para {nome_completo}")

# Exemplo de uso:
codigo = """
# arquivo: main.py
# trecho: conexão com supabase

def conectar_supabase():
    ...
"""
exportar_codigo("main_conexao", codigo)
