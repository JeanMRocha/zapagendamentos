from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS perguntas_vaga (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vaga_id INTEGER,
                pergunta TEXT,
                tipo_resposta TEXT,  -- texto, múltipla escolha, etc.
                opcoes TEXT,          -- se aplicável
                obrigatoria BOOLEAN DEFAULT 1,
                FOREIGN KEY (vaga_id) REFERENCES vagas_emprego(id)
            )
        """)
        conn.commit()