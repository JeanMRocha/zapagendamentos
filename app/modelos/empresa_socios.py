
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS empresa_socios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                empresa_id INTEGER,
                nome TEXT,
                cpf TEXT,
                papel TEXT,
                telefone TEXT,
                autorizado BOOLEAN DEFAULT 0,
                FOREIGN KEY (empresa_id) REFERENCES empresas(id)
            )
        """)
        conn.commit()
