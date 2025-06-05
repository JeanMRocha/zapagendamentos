from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS respostas_automaticas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                tipo_pergunta TEXT,
                padrao_pergunta TEXT,
                resposta_automatica TEXT,
                palavras_chave TEXT,
                ativo BOOLEAN DEFAULT 1,
                id_produto_servico INTEGER, -- NOVO: vincula diretamente a um item
                tipo_origem TEXT DEFAULT 'manual', -- NOVO: manual, banco, IA
                fonte_dados TEXT, -- ex: tabela nome, link de origem, módulo externo
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY (id_produto_servico) REFERENCES produtos_servico(id)
            )
        """)

        conn.commit()