from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        # Tabela principal de denúncias
        c.execute("""
            CREATE TABLE IF NOT EXISTS denuncias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                categoria TEXT,
                titulo TEXT,
                descricao TEXT,
                local TEXT,
                foto TEXT,
                status TEXT DEFAULT 'pendente',
                data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                aprovado BOOLEAN DEFAULT 0,
                anonima BOOLEAN DEFAULT 0,
                responsavel_orgao TEXT,
                prazo_resposta INTEGER DEFAULT 5,
                data_resposta TEXT,
                resolvido_por TEXT,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)

        # Tabela de respostas da denúncia
        c.execute("""
            CREATE TABLE IF NOT EXISTS respostas_denuncia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_denuncia INTEGER,
                autor TEXT,
                tipo TEXT, -- resposta, observacao, orientacao, pedido_documento
                mensagem TEXT,
                data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_denuncia) REFERENCES denuncias(id)
            )
        """)

        conn.commit()