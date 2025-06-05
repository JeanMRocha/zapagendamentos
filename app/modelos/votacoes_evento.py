from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS votacoes_evento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_agenda INTEGER,
                pergunta TEXT,
                opcoes TEXT,
                privada BOOLEAN DEFAULT 1,
                aberta_para TEXT,
                aberta BOOLEAN DEFAULT 1,
                resultado_publico BOOLEAN DEFAULT 0,
                FOREIGN KEY (id_agenda) REFERENCES agenda_oficial(id)
            )
        """)
        conn.commit()