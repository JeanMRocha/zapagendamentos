from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS respostas_solicitacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                solicitacao_id INTEGER,
                prestador_id INTEGER,
                proposta_valor TEXT,
                mensagem TEXT,
                aceita BOOLEAN DEFAULT 0,
                data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (solicitacao_id) REFERENCES solicitacoes_servico(id),
                FOREIGN KEY (prestador_id) REFERENCES empresas(id)
            )
        """)
        conn.commit()