
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS empresas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf_cnpj TEXT,
                tipo_cadastro TEXT CHECK(tipo_cadastro IN ('profissional', 'empresa')) DEFAULT 'profissional',
                telefone TEXT,
                email TEXT,
                bairro_id INTEGER,
                distrito_id INTEGER,
                cep TEXT DEFAULT '28770-000',
                endereco_detalhado TEXT,
                cidade TEXT DEFAULT 'Santa Maria Madalena',
                plano_id TEXT,
                status TEXT DEFAULT 'pendente',
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
