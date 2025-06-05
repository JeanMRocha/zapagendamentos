from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS preferencias_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER UNIQUE,
                interesse_saude BOOLEAN DEFAULT 0,
                interesse_turismo BOOLEAN DEFAULT 0,
                interesse_eventos BOOLEAN DEFAULT 0,
                interesse_empregos BOOLEAN DEFAULT 0,
                interesse_pets BOOLEAN DEFAULT 0,
                interesse_doacoes BOOLEAN DEFAULT 0,
                interesse_esportes BOOLEAN DEFAULT 0,
                interesse_compras BOOLEAN DEFAULT 0,
                interesse_educacao BOOLEAN DEFAULT 0,
                interesse_servicos BOOLEAN DEFAULT 0,
                interesse_alertas_publicos BOOLEAN DEFAULT 0,
                receber_notificacoes BOOLEAN DEFAULT 1,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        """)

        conn.commit()