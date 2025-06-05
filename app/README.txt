# 🚀 ZapAgendamentos

Sistema de agendamento inteligente via WhatsApp, com suporte a planos, cupons, gamificação, organizações e promoções integradas.

## 📦 Instalação Local

```bash
# Clonar o repositório
$ git clone https://github.com/JeanMRocha/zapagendamentos.git
$ cd zapagendamentos

# Criar ambiente virtual (opcional)
$ python -m venv .venv
$ source .venv/bin/activate  # Linux/macOS
$ .venv\Scripts\activate   # Windows

# Instalar dependências
$ pip install -r requirements.txt
```

## 🧱 Estrutura de Banco de Dados

Para iniciar o banco de dados local (SQLite):
```bash
python app/database/init_db.py
```
Isso criará o arquivo `zapagendamentos.db` com todas as tabelas do projeto.

## ✨ Funcionalidades Atuais

- Gerenciamento de usuários e planos
- Sistema de créditos e bônus
- Recompensas por engajamento e ranking local
- Cupons e campanhas de indicação
- Organizações com conselhos e relatórios financeiros
- Script automatizado de premiação mensal (`app/premiacao_mensal.py`)

## 🔜 Próximas Etapas

- Integração com WhatsApp Cloud API
- Automações com n8n
- Painel administrativo
- API REST com FastAPI (opcional)

## 📁 Estrutura Recomendada

```
app/
├── modelos/               # Todos os modelos SQLAlchemy separados por tema
├── database/              # Scripts de banco e inicialização
├── premiacao_mensal.py    # Script mensal de bônus/ranking
└── ...                    # Demais módulos do projeto
```

---

## 🧠 Créditos
Projeto modelado com foco em escalabilidade, marketing de alta conversão e performance operacional. Desenvolvido com apoio de IA especializada e princípios de arquitetura limpa.
