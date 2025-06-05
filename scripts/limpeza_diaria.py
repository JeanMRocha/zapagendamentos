import sqlite3
from datetime import datetime, timedelta

DB_PATH = "zapagendamentos.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def mover_inativos():
    conn = conectar()
    cursor = conn.cursor()

    limite = (datetime.now() - timedelta(days=90)).isoformat()

    cursor.execute("""
    SELECT telefone, data_criacao FROM usuarios
    WHERE data_criacao <= ?
    """, (limite,))
    inativos = cursor.fetchall()

    for telefone, _ in inativos:
        # Verifica se já está na tabela de inativos
        cursor.execute("SELECT 1 FROM usuarios_inativos WHERE telefone = ?", (telefone,))
        if cursor.fetchone():
            continue

        print(f"[INATIVO] Movendo usuário {telefone}")
        cursor.execute("""
        INSERT INTO usuarios_inativos (telefone, data_inativacao)
        VALUES (?, ?)
        """, (telefone, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def excluir_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    limite = (datetime.now() - timedelta(days=5)).isoformat()

    cursor.execute("""
    SELECT telefone FROM exclusao_pendente
    WHERE data_solicitacao <= ? OR tipo = 'imediata'
    """, (limite,))
    a_excluir = cursor.fetchall()

    for telefone, in a_excluir:
        print(f"[EXCLUSAO] Apagando usuário {telefone}")
        cursor.execute("DELETE FROM usuarios WHERE telefone = ?", (telefone,))
        cursor.execute("DELETE FROM exclusao_pendente WHERE telefone = ?", (telefone,))
        # Em produção: transferir saldo via PIX aqui

    conn.commit()
    conn.close()

def exclusao_definitiva():
    conn = conectar()
    cursor = conn.cursor()

    limite = (datetime.now() - timedelta(days=365)).isoformat()

    cursor.execute("""
    SELECT telefone FROM usuarios_inativos
    WHERE data_inativacao <= ?
    """, (limite,))
    expirados = cursor.fetchall()

    for telefone, in expirados:
        print(f"[EXCLUSAO FINAL] Removendo cadastro definitivo {telefone}")
        cursor.execute("DELETE FROM usuarios_inativos WHERE telefone = ?", (telefone,))
        # Aqui você também pode remover de backups externos, logs, etc.

    conn.commit()
    conn.close()
def verificar_integridade():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA integrity_check")
    result = cursor.fetchone()[0]
    conn.close()
    if result != "ok":
        raise Exception("Erro de integridade no banco de dados!")
    
def executar_limpeza():
    print("🚀 Iniciando limpeza diária...")
    mover_inativos()
    excluir_pendentes()
    exclusao_definitiva()
    print("✅ Limpeza finalizada.")

if __name__ == "__main__":
    executar_limpeza()
