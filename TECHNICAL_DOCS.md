# 🔬 Documentación Técnica - Analizador de Celdas Solares

**Creado por**: Adriana Razo De León

## 📐 Algoritmos y Métodos Utilizados

### Cálculo de Parámetros Característicos

#### 1. Corriente de Cortocircuito (Isc)
```python
Isc = I[np.argmin(np.abs(V))]
```
Encuentra el punto donde el voltaje es más cercano a cero.

#### 2. Voltaje de Circuito Abierto (Voc)
```python
f_iv = interpolate.interp1d(I, V, kind='linear', fill_value='extrapolate')
Voc = float(f_iv(0.0))
```
Utiliza interpolación lineal para encontrar el voltaje cuando la corriente es cero.

#### 3. Punto de Máxima Potencia (Pmax)
```python
P = V * I
idx_max = np.argmax(P)
Vmp, Imp, Pmp = V[idx_max], I[idx_max], P[idx_max]
```
Calcula la potencia en cada punto y encuentra el máximo.

#### 4. Factor de Llenado (FF)
```python
FF = Pmp / (Isc * Voc)
```
Relación entre la potencia máxima real y la potencia máxima teórica.

#### 5. Eficiencia (η)
```python
Pin = irradiancia * area
eta = Pmp / Pin
```
Relación entre la potencia eléctrica de salida y la potencia solar de entrada.

## 🏗️ Arquitectura del Código

### Estructura Modular

1. **`analiza_celda()`**: Función principal de análisis
   - Validación de datos
   - Cálculos de parámetros
   - Generación de gráficas
   - Exportación de resultados

2. **`cargar_configuracion()`**: Carga configuración desde archivo
   - Manejo de errores
   - Valores por defecto
   - Validación de parámetros

3. **`main()`**: Función principal del programa
   - Interfaz de usuario
   - Coordinación de funciones
   - Manejo de excepciones

### Manejo de Errores

- **Validación de entrada**: Verificación de longitud y tipo de datos
- **Interpolación segura**: Manejo de casos extremos
- **Archivos**: Gestión de permisos y errores de E/S
- **Gráficas**: Backend alternativo para entornos sin GUI

## 📊 Formatos de Salida

### Archivo CSV
```
Análisis de Celda Solar - [timestamp]

=== DATOS EXPERIMENTALES ===
Voltaje (V), Corriente (A), Potencia (W)
[datos...]

=== PARÁMETROS CARACTERÍSTICOS ===
Parámetro, Valor, Unidad
[parámetros...]
```

### Gráficas PNG
- **Resolución**: 300 DPI
- **Formato**: PNG con transparencia
- **Dimensiones**: 14x6 pulgadas
- **Estilo**: Profesional con grid y leyendas

## 🧪 Testing y Validación

### Casos de Prueba

1. **Datos válidos**: Curva I-V típica
2. **Datos extremos**: Valores muy pequeños/grandes
3. **Datos mínimos**: 3 puntos de medición
4. **Errores comunes**: Arrays de diferente longitud

### Validación Física

- **Isc > 0**: Corriente de cortocircuito positiva
- **Voc > 0**: Voltaje de circuito abierto positivo
- **0 < FF < 1**: Factor de llenado en rango válido
- **η < 50%**: Eficiencia físicamente realista

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
export MPLBACKEND=Agg  # Para entornos sin GUI
export PYTHONPATH=$PYTHONPATH:./  # Para importaciones locales
```

### Matplotlib Backends
- **Agg**: Sin GUI (por defecto)
- **TkAgg**: Con interfaz Tkinter
- **Qt5Agg**: Con interfaz Qt

### Personalización de Gráficas
```python
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
```

## 📈 Extensiones Posibles

### Funcionalidades Adicionales

1. **Análisis de temperatura**: Coeficientes térmicos
2. **Resistencia serie**: Cálculo de Rs y Rsh
3. **Factor de idealidad**: Análisis del diodo
4. **Degradación**: Comparación temporal
5. **Múltiples celdas**: Análisis en lote

### Integración con Otros Tools

- **Jupyter Notebooks**: Para análisis interactivo
- **Pandas**: Para manejo avanzado de datos
- **Plotly**: Para gráficas interactivas
- **REST API**: Para análisis remoto

## 🐛 Debugging y Solución de Problemas

### Logs de Debug
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Problemas Comunes

1. **ImportError**: Dependencias no instaladas
2. **ValueError**: Datos de entrada inválidos
3. **RuntimeError**: Problemas con matplotlib
4. **PermissionError**: Problemas de escritura

### Herramientas de Diagnóstico
```bash
python3 -c "import sys; print(sys.version)"
python3 -c "import numpy; print(numpy.__version__)"
python3 -c "import matplotlib; print(matplotlib.get_backend())"
```

## 📚 Referencias

1. [Green, M. A. (1982). Solar cell fill factor.](https://doi.org/10.1016/0038-1101(82)90203-7)
2. [Sze, S. M. (2007). Physics of Semiconductor Devices](https://www.wiley.com/)
3. [ASTM G173 Standard](https://www.astm.org/Standards/G173.htm)
4. [IEC 61215 Standard](https://webstore.iec.ch/publication/4938)

## 👥 Contribuciones

### Guidelines para Desarrolladores

1. **PEP 8**: Seguir estilo de código Python
2. **Docstrings**: Documentar todas las funciones
3. **Type Hints**: Usar anotaciones de tipo
4. **Tests**: Incluir pruebas unitarias
5. **Comments**: Comentarios en español para usuarios finales

### Estructura de Commits
```
tipo(alcance): descripción

- feat: nueva funcionalidad
- fix: corrección de bug
- docs: documentación
- style: formato/estilo
- refactor: reestructuración
- test: pruebas
```
