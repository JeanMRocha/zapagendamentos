
# ZapAgendamentos - Sistema Local de Agendamento via WhatsApp

Este projeto simula o backend de um sistema de agendamentos e serviços locais usando Python com interface Tkinter e banco SQLite.

---

## 📦 Estrutura de Pastas

```
app/
│
├── banco.py                   # conexão e criação central
├── modelos/
│   ├── __init__.py
│   ├── usuarios.py
│   ├── empresas.py
│   ├── servicos.py
│   ├── eventos.py
│   ├── pontos_turisticos.py
│   ├── oportunidades.py
│   ├── candidaturas.py
│   ├── entidades_publicas.py
│   └── notificacoes.py
├── painel_admin.py
└── adicionar_categorias_tipos.py

---

## ▶️ Como Rodar o Sistema

### 1. Rodar o sistema principal (Madaleno)
```bash
python main.py
```

- Digite seu número de telefone ou "VISITANTE" para entrar sem cadastro.
- Pode buscar por palavras como "dentista", "cabeleireiro", "barbeiro".
- Admins podem usar comandos especiais (ver abaixo).

### 2. Rodar o painel administrativo
```bash
python painel_admin.py
```

- Permite cadastrar novos serviços com validação e sugestão automática.
- Permite aprovar serviços pendentes.

---

## 🔧 Comandos para Administradores

Certifique-se de cadastrar o número na tabela `admins`.

Exemplos de comandos:

```
DAR 10 CRÉDITOS PARA 21999999999
PLANO RUBI 1M PARA 21999999999
DESTACAR SERVIÇO 27
REMOVER DESTAQUE 27
```

---

## 💡 Recursos Implementados

- ✅ Cadastro parcial ou completo de usuários
- ✅ Modo visitante sem necessidade de login
- ✅ Limite de 2 serviços por busca (modo gratuito/visitante)
- ✅ Exibição priorizada de serviços patrocinados
- ✅ IA local com histórico para contexto
- ✅ Painel para cadastro e aprovação de conteúdo
- ✅ Verificação automática contra termos inapropriados
- ✅ Sugestão de correções com base em bom português

---

## ⚠️ Requisitos

- Python 3.8+
- Biblioteca `requests`, `tkinter`
- Servidor Ollama com modelo `mistral` rodando localmente:
```bash
ollama run mistral
```

---

© 2025 ZapAgendamentos • Desenvolvido por Jean Rocha
