from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS conversas_recentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_prestador INTEGER,
                mensagem TEXT,
                origem TEXT, -- visitante, cliente_logado, admin, bot
                resposta TEXT,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY (id_prestador) REFERENCES usuarios(id)
            )
        """)

        conn.commit()