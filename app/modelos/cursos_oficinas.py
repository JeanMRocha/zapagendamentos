from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS cursos_oficinas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                descricao TEXT,
                ementa TEXT,
                metodologia TEXT,
                instrutores TEXT,
                certificacao_tipo TEXT, -- participação, qualificação, obrigatória etc.
                modalidade TEXT, -- presencial, online, híbrido
                duracao TEXT,
                carga_horaria TEXT,
                faixa_etaria TEXT,
                publico_alvo TEXT,
                local TEXT,
                endereco TEXT,
                cidade TEXT DEFAULT 'Santa Maria Madalena',
                distrito TEXT,
                bairro TEXT,
                organizador TEXT,
                link_inscricao TEXT,
                link_certificado TEXT,
                gratuito BOOLEAN DEFAULT 1,
                vagas_total INTEGER,
                vagas_disponiveis INTEGER,
                datas TEXT, -- JSON com datas específicas
                horario_inicio TEXT,
                horario_fim TEXT,
                precisa_levar TEXT,
                observacoes TEXT,
                aprovado BOOLEAN DEFAULT 0,
                destaque BOOLEAN DEFAULT 0,
                ativo BOOLEAN DEFAULT 1,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()