# 🔋 Analizador de Celdas Solares con Python ☀️⚡

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Estable-brightgreen.svg)]()
[![Author](https://img.shields.io/badge/Autor-Adriana%20Razo%20De%20León-purple.svg)]()

---

## 📝 Descripción del Proyecto

Este programa profesional analiza datos experimentales de corriente y voltaje de **celdas solares**, generando automáticamente:

- 📊 **Gráficas I-V y P-V** de alta calidad
- 🔢 **Parámetros característicos** (Isc, Voc, Pmax, FF, eficiencia)
- 📄 **Reportes en CSV** con timestamp profesional
- 📈 **Análisis completo** listo para publicaciones

### ✨ ¿Qué hace este programa?

1. **Carga tus datos experimentales** desde archivos CSV o configuración directa
2. **Calcula automáticamente** todos los parámetros importantes de tu celda solar
3. **Genera gráficas profesionales** I-V y P-V con el punto de máxima potencia marcado
4. **Exporta resultados** en formato CSV listo para reportes e investigación
5. **Calcula eficiencia** si proporcionas irradiancia y área de la celda

### 🎯 ¿Para quién es este programa?

- 🎓 **Estudiantes** de ingeniería y física
- 🔬 **Investigadores** en energías renovables
- 👨‍🏫 **Profesores** que enseñan sobre celdas solares
- 🏭 **Técnicos** en laboratorios de fotovoltaicos
- 💼 **Profesionales** del sector solar

---

## 🚀 Instalación Rápida por Sistema Operativo

**👆 Selecciona tu sistema operativo para instrucciones específicas:**

<div align="center">

| Sistema | Enlace Directo | Descripción |
|---------|---------------|-------------|
| 🪟 | **[Windows 10/11](#-windows-1011)** | Para usuarios con poca experiencia |
| 🐧 | **[Linux](#-linux-ubuntudebian)** | Ubuntu, Debian, instalación rápida |
| 🍎 | **[macOS](#-macos)** | Mac Intel y Apple Silicon |
| 👨‍💻 | **[Desarrolladores](#-para-desarrolladores)** | Si ya usas Python |

</div>

> 💡 **¿Primera vez con Python?** → Empieza con [Windows](#-windows-1011) o [Linux](#-linux-ubuntudebian)  
> 🚀 **¿Quieres lo más rápido?** → Ve a [Desarrolladores](#-para-desarrolladores)

---

## 🪟 Windows 10/11

### Opción 1: Con VS Code (Recomendado para principiantes)

1. **📥 Descarga VS Code**: https://code.visualstudio.com/
2. **📦 Descarga este proyecto**: Botón "Code" → "Download ZIP" → Extrae la carpeta
3. **📂 Abre en VS Code**: `File` → `Open Folder...` → Selecciona la carpeta del proyecto
4. **⚡ Abre terminal**: `Ctrl + `` ` (o `View` → `Terminal`)
5. **🔧 Instala dependencias**:
   ```powershell
   # Opción A: PowerShell (recomendado)
   .\install.ps1
   
   # Opción B: Command Prompt
   install.bat
   ```
6. **🚀 Ejecuta el programa**:
   ```powershell
   # Opción 1
   # Desde terminal
   .\run.ps1
   
   # Opción 2
   # usar tareas: Ctrl+Shift+P → "Tasks: Run Task" → "Ejecutar Analizador"
   ```

### Opción 2: Sin VS Code (Más simple)

1. **🐍 Instala Python**: 
   - **Microsoft Store**: Busca "Python 3.11" 
   - **Web oficial**: https://python.org (marca "Add to PATH")
2. **📦 Descarga el proyecto** como ZIP y extráelo
3. **🖱️ Doble clic** en `install.bat` para instalar
4. **🖱️ Doble clic** en `run.bat` para ejecutar

### ⚡ Solución Rápida de Problemas en Windows
- **"Python no encontrado"**: Instala desde Microsoft Store
- **"Error PowerShell"**: Usa los archivos `.bat` en su lugar
- **VS Code no detecta Python**: `Ctrl+Shift+P` → "Python: Select Interpreter"

---

## 🐧 Linux (Ubuntu/Debian)

### Instalación Automática (1 comando)

```bash
# Instalar todo de una vez
sudo apt update && sudo apt install python3 python3-pip git -y
git clone [URL_DEL_REPOSITORIO] && cd graph
./install.sh && ./run.sh
```

### Instalación Paso a Paso

1. **🔧 Instala dependencias del sistema**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```

2. **📦 Descarga el proyecto**:
   ```bash
   # Opción A: Con Git
   git clone [URL_DEL_REPOSITORIO]
   cd graph
   
   # Opción B: Descarga ZIP y extrae
   wget [URL_ZIP] && unzip graph.zip && cd graph
   ```

3. **🚀 Instala y ejecuta**:
   ```bash
   chmod +x install.sh run.sh  # Dar permisos
   ./install.sh                # Instalar dependencias Python
   ./run.sh                    # Ejecutar programa
   ```

### Con VS Code en Linux

```bash
# Instalar VS Code
sudo snap install code --classic

# Abrir proyecto
code .

# Usar terminal integrada: Ctrl + `
./install.sh
./run.sh
```

---

## 🍎 macOS

### Con Homebrew (Recomendado)

1. **🍺 Instala Homebrew** (si no lo tienes):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **🐍 Instala Python**:
   ```bash
   brew install python
   ```

3. **📦 Descarga y ejecuta**:
   ```bash
   # Opción 1
   # Descargar proyecto
   git clone [URL_DEL_REPOSITORIO] && cd graph
   
   # Opción 2
   # descargar ZIP y extraer
   curl -O [URL_ZIP] && unzip graph.zip && cd graph
   
   # Instalar y ejecutar
   chmod +x install.sh run.sh
   ./install.sh
   ./run.sh
   ```

### Sin Homebrew

1. **🐍 Descarga Python**: https://python.org/downloads/
2. **📦 Descarga el proyecto** como ZIP y extrae
3. **🖥️ Abre Terminal** en la carpeta del proyecto
4. **🚀 Ejecuta**:
   ```bash
   chmod +x install.sh run.sh
   ./install.sh
   ./run.sh
   ```

---

## 👨‍💻 Para Desarrolladores

### Instalación Rápida

```bash
# Opción 1
# Clonar repositorio
git clone [URL_DEL_REPOSITORIO]
cd graph

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS

# Opción 2
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python graph_I_V.py
```

### Dependencias

```txt
numpy>=1.20.0
matplotlib>=3.5.0
scipy>=1.7.0
pandas>=1.3.0
```

---

## 📊 Uso del Programa

Una vez instalado, tienes **dos formas** de proporcionar tus datos:

### Método 1: Archivo CSV (Recomendado) 📄

1. **Prepara tu CSV** con dos columnas:
   ```csv
   Voltaje,Corriente
   0.000,0.500
   0.100,0.480
   0.200,0.450
   ```

2. **Configura el programa**:
   - Abre `config.py`
   - Cambia: `usar_archivo_csv = True`
   - Especifica: `archivo_csv = "mi_archivo.csv"`

3. **Ejecuta**: El programa detecta automáticamente el formato

### Método 2: Datos Directos 📝

1. **Edita `config.py`**:
   ```python
   # Asegúrate que esto esté en False
   usar_archivo_csv = False
   
   # Modifica estos arrays con tus datos
   voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
   corrientes = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]
   ```

2. **Ejecuta**: El programa usará estos datos directamente

---

## 🎯 Resultados que Obtienes

| Parámetro | Descripción | Unidad |
|-----------|-------------|---------|
| **Isc** | Corriente de cortocircuito | A |
| **Voc** | Voltaje de circuito abierto | V |
| **Imp** | Corriente en máxima potencia | A |
| **Vmp** | Voltaje en máxima potencia | V |
| **Pmax** | Potencia máxima | W |
| **FF** | Factor de llenado | % |
| **η** | Eficiencia | % |

**📁 Archivos generados:**
- `curvas_IV_PV_FECHA.png` - Gráficas profesionales
- `resultados_celda_FECHA.csv` - Reporte completo con datos

---

## 🆘 Solución de Problemas

### Problemas Comunes

| Error | Solución |
|-------|----------|
| `Python no encontrado` | Instala Python y marca "Add to PATH" |
| `pip no reconocido` | Reinstala Python o usa `python -m pip` |
| `No module named...` | Ejecuta `pip install -r requirements.txt` |
| `Permission denied` | Linux/Mac: `chmod +x *.sh` |
| Arrays diferentes | Verifica que voltajes y corrientes tengan igual cantidad de valores |

### Contacto para Soporte

- 🐛 **Reportar bugs**: Crea un issue en GitHub
- 💡 **Sugerir mejoras**: Issue con etiqueta "enhancement"
- 📧 **Contacto directo**: adrianarazo.leon@gmail.com

---

## 📚 Documentación Completa

- � **[ÍNDICE](INDICE.md)** - Navegación por todos los documentos
- �📖 **[Guía Completa](GUIA_COMPLETA.md)** - Documentación detallada con todos los métodos
- 🔧 **[Documentación Técnica](TECHNICAL_DOCS.md)** - Para desarrolladores
- 📄 **[Licencia](LICENSE)** - Términos de uso

---

## 🏆 Créditos

**Desarrollado por**: [Adriana Razo De León](mailto:adrianarazo.leon@gmail.com)  
**Proyecto**: Herramientas de análisis para dispositivos fotovoltaicos  
**Versión**: 2.0 (2025)

---

## ⭐ ¿Te Gusta Este Proyecto?

- 🌟 **Dale una estrella** en GitHub
- 🔄 **Compártelo** con colegas investigadores
- 🤝 **Contribuye** con mejoras
- 📢 **Úsalo** en tus publicaciones (cita el proyecto)

---

<div align="center">

**🔋 ¡Analiza tus celdas solares como un profesional! ☀️**

---

### 🧭 Navegación Rápida

| 📱 Acción | 🔗 Enlace |
|-----------|-----------|
| 🚀 Instalar en Windows | [Windows 10/11](#-windows-1011) |
| 🐧 Instalar en Linux | [Linux](#-linux-ubuntudebian) |
| 🍎 Instalar en Mac | [macOS](#-macos) |
| 📊 Ver cómo usar | [Uso del Programa](#-uso-del-programa) |
| 📚 Documentación completa | [GUIA_COMPLETA.md](GUIA_COMPLETA.md) |
| 📋 Índice de documentos | [INDICE.md](INDICE.md) |
| 🆘 Solución problemas | [Problemas](#-solución-de-problemas) |

[⬆️ Volver al inicio](#-analizador-de-celdas-solares-con-python-️)

</div>
