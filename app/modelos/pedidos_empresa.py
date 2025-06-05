from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS pedidos_empresa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_produto INTEGER,
                quantidade INTEGER,
                preco_unitario TEXT,
                preco_total TEXT,
                forma_pagamento TEXT,
                observacoes TEXT,
                status TEXT DEFAULT 'recebido', -- recebido, confirmado, concluído, cancelado
                data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao TIMESTAMP,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY (id_produto) REFERENCES produtos_servico(id)
            )
        """)

        conn.commit()