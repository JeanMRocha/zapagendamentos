
@echo off
SETLOCAL

echo 📦 Ativando ambiente virtual...
call venv\Scripts\activate.bat

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ ERRO: Falha ao ativar o ambiente virtual.
    GOTO end
)

echo ✅ Ambiente ativado!

echo 🧪 Verificando Python...
where python

echo 🔄 Instalando dependências...
pip install -r app\requirements.txt

echo ⚙️ Inicializando banco de dados...
python app\database\init_db.py

:end
echo 🔚 Script finalizado. Pressione qualquer tecla para sair.
pause >nul
