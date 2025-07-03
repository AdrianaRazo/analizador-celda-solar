# 🔋 Analizador de Celdas Solares con Python ☀️⚡

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICEN### Método 3: VS Code Tasks (Avanzado)

Si usas VS Code, puedes aprovechar las tareas configuradas:
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Instalar dependencias"
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Ejecutar Analizador"  
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Configurar datos"

### 📊 Guía detallada para archivos CSV

#### Paso 1: Preparar tu archivo CSV
1. **Crea tu archivo CSV** con tus datos de medición:
   - Dos columnas: voltaje y corriente
   - Puedes usar Excel, LibreOffice, o cualquier editor de texto
   - Guarda como archivo `.csv`

2. **Formatos soportados:**
   ```csv
   # Opción A: Con encabezados (recomendado)
   Voltaje,Corriente
   0.000,0.500
   0.100,0.480
   
   # Opción B: Sin encabezados
   0.000,0.500
   0.100,0.480
   
   # Opción C: Nombres alternativos
   V,I
   0.000,0.500
   0.100,0.480
   ```

#### Paso 2: Configurar el programa
1. **Abre** `config.py`
2. **Cambia** `usar_archivo_csv = True`
3. **Especifica** tu archivo: `archivo_csv = "mi_archivo.csv"`
4. **Opcional**: Ajusta irradiancia y área para calcular eficiencia

#### Paso 3: Ejecutar
- El programa detectará automáticamente el formato de tu CSV
- Si hay problemas, te ofrecerá crear un archivo de ejemplo
- Los resultados se exportan normalmente

**� Consejos:**
- Usa el archivo `datos_ejemplo.csv` como plantilla
- El programa maneja decimales con coma (formato europeo)
- Separa columnas con coma, punto y coma, o tabulación

---

## � Requisitos del Sistema

### Software necesario:
- **Python** ≥ 3.8
- **pip** (incluido con Python)

### Librerías Python (se instalan automáticamente):
- `numpy` ≥ 1.20.0 - Cálculos numéricos
- `matplotlib` ≥ 3.5.0 - Generación de gráficas
- `scipy` ≥ 1.7.0 - Interpolación de datos
- `pandas` ≥ 1.3.0 - Manejo robusto de archivos CSVscode/             # Configuración de VS Code
│   ├── settings.json       # Configuraciones del proyecto
│   ├── tasks.json          # Tareas automatizadas
│   └── extensions.json     # Extensiones recomendadas
├── 🔧 install.bat          # Instalador para Windows (Command Prompt)fig_ejemplo.py     # Plantilla de configuración con ejemplos
├── 📋 requirements.txt      # Dependencias de Python[Status](https://img.shields.io/badge/Status-Estable-brightgreen.svg)]()
[![Author](https://img.shields.io/badge/Autor-Adriana%20Razo%20De%20León-purple.svg)]()

Este proyecto analiza datos experimentales de corriente y voltaje de celdas solares, genera gráficas profesionales I-V y P-V, calcula parámetros característicos como **Isc, Voc, Pmax, FF y eficiencia**, y exporta todos los resultados a archivos CSV.

## 🌟 Características

- ✅ **Análisis completo** de curvas I-V y P-V
- ✅ **Cálculo automático** de parámetros característicos
- ✅ **Gráficas profesionales** con alta resolución
- ✅ **Exportación automática** a CSV con timestamp
- ✅ **Carga de datos desde CSV** - ¡NUEVO! 📊
- ✅ **Configuración fácil** a través de archivo de configuración
- ✅ **Múltiples formatos CSV** soportados (coma, punto y coma, tabulación)
- ✅ **Detección automática** de separadores y columnas
- ✅ **Instalación automatizada** para Windows, Linux y macOS
- ✅ **Documentación completa** y código bien comentado
- ✅ **Manejo de errores** robusto
- ✅ **Interface amigable** para usuarios sin experiencia en Python

## 📊 Resultados que obtienes

El programa calcula y muestra:

| Parámetro | Descripción | Unidad |
|-----------|-------------|---------|
| **Isc** | Corriente de cortocircuito | A |
| **Voc** | Voltaje de circuito abierto | V |
| **Imp** | Corriente en punto de máxima potencia | A |
| **Vmp** | Voltaje en punto de máxima potencia | V |
| **Pmax** | Potencia máxima | W |
| **FF** | Factor de llenado | % |
| **η** | Eficiencia de conversión | % |

---

## 🚀 Instalación Rápida

### Para usuarios SIN experiencia en Python:

#### Windows 🪟 (Windows 10/11 + VS Code)
**Opción 1: Desde VS Code (Recomendado)**
1. **Descarga este proyecto** como ZIP y extráelo
2. **Abre VS Code** y ve a `File > Open Folder...`
3. **Selecciona la carpeta** del proyecto extraído
4. **Abre la terminal integrada** (`Ctrl + `` ` o `View > Terminal`)
5. **Ejecuta en la terminal**:
   ```powershell
   # Para PowerShell (recomendado)
   .\install.ps1
   
   # O para Command Prompt
   install.bat
   ```
6. **Una vez instalado, ejecuta**:
   ```powershell
   # Para PowerShell
   .\run.ps1
   
   # O para Command Prompt  
   run.bat
   
   # O usar tareas de VS Code: Ctrl+Shift+P → "Tasks: Run Task" → "Ejecutar Analizador"
   ```

**Opción 2: Sin VS Code**
1. **Descarga este proyecto** como ZIP y extráelo
2. **Doble clic** en `install.bat` (o `install.ps1` si tienes PowerShell)
3. **Doble clic** en `run.bat` (o `run.ps1`) para ejecutar el programa

**Instalación de Python para Windows 11:**
- **Microsoft Store (Más fácil)**: Busca "Python 3.11" en Microsoft Store
- **Sitio oficial**: https://www.python.org/downloads/ (marca "Add to PATH")
- **Desde VS Code**: `Ctrl+Shift+P` → "Python: Select Interpreter" → seguir guía de instalación

#### Linux/macOS 🐧🍎
1. **Descarga este proyecto** como ZIP y extráelo
2. **Abre terminal** en la carpeta del proyecto
3. **Ejecuta**: `./install.sh`
4. **Ejecuta**: `./run.sh`

### Para usuarios CON experiencia en Python:

```bash
# Clonar repositorio
git clone [URL_DEL_REPOSITORIO]
cd graph

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python graph_I_V.py
```

**Desde VS Code:**
```powershell
# Abrir proyecto en VS Code
code .

# Usar terminal integrada (Ctrl + ` )
python graph_I_V.py

# O usar tareas: Ctrl+Shift+P → "Tasks: Run Task" → "Ejecutar Analizador"
```

---

## 🛠️ Cómo usar el programa

### Método 1: Cargar datos desde archivo CSV (Recomendado) 📊

¡NUEVO! Ahora puedes cargar tus datos experimentales directamente desde archivos CSV:

1. **Configura para usar CSV**:
   - Abre `config.py` en VS Code
   - Cambia: `usar_archivo_csv = True`
   - Especifica tu archivo: `archivo_csv = "mi_archivo.csv"`

2. **Formato del archivo CSV**:
   Tu archivo CSV puede tener varios formatos:
   
   **Opción A - Con encabezados:**
   ```csv
   Voltaje,Corriente
   0.000,0.500
   0.100,0.480
   0.200,0.450
   ```
   
   **Opción B - Sin encabezados:**
   ```csv
   0.000,0.500
   0.100,0.480
   0.200,0.450
   ```
   
   **Opción C - Otros nombres de columnas:**
   ```csv
   V,I
   0.000,0.500
   0.100,0.480
   ```

3. **Separadores soportados**:
   - Coma (`,`) - Recomendado
   - Punto y coma (`;`)
   - Tabulación (`\t`)

4. **Ejecuta el análisis** (igual que antes):
   - **VS Code**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Ejecutar Analizador"
   - **Terminal**: `python graph_I_V.py`

**💡 Ejemplo de archivo CSV:** Se incluye `datos_ejemplo.csv` como plantilla.

### Método 2: Desde VS Code (Datos directos)

1. **Abre el proyecto en VS Code**:
   ```
   File > Open Folder... > Selecciona la carpeta del proyecto
   ```

2. **Configura tus datos**:
   - Abre `config.py` en VS Code
   - Asegúrate que: `usar_archivo_csv = False`
   - Modifica los valores con tus datos experimentales:
   ```python
   # Tus datos medidos
   voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]  # En Voltios
   corrientes = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]  # En Amperios
   
   # Condiciones de medición (opcional)
   irradiancia = 1000  # W/m² (1000 = condiciones estándar)
   area_celda = 0.01   # m² (área de tu celda solar)
   ```

3. **Ejecuta el análisis**:
   - **Opción A**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Ejecutar Analizador"
   - **Opción B**: Terminal integrada (`Ctrl + `` `) → `python graph_I_V.py`
   - **Opción C**: Terminal integrada → `.\run.ps1` (PowerShell)

### Método 3: Archivo de configuración (Tradicional)

1. **Edita el archivo `config.py`** con tus datos:

```python
# Tus datos medidos
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]  # En Voltios
corrientes = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]  # En Amperios

# Condiciones de medición (opcional)
irradiancia = 1000  # W/m² (1000 = condiciones estándar)
area_celda = 0.01   # m² (área de tu celda solar)
```

2. **Ejecuta el programa** usando los archivos `.bat` (Windows) o `.sh` (Linux/macOS)

### Método 2: Modificar código directamente

Si prefieres modificar el código, edita la función `main()` en `graph_I_V.py`.

### Método 3: VS Code Tasks (Avanzado)

Si usas VS Code, puedes aprovechar las tareas configuradas:
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Instalar dependencias"
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Ejecutar Analizador"  
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Configurar datos"

---

## � Requisitos del Sistema

### Software necesario:
- **Python** ≥ 3.8
- **pip** (incluido con Python)

### Librerías Python (se instalan automáticamente):
- `numpy` ≥ 1.20.0 - Cálculos numéricos
- `matplotlib` ≥ 3.5.0 - Generación de gráficas
- `scipy` ≥ 1.7.0 - Interpolación de datos

---

## 🐍 Instalación Manual de Python

### Windows 🪟
1. **Descarga Python** desde: https://www.python.org/downloads/
2. **Durante la instalación**: ✅ Marca "Add Python to PATH"
3. **Verifica instalación**: Abre CMD y ejecuta `python --version`

### Linux (Ubuntu/Debian) 🐧
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Linux (CentOS/RHEL/Fedora) 🐧
```bash
sudo yum install python3 python3-pip
# O para versiones nuevas:
sudo dnf install python3 python3-pip
```

### macOS 🍎
```bash
# Con Homebrew (recomendado)
brew install python3

# O descarga desde python.org
```

---

## 📁 Estructura del Proyecto

```
graph/
├── 📄 graph_I_V.py          # Programa principal
├── ⚙️ config.py             # Archivo de configuración
├── � config_ejemplo.py     # Plantilla de configuración con ejemplos
├── �📋 requirements.txt      # Dependencias de Python
├── 📖 README.md            # Esta documentación
├── 📖 TECHNICAL_DOCS.md    # Documentación técnica
├── 📄 LICENSE              # Licencia MIT
├── � .vscode/             # Configuración de VS Code
│   ├── settings.json       # Configuraciones del proyecto
│   └── tasks.json          # Tareas automatizadas
├── �🔧 install.bat          # Instalador para Windows (Command Prompt)
├── 🔧 install.ps1          # Instalador para Windows (PowerShell)
├── 🔧 install.sh           # Instalador para Linux/macOS  
├── ▶️ run.bat              # Ejecutor para Windows (Command Prompt)
├── ▶️ run.ps1              # Ejecutor para Windows (PowerShell)
├── ▶️ run.sh               # Ejecutor para Linux/macOS
├── 🔧 setup.sh             # Configuración inicial (Linux/macOS)
├── 📊 curvas_IV_PV_*.png   # Gráficas generadas
└── 📈 resultados_*.csv     # Resultados exportados

# Archivos CSV de datos (nuevos):
├── 📊 datos_ejemplo.csv    # Archivo CSV de ejemplo incluido
└── 📊 tus_datos.csv       # Tus archivos CSV personalizados
```

### 📋 Formato de archivos CSV de entrada

El programa soporta múltiples formatos de archivos CSV para cargar datos:

**Formato recomendado (con encabezados):**
```csv
Voltaje,Corriente
0.000,0.500
0.100,0.480
0.200,0.450
0.300,0.400
0.400,0.300
0.500,0.000
```

**Otros formatos soportados:**
- Sin encabezados (primera columna = voltaje, segunda = corriente)
- Nombres alternativos: `V,I` o `Voltage,Current` o `Voltaje,Corriente`
- Separadores: coma (`,`), punto y coma (`;`) o tabulación (`\t`)
- Decimales con coma europea (`0,500`) se convierten automáticamente

**💡 Tip:** El archivo `datos_ejemplo.csv` incluido sirve como plantilla.
```

---

## 📸 Ejemplos de Resultados

### Gráficas generadas:
- **Curva I-V**: Muestra la relación corriente-voltaje
- **Curva P-V**: Muestra la variación de potencia con el voltaje
- **Punto de máxima potencia** claramente marcado
- **Eficiencia** mostrada en la gráfica (si se proporciona)

### Archivo CSV exportado:
- **Datos experimentales** completos con timestamp
- **Parámetros característicos** calculados
- **Condiciones de medición** registradas
- **Formato profesional** listo para reportes

### 📊 Ejemplos de archivos CSV de entrada

El proyecto incluye `datos_ejemplo.csv` que puedes usar como plantilla:

```csv
Voltaje,Corriente
0.000,0.500
0.100,0.480
0.200,0.450
0.300,0.400
0.400,0.300
0.500,0.000
```

**Ejemplos adicionales de formatos soportados:**

1. **Con nombres en inglés:**
```csv
Voltage,Current
0.0,0.52
0.1,0.50
0.2,0.47
```

2. **Sin encabezados:**
```csv
0.0,0.52
0.1,0.50
0.2,0.47
```

3. **Con separador punto y coma:**
```csv
V;I
0,0;0,52
0,1;0,50
0,2;0,47
```

**💡 Consejos para crear tu CSV:**
- Usa Excel: "Guardar como" → "CSV (separado por comas)"
- Usa LibreOffice: "Archivo" → "Guardar como" → formato CSV
- Usa cualquier editor de texto: guarda con extensión `.csv`
- Asegúrate de que la primera columna sea voltaje y la segunda corriente

---

## 🔧 Solución de Problemas

### ❌ "Python no está instalado"
- **Windows**: Reinstala Python desde python.org marcando "Add to PATH"
- **Linux**: `sudo apt install python3 python3-pip`
- **macOS**: `brew install python3`

### ❌ "No module named 'numpy/matplotlib/scipy'"
- Ejecuta: `pip install -r requirements.txt`
- O individualmente: `pip install numpy matplotlib scipy`

### ❌ "Error de permisos" (Linux/macOS)
- Ejecuta: `chmod +x install.sh run.sh`
- O usa: `python3 graph_I_V.py` directamente

### ❌ "Error de permisos PowerShell" (Windows)
- Abre PowerShell como Administrador
- Ejecuta: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- O usa los archivos .bat en su lugar

### ❌ "Los arrays deben tener la misma longitud"
- Verifica que voltajes y corrientes tengan el mismo número de valores
- Revisa el archivo `config.py`

### ❌ Gráficas no se muestran
- En servidores remotos: instala `sudo apt install python3-tk`
- En Docker: configura X11 forwarding
- En VS Code: las gráficas se guardan como PNG automáticamente

### ❌ VS Code no reconoce Python
- `Ctrl+Shift+P` → "Python: Select Interpreter"
- Selecciona la versión de Python instalada
- Si no aparece ninguna, instala Python primero

---

## 🤝 Contribuir al Proyecto

¡Las contribuciones son bienvenidas! 

1. **Fork** este repositorio
2. **Crea una rama** para tu característica (`git checkout -b nueva-caracteristica`)
3. **Commit** tus cambios (`git commit -am 'Agrega nueva característica'`)
4. **Push** a la rama (`git push origin nueva-caracteristica`)
5. **Abre un Pull Request**

---

## 📞 Soporte y Contacto

**Desarrolladora**: Adriana Razo De León

- 🐛 **Reportar bugs**: Abre un issue en GitHub
- 💡 **Sugerir mejoras**: Abre un issue con la etiqueta "enhancement"
- 📧 **Contacto directo**: [adrianarazo.leon@gmail.com]

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

La Licencia MIT es una licencia de software libre y de código abierto, muy permisiva y ampliamente utilizada. Permite a cualquier persona usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del software, siempre que se incluya el aviso de copyright original y la nota de licencia en todas las copias o partes sustanciales del software.

Consulta el archivo `LICENSE` para más detalles.

---

## 🏆 Créditos

**Creado por**: Adriana Razo De León  
**Proyecto**: Desarrollo de herramientas para análisis de dispositivos fotovoltaicos

**Versión**: 2.0  
**Última actualización**: 2025

---

## 🔗 Enlaces Útiles

- [Documentación de Python](https://docs.python.org/3/)
- [Tutorial de Matplotlib](https://matplotlib.org/stable/tutorials/index.html)
- [Guía de NumPy](https://numpy.org/doc/stable/user/quickstart.html)
- [Información sobre Celdas Solares](https://www.energy.gov/eere/solar)

---

⭐ **¿Te gusta este proyecto?** ¡Dale una estrella en GitHub!

📢 **¿Lo encontraste útil?** ¡Compártelo con colegas e investigadores!

---

## 💻 Guía Específica para VS Code en Windows 11

### Instalación Inicial
1. **Instala VS Code** desde: https://code.visualstudio.com/
2. **Descarga este proyecto** y extráelo
3. **Abre VS Code** → `File` → `Open Folder...` → Selecciona la carpeta del proyecto
4. **Instala extensiones recomendadas**: VS Code te preguntará automáticamente
5. **Abre terminal integrada**: `Ctrl + `` ` o `View > Terminal`

### Primera Configuración
```powershell
# En la terminal de VS Code, ejecuta:
.\install.ps1

# Si tienes problemas con PowerShell, usa:
install.bat
```

### Uso Diario en VS Code
1. **Configurar datos**: Abre `config.py` y modifica los valores
2. **Ejecutar análisis**: 
   - **Método 1**: `Ctrl+Shift+P` → "Tasks: Run Task" → "Ejecutar Analizador"
   - **Método 2**: Terminal → `python graph_I_V.py`
   - **Método 3**: Terminal → `.\run.ps1`

### Tareas Disponibles en VS Code
- `Ctrl+Shift+P` → "Tasks: Run Task":
  - **"Ejecutar Analizador"**: Corre el análisis principal
  - **"Instalar dependencias"**: Reinstala las librerías
  - **"Verificar instalación"**: Comprueba que todo esté bien
  - **"Configurar datos"**: Abre config.py para editar
  - **"Limpiar archivos generados"**: Borra resultados anteriores

### Solución de Problemas en VS Code
- **Python no detectado**: `Ctrl+Shift+P` → "Python: Select Interpreter"
- **Extensiones faltantes**: Ve a Extensions (Ctrl+Shift+X) e instala las recomendadas
- **Terminal no funciona**: Prueba cambiar de PowerShell a Command Prompt en la terminal
