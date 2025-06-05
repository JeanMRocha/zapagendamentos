-- Arquivo base de estrutura inicial: app/database/schema_base.sql

-- Tabelas principais
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120),
    telefone VARCHAR(20),
    email VARCHAR(120),
    chave_pix VARCHAR(120),
    agendamentos_mes INTEGER DEFAULT 0,
    agendamentos_total INTEGER DEFAULT 0,
    categoria_atual VARCHAR(50),
    ranking_posicao INTEGER,
    badge VARCHAR(100),
    telefone_confirmado BOOLEAN DEFAULT FALSE,
    email_confirmado BOOLEAN DEFAULT FALSE
);

CREATE TABLE planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    limite_creditos_mensal INTEGER,
    val_recompensa INTEGER,
    val_validade_credito INTEGER,
    bonus_primeira_compra INTEGER,
    bonus_recorrencia INTEGER,
    limite_acumulo_creditos INTEGER
);

-- Recompensas e gamificação
CREATE TABLE categorias_uso (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE,
    min_agendamentos INTEGER NOT NULL,
    max_agendamentos INTEGER,
    recompensa_creditos INTEGER DEFAULT 0,
    validade_dias INTEGER DEFAULT 15,
    selo VARCHAR(100),
    destaque_publico BOOLEAN DEFAULT FALSE
);

CREATE TABLE bonus (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    tipo VARCHAR(50),
    valor_creditos INTEGER,
    validade TIMESTAMP,
    descricao VARCHAR(255),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE conquistas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    agendamentos_necessarios INTEGER NOT NULL,
    beneficio VARCHAR(100),
    icone VARCHAR(100),
    descricao TEXT
);

CREATE TABLE conquistas_usuarios (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    conquista_id INTEGER REFERENCES conquistas(id),
    data_conquista TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rankings_mensais (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    cidade VARCHAR(100),
    mes VARCHAR(7),
    posicao INTEGER,
    destaque BOOLEAN DEFAULT FALSE
);

-- Cupons e campanhas
CREATE TABLE cupons (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    criado_por_usuario_id INTEGER REFERENCES usuarios(id),
    valor_creditos INTEGER,
    validade TIMESTAMP,
    usos_maximos INTEGER DEFAULT 1,
    usos_atuais INTEGER DEFAULT 0,
    descricao VARCHAR(255)
);

CREATE TABLE usos_cupom (
    id SERIAL PRIMARY KEY,
    cupom_id INTEGER REFERENCES cupons(id),
    usuario_id INTEGER REFERENCES usuarios(id),
    data_uso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE campanhas_indicacao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    ativo BOOLEAN DEFAULT TRUE,
    data_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_fim TIMESTAMP,
    bonus_indicador INTEGER DEFAULT 0,
    bonus_indicado INTEGER DEFAULT 0,
    uso_limite_por_usuario INTEGER DEFAULT 1
);

CREATE TABLE brindes_indicacao (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    campanha_id INTEGER REFERENCES campanhas_indicacao(id),
    tipo VARCHAR(50),
    creditos INTEGER DEFAULT 0,
    entregue BOOLEAN DEFAULT FALSE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Organizações
CREATE TABLE organizacoes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    tipo VARCHAR(20),
    descricao TEXT,
    cnpj VARCHAR(18) UNIQUE,
    ativa BOOLEAN DEFAULT TRUE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE organizacoes_membros (
    id SERIAL PRIMARY KEY,
    organizacao_id INTEGER REFERENCES organizacoes(id),
    usuario_id INTEGER REFERENCES usuarios(id),
    funcao VARCHAR(50),
    direito_voto BOOLEAN DEFAULT FALSE,
    acesso_total BOOLEAN DEFAULT FALSE,
    data_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_saida TIMESTAMP
);

CREATE TABLE relatorios_financeiros (
    id SERIAL PRIMARY KEY,
    organizacao_id INTEGER REFERENCES organizacoes(id),
    periodo_inicio TIMESTAMP,
    periodo_fim TIMESTAMP,
    descricao TEXT,
    total_receitas INTEGER,
    total_despesas INTEGER,
    publicado BOOLEAN DEFAULT FALSE
);
