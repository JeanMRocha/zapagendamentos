from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                telefone TEXT UNIQUE,
                email TEXT,
                chave_pix TEXT,
                stripe_id TEXT,
                data_nascimento TEXT,
                genero TEXT,
                cor TEXT,
                renda TEXT,
                endereco TEXT,
                cep TEXT DEFAULT '28770-000',
                distrito TEXT,
                bairro TEXT,
                plano TEXT DEFAULT 'gratuito',
                status TEXT DEFAULT 'ativo',
                saldo INTEGER DEFAULT 0,
                is_master BOOLEAN DEFAULT 0,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def registrar_usuario(nome, telefone, cpf=None, email=None, is_master=False):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            INSERT OR IGNORE INTO usuarios (nome, telefone, cpf, email, is_master)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, telefone, cpf, email, int(is_master)))
        conn.commit()

def is_usuario_master(telefone):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("SELECT is_master FROM usuarios WHERE telefone = ?", (telefone,))
        resultado = c.fetchone()
        return resultado and resultado[0] == 1

def obter_usuario_por_telefone(telefone):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE telefone = ?", (telefone,))
        return c.fetchone()

def simular_usuarios_teste():
    registrar_usuario("Jean Rocha", "+550000000001", cpf="000.000.000-01", is_master=True)
    registrar_usuario("Carlos Silva", "+550000000002", is_master=False)
    registrar_usuario("Ana Prestadora", "+550000000003", is_master=False)