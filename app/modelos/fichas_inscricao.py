from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS fichas_inscricao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curso_id INTEGER,
                pergunta TEXT,
                tipo_resposta TEXT,
                opcoes TEXT,
                obrigatoria BOOLEAN DEFAULT 1,
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )
        """)
        conn.commit()