from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS categorias_aluguel_sugeridas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                id_usuario INTEGER,
                comentario TEXT,
                aprovado BOOLEAN DEFAULT 0,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        """)
        conn.commit()