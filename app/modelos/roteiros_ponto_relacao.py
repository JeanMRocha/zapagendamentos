from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS roteiros_ponto_relacao (
                roteiro_id INTEGER,
                ponto_id INTEGER,
                ordem INTEGER,
                destaque BOOLEAN DEFAULT 0,
                tempo_estadia TEXT,
                PRIMARY KEY (roteiro_id, ponto_id),
                FOREIGN KEY (roteiro_id) REFERENCES roteiros_comerciais(id),
                FOREIGN KEY (ponto_id) REFERENCES pontos_turisticos(id)
            )
        """)
        conn.commit()