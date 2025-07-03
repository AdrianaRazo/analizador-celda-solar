@echo off
echo ========================================
echo Instalador de Analizador de Celdas Solares
echo Creado por: Adriana Razo De Leon
echo Compatible con Windows 10/11 y VS Code
echo ========================================
echo.

REM Verificar si PowerShell está disponible para usar script avanzado
where powershell >nul 2>&1
if %errorlevel% equ 0 (
    echo Detectado PowerShell - Usando instalador avanzado...
    echo.
    powershell -ExecutionPolicy Bypass -File "install.ps1"
    if %errorlevel% neq 0 (
        echo.
        echo El instalador avanzado falló, continuando con instalación básica...
        echo.
        goto BASIC_INSTALL
    ) else (
        goto END
    )
)

:BASIC_INSTALL
echo Usando instalación básica...
echo.

echo Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no esta instalado.
    echo.
    echo OPCIONES DE INSTALACION:
    echo 1. Microsoft Store ^(Recomendado para Windows 10/11^):
    echo    - Abre Microsoft Store
    echo    - Busca "Python 3.11" o "Python 3.12"
    echo    - Haz clic en "Obtener"
    echo.
    echo 2. Sitio web oficial:
    echo    - Ve a: https://www.python.org/downloads/
    echo    - Descarga Python 3.8 o superior
    echo    - IMPORTANTE: Marca "Add Python to PATH" durante la instalacion
    echo.
    echo 3. Desde VS Code:
    echo    - Abre Command Palette ^(Ctrl+Shift+P^)
    echo    - Busca "Python: Select Interpreter"
    echo    - Si no hay interpretes, VS Code te guiara para instalar
    echo.
    set /p choice="¿Quieres abrir Microsoft Store para instalar Python? (S/N): "
    if /i "%choice%"=="S" start ms-windows-store://search?query=python
    if /i "%choice%"=="Y" start ms-windows-store://search?query=python
    echo.
    echo Por favor instala Python y ejecuta este script nuevamente.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

echo Instalando dependencias...
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias.
    echo Intentando instalacion individual...
    python -m pip install numpy matplotlib scipy --quiet
    if %errorlevel% neq 0 (
        echo ERROR: Fallo la instalacion de dependencias.
        echo Verifica tu conexion a internet e intenta de nuevo.
        pause
        exit /b 1
    )
)

REM Crear configuración básica de VS Code si no existe
if not exist ".vscode" mkdir .vscode
if not exist ".vscode\settings.json" (
    echo Creando configuracion basica de VS Code...
    echo { > .vscode\settings.json
    echo   "files.associations": { >> .vscode\settings.json
    echo     "*.py": "python" >> .vscode\settings.json
    echo   }, >> .vscode\settings.json
    echo   "python.terminal.activateEnvironment": true >> .vscode\settings.json
    echo } >> .vscode\settings.json
)

:END
echo.
echo ========================================
echo Instalacion completada exitosamente!
echo ========================================
echo.
echo PROXIMOS PASOS:
echo 1. Edita 'config.py' con tus datos experimentales
echo 2. Ejecuta el programa:
echo.
echo    DESDE VS CODE ^(Recomendado^):
echo    - Abre este proyecto en VS Code
echo    - Presiona Ctrl+Shift+P
echo    - Busca "Tasks: Run Task"
echo    - Selecciona "Ejecutar Analizador"
echo.
echo    DESDE POWERSHELL:
echo    - .\run.ps1
echo.
echo    DESDE COMMAND PROMPT:
echo    - run.bat
echo.
echo    O directamente: python graph_I_V.py
echo.

REM Verificar si VS Code está instalado
where code >nul 2>&1
if %errorlevel% equ 0 (
    set /p choice="¿Quieres abrir el proyecto en VS Code ahora? (S/N): "
    if /i "%choice%"=="S" code .
    if /i "%choice%"=="Y" code .
)

pause
