@echo off
echo ========================================
echo Analizador de Celdas Solares
echo Creado por: Adriana Razo De Leon
echo Ejecutando desde Windows...
echo ========================================
echo.

REM Verificar si PowerShell está disponible para usar script avanzado
where powershell >nul 2>&1
if %errorlevel% equ 0 (
    echo Usando ejecutor avanzado de PowerShell...
    powershell -ExecutionPolicy Bypass -File "run.ps1"
    if %errorlevel% equ 0 goto END
    echo.
    echo El ejecutor avanzado falló, continuando con ejecución básica...
    echo.
)

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no encontrado.
    echo.
    echo SOLUCIONES:
    echo 1. Ejecuta primero: install.bat
    echo 2. O instala Python desde Microsoft Store
    echo 3. O descarga desde: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Verificar dependencias básicas
python -c "import numpy, matplotlib, scipy" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Dependencias no instaladas.
    echo.
    echo SOLUCION: Ejecuta install.bat primero
    echo.
    pause
    exit /b 1
)

REM Verificar archivo de configuración
if not exist "config.py" (
    echo Archivo config.py no encontrado.
    if exist "config_ejemplo.py" (
        echo Creando config.py desde plantilla...
        copy "config_ejemplo.py" "config.py" >nul
        echo.
        echo IMPORTANTE: Edita config.py con tus datos antes de continuar
        echo.
        set /p choice="¿Quieres abrir config.py para editarlo? (S/N): "
        if /i "%choice%"=="S" (
            where code >nul 2>&1
            if %errorlevel% equ 0 (
                code config.py
            ) else (
                notepad config.py
            )
            pause
        )
        if /i "%choice%"=="Y" (
            where code >nul 2>&1
            if %errorlevel% equ 0 (
                code config.py
            ) else (
                notepad config.py
            )
            pause
        )
    ) else (
        echo ERROR: No se encontro config_ejemplo.py
        echo Verifica que estes en la carpeta correcta del proyecto
        pause
        exit /b 1
    )
)

echo Ejecutando Analizador de Celdas Solares...
echo.

REM Configurar backend de matplotlib
set MPLBACKEND=Agg

python graph_I_V.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Error durante la ejecución.
    echo.
    echo SOLUCIONES SUGERIDAS:
    echo 1. Verifica que config.py tenga datos válidos
    echo 2. Ejecuta install.bat para reinstalar dependencias
    echo 3. Consulta README.md para más información
    echo.
) else (
    echo.
    echo ¡Análisis completado exitosamente!
    echo.
    echo ARCHIVOS GENERADOS:
    echo - resultados_celda_*.csv (datos y parámetros)
    echo - curvas_IV_PV_*.png (gráficas)
    echo.
    set /p choice="¿Quieres abrir la carpeta de resultados? (S/N): "
    if /i "%choice%"=="S" explorer .
    if /i "%choice%"=="Y" explorer .
)

:END
echo.
pause
