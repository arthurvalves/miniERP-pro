@echo off
REM ============================================================
REM Script para iniciar miniERP Pro localmente (Windows)
REM ============================================================

setlocal enabledelayedexpansion
chcp 65001 > nul

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║        miniERP Pro - Inicializador de Aplicação       ║
echo ║              Sistema Windows 10/11                     ║
echo ╚════════════════════════════════════════════════════════╝
echo.

REM 1. Verificar Python
echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo X Python não encontrado!
    echo.
    echo Por favor, instale Python 3.8+ de:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% encontrado
echo.

REM 2. Criar ambiente virtual se não existir
echo [2/5] Configurando ambiente virtual...
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
    echo [OK] Ambiente virtual criado
) else (
    echo [OK] Ambiente virtual já existe
)
echo.

REM 3. Ativar ambiente virtual
echo [3/5] Ativando ambiente virtual...
call venv\Scripts\activate.bat
echo [OK] Ambiente virtual ativado
echo.

REM 4. Instalar dependências
echo [4/5] Instalando dependências...
if exist "requirements.txt" (
    pip install -q -r requirements.txt
    if errorlevel 1 (
        echo.
        echo X Erro ao instalar dependências
        echo.
        pause
        exit /b 1
    )
    echo [OK] Dependências instaladas
) else (
    echo.
    echo X requirements.txt não encontrado
    echo.
    pause
    exit /b 1
)
echo.

REM 5. Iniciar aplicação
echo [5/5] Iniciando miniERP Pro...
echo.
echo ════════════════════════════════════════════════════════
echo [OK] Aplicação iniciando...
echo ════════════════════════════════════════════════════════
echo.

python erp_frontend/main_window.py

REM Se a aplicação fechar, mostrar mensagem
echo.
echo Aplicação encerrada.
echo.
pause
