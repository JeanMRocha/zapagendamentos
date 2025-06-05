from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS respostas_inscritos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curso_id INTEGER,
                telefone TEXT,
                pergunta_id INTEGER,
                resposta TEXT,
                FOREIGN KEY (curso_id) REFERENCES cursos(id),
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone),
                FOREIGN KEY (pergunta_id) REFERENCES fichas_inscricao(id)
            )
        """)
        conn.commit()