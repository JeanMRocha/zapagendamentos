from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS votos_evento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_votacao INTEGER,
                cpf TEXT,
                resposta TEXT,
                data_voto TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                anonimo BOOLEAN DEFAULT 1,
                FOREIGN KEY (id_votacao) REFERENCES votacoes_evento(id)
            )
        """)
        conn.commit()