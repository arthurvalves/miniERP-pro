#!/bin/bash

# ============================================================
# Script para iniciar miniERP Pro localmente
# Suporta: macOS, Linux, Windows (Git Bash)
# ============================================================

echo "╔════════════════════════════════════════════════════════╗"
echo "║        miniERP Pro - Inicializador de Aplicação       ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Detectar SO
OS_TYPE="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macOS"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    OS_TYPE="Windows"
fi

echo -e "${BLUE}Sistema Operacional: ${OS_TYPE}${NC}"
echo ""

# 1. Verificar Python
echo -e "${YELLOW}[1/5] Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}✗ Python não encontrado!${NC}"
        echo "Por favor, instale Python 3.8+ de https://www.python.org/downloads/"
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} encontrado${NC}"
echo ""

# 2. Criar ambiente virtual se não existir
echo -e "${YELLOW}[2/5] Configurando ambiente virtual...${NC}"
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    $PYTHON_CMD -m venv venv
    echo -e "${GREEN}✓ Ambiente virtual criado${NC}"
else
    echo -e "${GREEN}✓ Ambiente virtual já existe${NC}"
fi
echo ""

# 3. Ativar ambiente virtual
echo -e "${YELLOW}[3/5] Ativando ambiente virtual...${NC}"
if [[ "$OS_TYPE" == "Windows" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo -e "${GREEN}✓ Ambiente virtual ativado${NC}"
echo ""

# 4. Instalar dependências
echo -e "${YELLOW}[4/5] Instalando dependências...${NC}"
if [ -f "requirements.txt" ]; then
    pip install -q -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Dependências instaladas${NC}"
    else
        echo -e "${RED}✗ Erro ao instalar dependências${NC}"
        exit 1
    fi
else
    echo -e "${RED}✗ requirements.txt não encontrado${NC}"
    exit 1
fi
echo ""

# 5. Iniciar aplicação
echo -e "${YELLOW}[5/5] Iniciando miniERP Pro...${NC}"
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Aplicação iniciando...${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
echo ""

$PYTHON_CMD erp_frontend/main_window.py

# Se a aplicação fechar, mostrar mensagem
echo ""
echo -e "${YELLOW}Aplicação encerrada.${NC}"
