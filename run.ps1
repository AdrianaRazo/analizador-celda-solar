# ============================================
# EJECUTOR PARA WINDOWS - ANALIZADOR DE CELDAS SOLARES
# ============================================
# Compatible con Windows 10/11, PowerShell y VS Code

param(
    [switch]$Silent = $false
)

function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Header {
    Write-ColorOutput Cyan "========================================"
    Write-ColorOutput Cyan "🔋 Analizador de Celdas Solares"
    Write-ColorOutput Cyan "   Creado por: Adriana Razo De León"
    Write-ColorOutput Cyan "   Ejecutando desde Windows..."
    Write-ColorOutput Cyan "========================================"
    Write-Output ""
}

function Find-PythonCommand {
    $pythonCommands = @("python", "python3", "py")
    
    foreach ($cmd in $pythonCommands) {
        try {
            $version = & $cmd --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-ColorOutput Green "✅ Python encontrado: $version"
                return $cmd
            }
        } catch {
            continue
        }
    }
    
    return $null
}

function Test-Dependencies($pythonCmd) {
    Write-ColorOutput Yellow "🔍 Verificando dependencias..."
    
    $testScript = @"
try:
    import numpy
    import matplotlib
    from scipy import interpolate
    print("✅ Dependencias verificadas")
    exit(0)
except ImportError as e:
    print(f"❌ Dependencia faltante: {e}")
    exit(1)
"@
    
    $testScript | & $pythonCmd -
    return ($LASTEXITCODE -eq 0)
}

function Run-Analyzer($pythonCmd) {
    Write-ColorOutput Yellow "🚀 Ejecutando Analizador de Celdas Solares..."
    Write-Output ""
    
    if (-not (Test-Path "graph_I_V.py")) {
        Write-ColorOutput Red "❌ No se encontró graph_I_V.py"
        Write-Output "Asegúrate de estar en la carpeta correcta del proyecto"
        return $false
    }
    
    # Configurar variables de entorno para matplotlib
    $env:MPLBACKEND = "Agg"
    
    try {
        & $pythonCmd graph_I_V.py
        
        if ($LASTEXITCODE -eq 0) {
            Write-Output ""
            Write-ColorOutput Green "🎉 ¡Análisis completado exitosamente!"
            return $true
        } else {
            Write-ColorOutput Red "❌ Error durante la ejecución (código: $LASTEXITCODE)"
            return $false
        }
    } catch {
        Write-ColorOutput Red "❌ Error al ejecutar: $($_.Exception.Message)"
        return $false
    }
}

function Show-Results {
    Write-Output ""
    Write-ColorOutput Cyan "📊 ARCHIVOS GENERADOS:"
    Write-Output "========================"
    
    # Buscar archivos CSV generados
    $csvFiles = Get-ChildItem -Filter "resultados_celda_*.csv" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
    if ($csvFiles) {
        Write-Output "📈 Archivos CSV (resultados):"
        foreach ($file in $csvFiles) {
            Write-Output "   - $($file.Name) ($($file.LastWriteTime.ToString('yyyy-MM-dd HH:mm')))"
        }
    }
    
    # Buscar archivos PNG generados
    $pngFiles = Get-ChildItem -Filter "curvas_IV_PV_*.png" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
    if ($pngFiles) {
        Write-Output "🖼️ Gráficas PNG:"
        foreach ($file in $pngFiles) {
            Write-Output "   - $($file.Name) ($($file.LastWriteTime.ToString('yyyy-MM-dd HH:mm')))"
        }
    }
    
    Write-Output ""
    Write-ColorOutput Yellow "💡 SUGERENCIAS:"
    Write-Output "• Abre los archivos CSV en Excel para ver los datos"
    Write-Output "• Las gráficas PNG se pueden abrir con cualquier visor de imágenes"
    Write-Output "• Para modificar datos, edita 'config.py' y ejecuta de nuevo"
}

function Open-Results {
    if (-not $Silent) {
        Write-Output ""
        $choice = Read-Host "¿Quieres abrir la carpeta con los resultados? (S/N)"
        if ($choice -match "^[SsYy]") {
            Write-Output "📂 Abriendo carpeta de resultados..."
            Start-Process explorer.exe -ArgumentList (Get-Location).Path
        }
        
        $choice = Read-Host "¿Quieres ver la última gráfica generada? (S/N)"
        if ($choice -match "^[SsYy]") {
            $latestPng = Get-ChildItem -Filter "curvas_IV_PV_*.png" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
            if ($latestPng) {
                Write-Output "🖼️ Abriendo gráfica..."
                Start-Process $latestPng.FullName
            } else {
                Write-ColorOutput Yellow "⚠️ No se encontraron gráficas"
            }
        }
    }
}

# ============================================
# SCRIPT PRINCIPAL
# ============================================

try {
    Write-Header
    
    # Verificar Python
    $pythonCmd = Find-PythonCommand
    if (-not $pythonCmd) {
        Write-ColorOutput Red "❌ Python no encontrado"
        Write-Output ""
        Write-Output "🔧 SOLUCIONES:"
        Write-Output "1. Ejecuta primero: .\install.ps1"
        Write-Output "2. O instala Python desde Microsoft Store"
        Write-Output "3. O descarga desde: https://www.python.org/downloads/"
        Write-Output ""
        exit 1
    }
    
    # Verificar dependencias
    if (-not (Test-Dependencies $pythonCmd)) {
        Write-ColorOutput Red "❌ Dependencias no instaladas"
        Write-Output ""
        Write-Output "🔧 SOLUCIÓN:"
        Write-Output "Ejecuta: .\install.ps1"
        Write-Output ""
        exit 1
    }
    
    # Verificar archivo de configuración
    if (-not (Test-Path "config.py")) {
        Write-ColorOutput Yellow "⚠️ No se encontró config.py"
        
        if (Test-Path "config_ejemplo.py") {
            Write-Output "📋 Creando config.py desde plantilla..."
            Copy-Item "config_ejemplo.py" "config.py"
            Write-ColorOutput Green "✅ config.py creado"
            Write-Output ""
            Write-ColorOutput Yellow "📝 IMPORTANTE: Edita config.py con tus datos antes de continuar"
            
            if (-not $Silent) {
                $choice = Read-Host "¿Quieres abrir config.py para editarlo ahora? (S/N)"
                if ($choice -match "^[SsYy]") {
                    if (Get-Command code -ErrorAction SilentlyContinue) {
                        & code config.py
                        Read-Host "Presiona Enter cuando hayas terminado de editar config.py..."
                    } else {
                        & notepad config.py
                        Read-Host "Presiona Enter cuando hayas terminado de editar config.py..."
                    }
                }
            }
        } else {
            Write-ColorOutput Red "❌ No se encontró config_ejemplo.py"
            Write-Output "Verifica que estés en la carpeta correcta del proyecto"
            exit 1
        }
    }
    
    # Ejecutar análisis
    $success = Run-Analyzer $pythonCmd
    
    if ($success) {
        Show-Results
        Open-Results
        
        Write-Output ""
        Write-ColorOutput Green "✨ ¡Programa ejecutado exitosamente! ✨"
        Write-Output ""
        Write-ColorOutput Cyan "🔄 Para ejecutar de nuevo:"
        Write-Output "• Desde VS Code: Ctrl+Shift+P → 'Tasks: Run Task' → 'Ejecutar Analizador'"
        Write-Output "• Desde PowerShell: .\run.ps1"
        Write-Output "• Comando directo: $pythonCmd graph_I_V.py"
        
    } else {
        Write-ColorOutput Red "❌ Error durante la ejecución"
        Write-Output ""
        Write-Output "🔧 SOLUCIONES SUGERIDAS:"
        Write-Output "1. Verifica que config.py tenga datos válidos"
        Write-Output "2. Ejecuta: .\install.ps1 para reinstalar dependencias"
        Write-Output "3. Consulta README.md para más información"
        Write-Output "4. Verifica que los arrays de voltaje y corriente tengan la misma longitud"
    }
    
} catch {
    Write-ColorOutput Red "❌ Error inesperado: $($_.Exception.Message)"
    Write-Output ""
    Write-Output "💡 Si el problema persiste:"
    Write-Output "1. Consulta README.md"
    Write-Output "2. Verifica la instalación de Python"
    Write-Output "3. Ejecuta .\install.ps1 nuevamente"
    
} finally {
    if (-not $Silent) {
        Write-Output ""
        Read-Host "🔚 Presiona Enter para salir..."
    }
}
