from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS alugueis_materiais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                tipo TEXT, -- tenda, mesa, cadeira, equipamento, salão, etc.
                categoria TEXT, -- eventos, construção, agricultura, etc.
                quantidade_disponivel INTEGER,
                unidade TEXT, -- diária, hora, pacote etc.
                preco TEXT,
                preco_promocional TEXT,
                forma_pagamento TEXT,
                caucao TEXT,
                dias_disponiveis TEXT, -- JSON ou CSV com dias da semana
                horario_retirada TEXT,
                horario_devolucao TEXT,
                prazo_minimo TEXT,
                prazo_maximo TEXT,
                observacoes TEXT,
                termos_uso TEXT,
                cidade TEXT DEFAULT 'Santa Maria Madalena',
                distrito TEXT,
                bairro TEXT,
                endereco TEXT,
                contato TEXT,
                link_fotos TEXT,
                destaque BOOLEAN DEFAULT 0,
                aprovado BOOLEAN DEFAULT 0,
                ativo BOOLEAN DEFAULT 1,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()