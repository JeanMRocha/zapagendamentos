from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS roteiros_comerciais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                preco REAL,
                duracao TEXT,
                pontos_ids TEXT,
                agencia_id INTEGER,
                guias_sugeridos TEXT,
                foto_url TEXT,
                ativo BOOLEAN DEFAULT 1
            )
        """)
        conn.commit()