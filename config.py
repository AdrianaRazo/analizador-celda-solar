# Configuración de datos para el Analizador de Celdas Solares
# 
# Instrucciones:
# 1. Elige tu método de entrada de datos (modificando 'usar_archivo_csv')
# 2. OPCIÓN A: Usar archivo CSV (recomendado)
#    - Cambia 'usar_archivo_csv = True'
#    - Especifica la ruta del archivo en 'archivo_csv'
# 3. OPCIÓN B: Datos directos en este archivo
#    - Cambia 'usar_archivo_csv = False' 
#    - Modifica los valores de voltajes y corrientes abajo
#
# IMPORTANTE: Los datos deben tener el mismo número de valores para voltaje y corriente

# ==========================================
# CONFIGURACIÓN DE FUENTE DE DATOS
# ==========================================

# ¿Usar archivo CSV para cargar datos?
usar_archivo_csv = True  # Cambiar a True para usar CSV

# Archivo CSV con datos (solo si usar_archivo_csv = True)
# El archivo puede tener formato:
# - Columnas: V,I o Voltage,Current o Voltaje,Corriente 
# - Separadores: coma, punto y coma o tabulación
# - Con o sin encabezados
archivo_csv = "ejemplo2.csv"  # Cambia por la ruta de tu archivo

# ==========================================
# DATOS DIRECTOS (solo si usar_archivo_csv = False)
# ==========================================

# Datos medidos de voltaje (V) - separados por comas
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

# Datos medidos de corriente (A) - separados por comas  
corrientes = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]

# ==========================================
# CONFIGURACIÓN DEL ANÁLISIS
# ==========================================

# Condiciones de medición (opcional para calcular eficiencia)
irradiancia = 1.9  # W/m² (1000 para condiciones estándar STC)
area_celda = 9e-6  # m² (área de la celda solar en metros cuadrados)

# Configuración de las gráficas
titulo_grafica = "Análisis de Celda Solar"
mostrar_eficiencia = True  # True para mostrar eficiencia en la gráfica
guardar_imagen = True      # True para guardar las gráficas como PNG
