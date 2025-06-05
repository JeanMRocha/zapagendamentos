from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        # Tabela de litígios privados entre cidadãos
        c.execute("""
            CREATE TABLE IF NOT EXISTS litigios_privados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone_denunciante TEXT,
                telefone_envolvido TEXT,
                tipo TEXT, -- barulho, ameaça, invasão, animais soltos, etc.
                descricao TEXT,
                local TEXT,
                evidencias TEXT, -- links, fotos, vídeos
                status TEXT DEFAULT 'pendente', -- pendente, em mediação, resolvido, arquivado
                moderador_atribuido TEXT,
                orgao_encaminhado TEXT,
                visibilidade TEXT DEFAULT 'restrita', -- restrita, encaminhada, pública
                data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (telefone_denunciante) REFERENCES usuarios(telefone),
                FOREIGN KEY (telefone_envolvido) REFERENCES usuarios(telefone)
            )
        """)

        # Histórico de mediação e comentários internos
        c.execute("""
            CREATE TABLE IF NOT EXISTS mediacoes_litigio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_litigio INTEGER,
                autor TEXT,
                tipo TEXT, -- mensagem, resposta, acordo, pedido de documento
                conteudo TEXT,
                data_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                publico BOOLEAN DEFAULT 0,
                FOREIGN KEY (id_litigio) REFERENCES litigios_privados(id)
            )
        """)

        conn.commit()