# ============================================
# INSTALADOR PARA WINDOWS - ANALIZADOR DE CELDAS SOLARES
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
    Write-ColorOutput Cyan "🔋 Instalador de Analizador de Celdas Solares"
    Write-ColorOutput Cyan "   Creado por: Adriana Razo De León"
    Write-ColorOutput Cyan "   Compatible con Windows 10/11 y VS Code"
    Write-ColorOutput Cyan "========================================"
    Write-Output ""
}

function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Install-Python {
    Write-ColorOutput Yellow "🐍 Verificando instalación de Python..."
    
    # Verificar si Python está instalado
    $pythonCmd = $null
    $pythonPaths = @("python", "python3", "py")
    
    foreach ($cmd in $pythonPaths) {
        try {
            $version = & $cmd --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                $pythonCmd = $cmd
                Write-ColorOutput Green "✅ Python encontrado: $version"
                break
            }
        } catch {
            continue
        }
    }
    
    if (-not $pythonCmd) {
        Write-ColorOutput Red "❌ Python no está instalado o no está en PATH"
        Write-Output ""
        Write-ColorOutput Yellow "📥 Opciones de instalación:"
        Write-Output "1. Microsoft Store (Recomendado para Windows 10/11):"
        Write-Output "   - Abre Microsoft Store"
        Write-Output "   - Busca 'Python 3.11' o 'Python 3.12'"
        Write-Output "   - Haz clic en 'Obtener' para instalar"
        Write-Output ""
        Write-Output "2. Sitio web oficial:"
        Write-Output "   - Ve a: https://www.python.org/downloads/"
        Write-Output "   - Descarga Python 3.8 o superior"
        Write-Output "   - ⚠️ IMPORTANTE: Marca 'Add Python to PATH' durante la instalación"
        Write-Output ""
        Write-Output "3. Desde VS Code:"
        Write-Output "   - Abre Command Palette (Ctrl+Shift+P)"
        Write-Output "   - Busca 'Python: Select Interpreter'"
        Write-Output "   - Si no hay intérpretes, VS Code te guiará para instalar"
        Write-Output ""
        
        if (-not $Silent) {
            $choice = Read-Host "¿Quieres abrir la Microsoft Store para instalar Python? (S/N)"
            if ($choice -match "^[SsYy]") {
                Start-Process "ms-windows-store://search?query=python"
            }
        }
        
        Write-ColorOutput Red "❌ Por favor instala Python y ejecuta este script nuevamente"
        exit 1
    }
    
    return $pythonCmd
}

function Install-Dependencies($pythonCmd) {
    Write-ColorOutput Yellow "📦 Instalando dependencias de Python..."
    
    # Verificar si pip está disponible
    try {
        & $pythonCmd -m pip --version | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "pip no disponible"
        }
    } catch {
        Write-ColorOutput Red "❌ pip no está disponible"
        Write-Output "Intenta reinstalar Python asegurándote de incluir pip"
        exit 1
    }
    
    # Actualizar pip
    Write-Output "🔄 Actualizando pip..."
    & $pythonCmd -m pip install --upgrade pip --quiet
    
    # Instalar dependencias
    if (Test-Path "requirements.txt") {
        Write-Output "📥 Instalando desde requirements.txt..."
        & $pythonCmd -m pip install -r requirements.txt --quiet
        
        if ($LASTEXITCODE -eq 0) {
            Write-ColorOutput Green "✅ Dependencias instaladas correctamente"
        } else {
            Write-ColorOutput Red "❌ Error al instalar dependencias"
            Write-Output "Intentando instalación individual..."
            
            # Instalar individualmente si falla
            $packages = @("numpy>=1.20.0", "matplotlib>=3.5.0", "scipy>=1.7.0")
            foreach ($package in $packages) {
                Write-Output "📦 Instalando $package..."
                & $pythonCmd -m pip install $package --quiet
            }
        }
    } else {
        Write-ColorOutput Yellow "⚠️ No se encontró requirements.txt, instalando dependencias básicas..."
        $packages = @("numpy", "matplotlib", "scipy")
        foreach ($package in $packages) {
            Write-Output "📦 Instalando $package..."
            & $pythonCmd -m pip install $package --quiet
        }
    }
}

function Test-Installation($pythonCmd) {
    Write-ColorOutput Yellow "🧪 Verificando instalación..."
    
    $testScript = @"
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')  # Backend sin GUI
    import matplotlib.pyplot as plt
    from scipy import interpolate
    print("✅ Todas las dependencias están disponibles")
    print(f"NumPy: {np.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    exit(0)
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    exit(1)
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    exit(1)
"@
    
    $testScript | & $pythonCmd -
    
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput Green "✅ Instalación verificada correctamente"
        return $true
    } else {
        Write-ColorOutput Red "❌ Error en la verificación"
        return $false
    }
}

function Create-VSCodeConfig($pythonCmd) {
    Write-ColorOutput Yellow "⚙️ Configurando VS Code..."
    
    # Crear carpeta .vscode si no existe
    if (-not (Test-Path ".vscode")) {
        New-Item -ItemType Directory -Path ".vscode" | Out-Null
    }
    
    # Obtener ruta del intérprete de Python
    $pythonPath = (& $pythonCmd -c "import sys; print(sys.executable)").Trim()
    
    # Configuración de VS Code
    $vscodeSettings = @{
        "python.pythonPath" = $pythonPath
        "python.defaultInterpreterPath" = $pythonPath
        "files.associations" = @{
            "*.py" = "python"
        }
        "python.terminal.activateEnvironment" = $true
    } | ConvertTo-Json -Depth 3
    
    $vscodeSettings | Out-File -FilePath ".vscode/settings.json" -Encoding UTF8
    
    # Configuración de tareas
    $tasks = @{
        "version" = "2.0.0"
        "tasks" = @(
            @{
                "label" = "Instalar dependencias"
                "type" = "shell"
                "command" = $pythonCmd
                "args" = @("-m", "pip", "install", "-r", "requirements.txt")
                "group" = "build"
                "problemMatcher" = @()
            },
            @{
                "label" = "Ejecutar Analizador"
                "type" = "shell"
                "command" = $pythonCmd
                "args" = @("graph_I_V.py")
                "group" = @{
                    "kind" = "build"
                    "isDefault" = $true
                }
                "problemMatcher" = @('$pylint')
            },
            @{
                "label" = "Configurar datos"
                "type" = "shell"
                "command" = "code"
                "args" = @("config.py")
                "group" = "build"
            }
        )
    } | ConvertTo-Json -Depth 4
    
    $tasks | Out-File -FilePath ".vscode/tasks.json" -Encoding UTF8
    
    Write-ColorOutput Green "✅ VS Code configurado para el proyecto"
}

# ============================================
# SCRIPT PRINCIPAL
# ============================================

try {
    Write-Header
    
    # Verificar sistema operativo
    if ($IsLinux -or $IsMacOS) {
        Write-ColorOutput Red "❌ Este script es solo para Windows"
        Write-Output "Para Linux/macOS, usa: ./install.sh"
        exit 1
    }
    
    # Verificar VS Code (opcional)
    $vscodeInstalled = $false
    try {
        & code --version | Out-Null
        if ($LASTEXITCODE -eq 0) {
            $vscodeInstalled = $true
            Write-ColorOutput Green "✅ VS Code detectado"
        }
    } catch {
        Write-ColorOutput Yellow "ℹ️ VS Code no detectado (opcional)"
    }
    
    # Instalar Python
    $pythonCmd = Install-Python
    
    # Instalar dependencias
    Install-Dependencies $pythonCmd
    
    # Verificar instalación
    $installOk = Test-Installation $pythonCmd
    
    if (-not $installOk) {
        Write-ColorOutput Red "❌ La instalación no se completó correctamente"
        exit 1
    }
    
    # Configurar VS Code si está disponible
    if ($vscodeInstalled) {
        Create-VSCodeConfig $pythonCmd
    }
    
    # Mensaje final
    Write-Output ""
    Write-ColorOutput Green "🎉 ¡Instalación completada exitosamente!"
    Write-ColorOutput Cyan "========================================="
    Write-Output ""
    Write-ColorOutput Yellow "📋 PRÓXIMOS PASOS:"
    Write-Output "1. Edita 'config.py' con tus datos experimentales"
    Write-Output "2. Ejecuta el programa con una de estas opciones:"
    Write-Output ""
    Write-Output "   🖱️ DESDE VS CODE (Recomendado):"
    Write-Output "   - Abre este proyecto en VS Code"
    Write-Output "   - Presiona Ctrl+Shift+P"
    Write-Output "   - Busca 'Tasks: Run Task'"
    Write-Output "   - Selecciona 'Ejecutar Analizador'"
    Write-Output ""
    Write-Output "   💻 DESDE POWERSHELL:"
    Write-Output "   - .\run.ps1"
    Write-Output ""
    Write-Output "   🔧 DESDE COMMAND PROMPT:"
    Write-Output "   - run.bat"
    Write-Output ""
    Write-Output "   ⌨️ COMANDO DIRECTO:"
    Write-Output "   - $pythonCmd graph_I_V.py"
    Write-Output ""
    
    if (-not $Silent) {
        $openVSCode = Read-Host "¿Quieres abrir el proyecto en VS Code ahora? (S/N)"
        if ($openVSCode -match "^[SsYy]" -and $vscodeInstalled) {
            Write-Output "🚀 Abriendo VS Code..."
            & code .
        }
    }
    
} catch {
    Write-ColorOutput Red "❌ Error durante la instalación: $($_.Exception.Message)"
    Write-Output ""
    Write-Output "💡 SOLUCIONES SUGERIDAS:"
    Write-Output "1. Ejecuta PowerShell como Administrador"
    Write-Output "2. Verifica tu conexión a internet"
    Write-Output "3. Asegúrate de que Python esté instalado correctamente"
    Write-Output "4. Consulta la documentación en README.md"
    exit 1
} finally {
    if (-not $Silent) {
        Write-Output ""
        Read-Host "Presiona Enter para continuar..."
    }
}
