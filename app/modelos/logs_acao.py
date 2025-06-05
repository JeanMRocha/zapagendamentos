from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS logs_acao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                acao TEXT,
                tabela_afetada TEXT,
                registro_id INTEGER,
                telefone_responsavel TEXT,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()