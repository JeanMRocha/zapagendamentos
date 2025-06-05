from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS candidatos_vaga (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vaga_id INTEGER,
                telefone TEXT,
                nome TEXT,
                email TEXT,
                resumo_profissional TEXT,
                data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (vaga_id) REFERENCES vagas_emprego(id),
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()