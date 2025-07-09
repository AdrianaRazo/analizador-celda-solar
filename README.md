# 🔋 Analizador de Celdas Solares - Versión 2.0 ☀️⚡

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Estable-brightgreen.svg)]()
[![Author](https://img.shields.io/badge/Autor-Adriana%20Razo%20De%20León-purple.svg)]()

---

## 🎯 **¡NUEVO! Versión Notebook Interactivo**

### 📱 **Para principiantes** (¡SIN programación requerida!)

**🌟 Recomendación**: Usa el **Jupyter Notebook interactivo** - ¡Es súper fácil!

<div align="center">

| Plataforma | Enlace | Descripción |
|------------|--------|-------------|
| 📱 **Google Colab** | [▶️ Abrir Notebook](https://drive.google.com/file/d/1_gOVvUh3uiuuAjivgtSkY0d2dJ3RL_3F/view?usp=sharing) | **Más fácil** |
| 💻 **VS Code** | [📓 Abrir archivo .ipynb](Analizador_Celdas_Solares.ipynb) | **Recomendado** - Completo |
| 📓 **Jupyter** | [🔗 Instalar Jupyter](https://jupyter.org/install) | **Clásico** - Navegador web |

</div>

### 🚀 **¿Cómo usar el Notebook?**

1. **📥 Descarga** el archivo `Analizador_Celdas_Solares.ipynb`
2. **🌐 Abre** en Google Colab, VS Code, o Jupyter Notebook
3. **▶️ Ejecuta** todas las celdas (botón "Run All")
4. **📋 Sigue** las instrucciones paso a paso
5. **🎉 ¡Disfruta** los resultados!

**💡 Ventajas del Notebook**:
- ✅ Sin instalación de programas
- ✅ Instrucciones paso a paso
- ✅ Funciona en cualquier dispositivo
- ✅ Perfecto para principiantes

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
- 🔬 **Investigadoras e investigadores** en energías renovables
- 👩‍🏫👨‍🏫 **Profesorado** que enseña sobre celdas solares
- 🏭 **Personal técnico** en laboratorios de fotovoltaicos
- 💼 **Profesionales** del sector solar

---

## �️ **Para desarrolladores** (Instalación tradicional)

### �🚀 Instalación Rápida por Sistema Operativo

**👆 Selecciona tu sistema operativo para instrucciones específicas:**

<div align="center">

| Sistema | Enlace Directo | Descripción |
|---------|---------------|-------------|
| 🪟 | **[Windows 10/11](#-windows-1011)** | Para personas con poca experiencia |
| 🐧 | **[Linux](#-linux-ubuntudebian)** | Ubuntu, Debian, instalación rápida |
| 🍎 | **[macOS](#-macos)** | Mac Intel y Apple Silicon |
| 👩‍💻👨‍💻 | **[Desarrolladoras/es](#-para-desarrolladoras-y-desarrolladores)** | Si ya usas Python |

</div>

> 💡 **¿Primera vez con Python?** → Mejor usa el **[Notebook interactivo](#-nuevo-versión-notebook-interactivo)** ↑  
> 🚀 **¿Quieres lo más rápido?** → Ve a [Desarrolladoras/es](#-para-desarrolladoras-y-desarrolladores)

---

## 🪟 Windows 10/11

### Opción 1: Con VS Code (Recomendado para principiantes)

**📋 Pasos detallados:**

1. **🐍 Instala Python primero**:
   - **Método más fácil**: Ve a Microsoft Store → Busca "Python 3.11" → Haz clic en "Obtener"
   - **Alternativo**: Ve a https://python.org → "Downloads" → Descarga Python → **IMPORTANTE**: Marca la casilla "Add Python to PATH"

2. **📥 Descarga VS Code**: 
   - Ve a https://code.visualstudio.com/
   - Haz clic en "Download for Windows"
   - Instala normalmente

3. **📦 Descarga este proyecto**: 
   - Haz clic en el botón verde "Code" arriba en esta página
   - Selecciona "Download ZIP"
   - Extrae el archivo ZIP en tu escritorio o carpeta de documentos

4. **📂 Abre el proyecto en VS Code**:
   - Abre VS Code
   - Ve al menú: `File` → `Open Folder...`
   - Busca y selecciona la carpeta que acabas de extraer
   - VS Code te preguntará si confías en la carpeta → Haz clic en "Yes, I trust"

5. **🔧 Instala las extensiones**:
   - VS Code te mostrará una notificación sobre extensiones recomendadas
   - Haz clic en "Install" para instalarlas automáticamente
   - Si no aparece, ve a Extensions (Ctrl+Shift+X) e instala "Python"

6. **⚡ Abre la terminal en VS Code**:
   - Ve al menú: `View` → `Terminal`
   - Aparecerá una ventana negra en la parte inferior

7. **🚀 Instala las dependencias**:
   - En la terminal que acabas de abrir, escribe exactamente esto y presiona Enter:
   ```
   .\install.ps1
   ```
   - Si da error, prueba con:
   ```
   install.bat
   ```
   - Espera a que termine de instalar todo (puede tomar unos minutos)

8. **🎉 Ejecuta el programa**:
   - Una vez que termine la instalación, escribe:
   ```
   .\run.ps1
   ```
   - O si prefieres:
   ```
   python graph_I_V.py
   ```

**💡 Método aún más fácil con VS Code:**
- Presiona `Ctrl+Shift+P`
- Escribe "Tasks: Run Task"
- Selecciona "Ejecutar Analizador"

### Opción 2: Método simple (sin VS Code)

**📋 Para quienes prefieren algo más directo:**

1. **🐍 Instala Python**:
   - Ve a Microsoft Store → Busca "Python 3.11" → "Obtener"
   - O desde https://python.org (marca "Add to PATH" durante instalación)

2. **📦 Descarga el proyecto**:
   - Botón "Code" → "Download ZIP" → Extrae en tu escritorio

3. **🖱️ Ejecuta con doble clic**:
   - Busca el archivo `install.bat` en la carpeta extraída
   - Haz doble clic en `install.bat` → Espera a que termine
   - Luego haz doble clic en `run.bat` para ejecutar el programa

### ⚡ Solución rápida si algo no funciona

| Problema | Solución |
|----------|----------|
| "Python no encontrado" | Instala Python desde Microsoft Store |
| "Error de PowerShell" | Usa los archivos `.bat` en lugar de `.ps1` |
| "Módulo no encontrado" | Ejecuta `pip install -r requirements.txt` en la terminal |
| VS Code no detecta Python | Presiona `Ctrl+Shift+P` → "Python: Select Interpreter" |
| La terminal no se abre | Ve a `View` → `Terminal` en VS Code |

**🤝 ¿Necesitas ayuda?** No dudes en preguntar. Este programa está diseñado para ser fácil de usar para todas las personas, sin importar su experiencia con programación.

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
   # Descargar proyecto
   git clone [URL_DEL_REPOSITORIO] && cd graph
   
   # O descargar ZIP y extraer
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

## 👩‍💻👨‍💻 Para Desarrolladoras y Desarrolladores

### Instalación Rápida

```bash
# Clonar repositorio
git clone [URL_DEL_REPOSITORIO]
cd graph

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
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

- 📋 **[ÍNDICE](INDICE.md)** - Navegación por todos los documentos
- 📖 **[Guía Completa](GUIA_COMPLETA.md)** - Documentación detallada con todos los métodos
- 🔧 **[Documentación Técnica](TECHNICAL_DOCS.md)** - Para desarrolladoras y desarrolladores
- 📄 **[Licencia](LICENSE)** - Términos de uso

---

## 🏆 Créditos

**Desarrollado por**: [Adriana Razo De León](mailto:adrianarazo.leon@gmail.com)  
**Proyecto**: Herramientas de análisis para dispositivos fotovoltaicos  
**Versión**: 2.0 (2025)

---

## ⭐ ¿Te Gusta Este Proyecto?

- 🌟 **Dale una estrella** en GitHub
- 🔄 **Compártelo** con colegas investigadoras e investigadores
- 🤝 **Contribuye** con mejoras
- 📢 **Úsalo** en tus publicaciones (cita el proyecto)

---

<div align="center">

**🔋 ¡Analiza tus celdas solares como una persona profesional! ☀️**

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
