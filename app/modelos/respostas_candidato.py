from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS respostas_candidato (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vaga_id INTEGER,
                telefone TEXT,
                pergunta_id INTEGER,
                resposta TEXT,
                FOREIGN KEY (vaga_id) REFERENCES vagas_emprego(id),
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone),
                FOREIGN KEY (pergunta_id) REFERENCES perguntas_vaga(id)
            )
        """)
        conn.commit()