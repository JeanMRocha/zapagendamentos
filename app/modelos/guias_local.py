from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS guias_local (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                registro_prefeitura TEXT,
                experiencia TEXT,
                especialidade TEXT,
                foto_url TEXT,
                aprovado BOOLEAN DEFAULT 0
            )
        """)
        conn.commit()