from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS inscritos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curso_id INTEGER,
                telefone TEXT,
                nome TEXT,
                cpf TEXT,
                data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                confirmado BOOLEAN DEFAULT 0,
                FOREIGN KEY (curso_id) REFERENCES cursos(id),
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()