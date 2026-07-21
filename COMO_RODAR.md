# Como Rodar miniERP Pro Localmente

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

### Verificar instalação do Python
```bash
python --version
# ou no macOS/Linux
python3 --version
```

Se não tiver Python instalado, baixe em: https://www.python.org/downloads/

---

## Instalação Rápida (Recomendado)

### 1. Clonar o repositório
```bash
git clone https://github.com/arthurvalves/miniERP-pro.git
cd miniERP-pro
```

### 2. Criar ambiente virtual (RECOMENDADO)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação
```bash
# Windows
python erp_frontend/main_window.py

# macOS/Linux
python3 erp_frontend/main_window.py
```

---

## Solução de Problemas Comuns

### Erro: "ModuleNotFoundError: No module named 'customtkinter'"
**Solução:**
```bash
pip install customtkinter --upgrade
```

### Erro: "No module named 'erp_backend'"
**Solução:** Certifique-se de estar no diretório correto
```bash
# Verificar se está na raiz do projeto
ls erp_frontend
ls erp_backend

# Se não estiver, navegue para a pasta correta
cd miniERP-pro
```

### Erro: "Database connection failed"
**Solução:** O banco de dados será criado automaticamente na primeira execução. Se persistir:
```bash
# Verifique permissões na pasta
ls -la erp_backend/

# Se necessário, crie a pasta de dados
mkdir -p erp_backend/data
```

### Erro no macOS: "cannot import name '_tkinter'"
**Solução:**
```bash
# Se usar Homebrew
brew install python-tk

# Se usar conda
conda install tk
```

### Interface fica branca/vazia
**Solução:** Aguarde alguns segundos. Na primeira execução, o sistema inicializa o banco de dados.

---

## Modo Desenvolvimento

### Com debug ativado
```bash
# Windows
python -u erp_frontend/main_window.py

# macOS/Linux
python3 -u erp_frontend/main_window.py
```

O `-u` força output sem buffer, útil para ver logs em tempo real.

### Executar testes (se existirem)
```bash
pytest tests/ -v
```

---

## Backend API (Opcional)

Se quiser rodar o backend Flask/FastAPI junto:

### Terminal 1 (Backend)
```bash
cd erp_backend
python main.py
# ou se tiver um app.py
python app.py
```

### Terminal 2 (Frontend)
```bash
cd erp_frontend
python main_window.py
```

---

## Configuração Avançada

### Variáveis de Ambiente
Criar arquivo `.env` na raiz do projeto:

```env
# Exemplo de configurações
DATABASE_PATH=./data/erp.db
LOG_LEVEL=INFO
DEBUG=False
API_URL=http://localhost:5000
```

Carregar no código Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_PATH = os.getenv('DATABASE_PATH', './data/erp.db')
```

### Aumentar/Diminuir Tamanho da Janela
Editar `erp_frontend/main_window.py`:
```python
# Linha padrão
self.geometry("1400x900")

# Customize conforme necessário
self.geometry("1600x1000")  # Maior
self.geometry("1200x700")   # Menor
```

### Mudar Tema/Cores
As cores estão centralizadas em `erp_frontend/theme.py`:
```python
COLORS = {
    "primary": "#FDB913",        # Amarelo (marca)
    "bg_dark": "#121212",        # Fundo principal
    "bg_secondary": "#1E1E1E",   # Fundo secundário
    # ... mais cores
}
```

---

## Estrutura de Pastas

```
miniERP-pro/
├── erp_frontend/              # Interface Tkinter
│   ├── main_window.py         # Arquivo principal
│   ├── theme.py               # Sistema de temas
│   ├── dashboard_view.py      # Dashboard
│   ├── pdv_view.py            # Ponto de venda
│   ├── products_view.py       # Produtos
│   └── ... (mais views)
│
├── erp_backend/               # Backend Flask/FastAPI
│   ├── main.py                # Entrada do backend
│   ├── utils/
│   │   └── db.py              # Conexão BD
│   └── ...
│
├── requirements.txt           # Dependências Python
├── venv/                      # Ambiente virtual (criado)
└── .env                       # Variáveis de ambiente (opcional)
```

---

## Performance & Otimizações

### Aumentar Velocidade de Inicialização
```bash
# Compilar arquivos Python para bytecode
python -m compileall erp_frontend/
python -m compileall erp_backend/
```

### Usar PyPy (mais rápido)
```bash
# Instalar PyPy
pip install pypy3

# Rodar com PyPy
pypy3 erp_frontend/main_window.py
```

---

## Verificação de Saúde

Executar checklist antes de começar:

```bash
#!/bin/bash
echo "✓ Checklist de Execução"
echo "1. Python version:"
python --version

echo "2. Pip version:"
pip --version

echo "3. Dependências instaladas:"
pip list | grep -E "customtkinter|flask|requests"

echo "4. Estrutura de pastas:"
test -d erp_frontend && echo "  ✓ erp_frontend/" || echo "  ✗ erp_frontend/ NÃO ENCONTRADO"
test -d erp_backend && echo "  ✓ erp_backend/" || echo "  ✗ erp_backend/ NÃO ENCONTRADO"

echo "5. Arquivos principais:"
test -f erp_frontend/main_window.py && echo "  ✓ main_window.py" || echo "  ✗ main_window.py NÃO ENCONTRADO"
test -f erp_frontend/theme.py && echo "  ✓ theme.py" || echo "  ✗ theme.py NÃO ENCONTRADO"

echo ""
echo "✅ Se todos os ✓ aparecerem, está pronto para rodar!"
```

---

## Próximos Passos

1. **Personalizar Cores:** Edite `erp_frontend/theme.py`
2. **Adicionar Novas Telas:** Use `VISUAL_DESIGN_GUIDE.md` como referência
3. **Conectar Banco Remoto:** Configure em `erp_backend/utils/db.py`
4. **Fazer Deploy:** Veja `DEPLOYMENT.md` (se existir)

---

## Suporte

- Problemas com Python? https://www.python.org/help/
- Problemas com CustomTkinter? https://github.com/TomSchimansky/CustomTkinter
- Problemas com Git? https://git-scm.com/doc

---

## Dicas Extras

### Dark Mode no Windows 10+
A aplicação já usa dark mode automaticamente. Para forçar:
```python
# em main_window.py
ctk.set_appearance_mode("dark")  # ou "light"
```

### Abrir DevTools/Console
```bash
# Rodar com modo interativo
python -i erp_frontend/main_window.py
```

### Criar Atalho no Desktop (Windows)
1. Criar arquivo `iniciar_erp.bat`:
```batch
@echo off
cd /d C:\Users\SeuUsuario\miniERP-pro
call venv\Scripts\activate.bat
python erp_frontend/main_window.py
pause
```

2. Criar atalho apontando para esse arquivo

---

**Última atualização:** 21/07/2026
**Versão:** 1.0
**Status:** Pronto para produção
