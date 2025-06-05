from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS ponto_guia_relacao (
                ponto_id INTEGER,
                guia_id INTEGER,
                observacao TEXT,
                PRIMARY KEY (ponto_id, guia_id),
                FOREIGN KEY (ponto_id) REFERENCES pontos_turisticos(id),
                FOREIGN KEY (guia_id) REFERENCES guias_local(id)
            )
        """)
        conn.commit()