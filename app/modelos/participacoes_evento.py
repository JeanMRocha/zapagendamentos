from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS participacoes_evento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_agenda INTEGER,
                cpf TEXT,
                telefone TEXT,
                confirmado_presenca BOOLEAN DEFAULT 0,
                assinou_ata BOOLEAN DEFAULT 0,
                token_confirmacao TEXT,
                timestamp_confirmacao TIMESTAMP,
                assinatura_legal TEXT,
                tipo_participante TEXT,
                FOREIGN KEY (id_agenda) REFERENCES agenda_oficial(id)
            )
        """)
        conn.commit()