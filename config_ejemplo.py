# 🔧 ARCHIVO DE CONFIGURACIÓN - INSTRUCCIONES DETALLADAS
# =======================================================
# 
# Analizador de Celdas Solares
# Creado por: Adriana Razo De León
#
# Este archivo te permite configurar fácilmente tus datos de medición
# sin necesidad de modificar el código principal.
#
# 📝 INSTRUCCIONES:
# 1. Modifica los valores a continuación con tus datos medidos
# 2. Guarda el archivo (Ctrl+S)
# 3. Ejecuta el programa usando run.bat (Windows) o ./run.sh (Linux/macOS)
#
# ⚠️ IMPORTANTE:
# - Los voltajes deben estar en Volt (V)
# - Las corrientes deben estar en Ampere (A)
# - Debe haber el mismo número de voltajes y corrientes
# - Los voltajes deben estar en orden ascendente
#
# 💡 CONSEJOS:
# - Para mayor precisión, usa más puntos de medición (mínimo 5)
# - Los datos deben cubrir desde V=0 hasta corriente cercana a 0
# - Para condiciones estándar usa irradiancia = 1000 W/m²

# =====================================================
# 📊 TUS DATOS DE MEDICIÓN
# =====================================================

# Voltajes medidos (en Volt) - ¡MODIFICA ESTOS VALORES!
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

# Corrientes medidas (en Ampere) - ¡MODIFICA ESTOS VALORES!
corrientes = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]

# =====================================================
# ⚙️ CONDICIONES DE MEDICIÓN (Opcional)
# =====================================================

# Irradiancia solar durante la medición (W/m²)
# Valores típicos: 1000 (STC), 800 (día nublado), 500 (interior)
irradiancia = 1000

# Área activa de la celda solar (m²)
# Ejemplos: 0.01 = 1 cm², 0.0025 = 0.25 cm², 0.04 = 4 cm²
area_celda = 0.01

# =====================================================
# 🎨 CONFIGURACIÓN DE GRÁFICAS
# =====================================================

# Título que aparecerá en las gráficas
titulo_grafica = "Análisis de Celda Solar"

# Mostrar la eficiencia en la gráfica I-V (True/False)
mostrar_eficiencia = True

# Guardar las gráficas como archivos PNG (True/False)
guardar_imagen = True

# =====================================================
# 📋 EJEMPLOS DE CONFIGURACIÓN
# =====================================================

# Si quieres probar con datos diferentes, puedes copiar y pegar
# alguno de estos ejemplos (descomenta las líneas quitando el #):

# --- EJEMPLO: Celda de alta eficiencia ---
# voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65]
# corrientes = [0.6, 0.58, 0.55, 0.50, 0.42, 0.30, 0.15, 0.0]
# titulo_grafica = "Celda de Alta Eficiencia"

# --- EJEMPLO: Celda orgánica ---
# voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# corrientes = [0.08, 0.075, 0.07, 0.06, 0.04, 0.02, 0.0]
# titulo_grafica = "Celda Solar Orgánica"

# --- EJEMPLO: Mini celda ---
# voltajes = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25]
# corrientes = [0.12, 0.11, 0.10, 0.08, 0.05, 0.0]
# area_celda = 0.0025  # 0.25 cm²
# titulo_grafica = "Mini Celda Solar"
