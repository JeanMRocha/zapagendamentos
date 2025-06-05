from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS interesses_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                tipo_interesse TEXT,
                palavras_chave TEXT,
                ultima_interacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                nivel_interesse INTEGER DEFAULT 1, -- escala de 1 a 5
                origem TEXT DEFAULT 'conversa',
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        """)

        conn.commit()