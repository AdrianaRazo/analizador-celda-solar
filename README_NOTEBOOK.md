# 🔋 Analizador de Celdas Solares - Versión 2.0

**Análisis profesional de curvas I-V y P-V para celdas solares**

---

## 🚀 ¡Nuevo! Versión Notebook Interactivo

### 📱 Para principiantes (¡Sin programación requerida!)

**🎯 Opción más fácil**: Usa el **Jupyter Notebook interactivo**

1. **Abrir el notebook**:
   - 📱 **Google Colab** (recomendado): Sube el archivo `Analizador_Celdas_Solares.ipynb` a [colab.research.google.com](https://colab.research.google.com)
   - 💻 **VS Code**: Abre el archivo `Analizador_Celdas_Solares.ipynb` en VS Code
   - 📓 **Jupyter Notebook**: Abre el archivo en Jupyter Notebook

2. **Ejecutar el análisis**:
   - Haz clic en "Run All" o "Ejecutar todo"
   - Sigue las instrucciones paso a paso
   - ¡No necesitas instalar nada!

3. **Cargar tus datos**:
   - **Opción A**: Usar datos de ejemplo (para probar)
   - **Opción B**: Subir archivo CSV desde Excel/Google Sheets
   - **Opción C**: Escribir datos directamente en el notebook

---

### 🔧 Para desarrolladores (Opciones avanzadas)

#### 🖥️ Instalación y ejecución tradicional:

**Windows:**
```bash
# Instalación automática
install.bat

# Ejecutar análisis
run.bat
```

**Linux/Mac:**
```bash
# Instalación automática
./install.sh

# Ejecutar análisis
./run.sh
```

**Python directo:**
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar análisis
python graph_I_V.py
```

---

## 📊 Características principales

### ✅ Lo que hace este analizador:

- **📈 Análisis completo**: Calcula todos los parámetros característicos de celdas solares
- **🎨 Gráficas profesionales**: Genera curvas I-V y P-V de alta calidad
- **📄 Exportación**: Guarda resultados en CSV y gráficas en PNG
- **🔢 Cálculos precisos**: Isc, Voc, Pmax, FF, eficiencia, y más
- **🌐 Multiplataforma**: Funciona en Windows, Linux, Mac, y navegadores web

### 📋 Parámetros calculados:

| Parámetro | Descripción |
|-----------|-------------|
| **Isc** | Corriente de cortocircuito |
| **Voc** | Voltaje de circuito abierto |
| **Imp, Vmp** | Corriente y voltaje de máxima potencia |
| **Pmax** | Potencia máxima |
| **FF** | Factor de llenado (Fill Factor) |
| **η** | Eficiencia de conversión |

---

## 📁 Estructura del proyecto

```
📂 NanoTechProjects/graph/
├── 📓 Analizador_Celdas_Solares.ipynb  # ← ¡NOTEBOOK PRINCIPAL!
├── 📄 README.md                        # ← Estás aquí
├── 🐍 graph_I_V.py                     # Script principal (desarrolladores)
├── ⚙️ config.py                        # Configuración (desarrolladores)
├── 📊 datos_ejemplo.csv                # Datos de ejemplo
├── 📊 ejemplo2.csv                     # Más datos de ejemplo
├── 📦 requirements.txt                 # Dependencias Python
├── 🔧 install.bat / install.sh         # Scripts de instalación
├── ▶️ run.bat / run.sh                 # Scripts de ejecución
└── 📚 docs/                           # Documentación adicional
```

---

## 🎯 Guía de uso rápido

### 🔰 Para principiantes:

1. **Descarga** el archivo `Analizador_Celdas_Solares.ipynb`
2. **Abre** en Google Colab, VS Code, o Jupyter Notebook
3. **Ejecuta** todas las celdas (Run All)
4. **Sigue** las instrucciones paso a paso
5. **¡Disfruta** los resultados!

### 🔧 Para desarrolladores:

1. **Clona** el repositorio
2. **Ejecuta** el script de instalación según tu OS
3. **Configura** tus datos en `config.py`
4. **Ejecuta** el script de análisis
5. **Personaliza** según tus necesidades

---

## 📝 Formatos de datos soportados

### 📊 Archivo CSV:
```csv
Voltaje,Corriente
0.0,0.500
0.1,0.480
0.2,0.450
0.3,0.400
0.4,0.300
0.5,0.000
```

### 📋 Configuración directa (config.py):
```python
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
corrientes = [0.500, 0.480, 0.450, 0.400, 0.300, 0.000]
```

---

## 🛠️ Dependencias

```
numpy>=1.20.0
matplotlib>=3.3.0
scipy>=1.7.0
pandas>=1.3.0
```

**Nota**: En Google Colab se instalan automáticamente.

---

## 🌟 Ejemplos de uso

### 📱 Google Colab:
1. Ve a [colab.research.google.com](https://colab.research.google.com)
2. Sube el archivo `Analizador_Celdas_Solares.ipynb`
3. Ejecuta todas las celdas
4. Sube tu archivo CSV cuando se te solicite

### 💻 VS Code:
1. Instala las extensiones Python y Jupyter
2. Abre el archivo `.ipynb`
3. Ejecuta celda por celda o todas a la vez

### 🖥️ Línea de comandos:
```bash
# Configurar datos
nano config.py

# Ejecutar análisis
python graph_I_V.py
```

---

## 🆘 Solución de problemas

### ❌ Problemas comunes:

**"No se encuentran las dependencias"**
- Notebook: Se instalan automáticamente
- Terminal: Ejecuta `pip install -r requirements.txt`

**"Error al cargar archivo CSV"**
- Revisa que el archivo tenga extensión `.csv`
- Verifica que tenga al menos 2 columnas numéricas
- Asegúrate de que use separadores estándar (,;)

**"Las gráficas no se muestran"**
- En notebooks: Deberían aparecer automáticamente
- En terminal: Revisa que tengas interfaz gráfica disponible

---

## 📞 Soporte

### 👥 Contacto:
- **📧 Email**: adrianarazo@outlook.com
- **🐙 GitHub**: [Reportar problemas](https://github.com/tuusuario/repo)
- **💬 Soporte académico**: Contacto directo para preguntas específicas

### 📚 Documentación:
- **📖 Manual completo**: `GUIA_COMPLETA.md`
- **🔧 Docs técnicas**: `TECHNICAL_DOCS.md`
- **📑 Índice**: `INDICE.md`

---

## 🎓 Información del proyecto

**Autora**: Adriana Razo De León  
**Proyecto**: Análisis de Celdas Solares  
**Versión**: 2.0 (Notebook Interactivo)  
**Fecha**: 2025  
**Licencia**: Ver archivo LICENSE

---

## 🌟 ¡Contribuye!

¿Tienes sugerencias o mejoras? ¡Nos encantaría escucharlas!

- 🐛 Reporta bugs
- 💡 Sugiere nuevas características
- 🔧 Contribuye con código
- 📖 Mejora la documentación

---

## 🔋 ¡Gracias por usar el Analizador de Celdas Solares!

¡Esperamos que esta herramienta te sea útil para tus investigaciones y proyectos con energía solar! 🌞

---

*¿Prefieres la versión fácil? → Usa el **Notebook Interactivo** 📓*  
*¿Eres desarrollador? → Usa los **scripts de Python** 🐍*
