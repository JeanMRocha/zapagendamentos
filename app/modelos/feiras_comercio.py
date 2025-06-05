from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        # Tabela de produtores ou comerciantes
        c.execute("""
            CREATE TABLE IF NOT EXISTS produtores_feira (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                cpf_cnpj TEXT,
                tipo TEXT, -- produtor, artesão, feirante, lojista
                descricao TEXT,
                cidade TEXT DEFAULT 'Santa Maria Madalena',
                distrito TEXT,
                bairro TEXT,
                endereco TEXT,
                aprovado BOOLEAN DEFAULT 0
            )
        """)

        # Tabela de produtos oferecidos
        c.execute("""
            CREATE TABLE IF NOT EXISTS produtos_feira (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_produtor INTEGER,
                nome TEXT,
                descricao TEXT,
                categoria TEXT, -- hortifruti, artesanato, alimentos, serviços, etc.
                preco TEXT,
                unidade TEXT,
                oferta BOOLEAN DEFAULT 0,
                estoque_disponivel TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ativo BOOLEAN DEFAULT 1,
                FOREIGN KEY (id_produtor) REFERENCES produtores_feira(id)
            )
        """)

        conn.commit()