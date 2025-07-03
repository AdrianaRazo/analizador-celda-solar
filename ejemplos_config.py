# Ejemplos de configuración para diferentes tipos de celdas solares
# 
# Copia y pega estos datos en config.py para probar diferentes casos

# ========================================
# EJEMPLO 1: Celda de silicio monocristalino
# ========================================
"""
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
corrientes = [0.55, 0.54, 0.52, 0.48, 0.40, 0.28, 0.0]
irradiancia = 1000  # W/m²
area_celda = 0.01   # m² (1 cm²)
titulo_grafica = "Celda de Silicio Monocristalino"
"""

# ========================================
# EJEMPLO 2: Celda de película delgada
# ========================================
"""
voltajes = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
corrientes = [0.12, 0.115, 0.11, 0.10, 0.08, 0.05, 0.0]
irradiancia = 800   # W/m²
area_celda = 0.005  # m² (0.5 cm²)
titulo_grafica = "Celda de Película Delgada (CdTe)"
"""

# ========================================
# EJEMPLO 3: Celda de perovskita experimental
# ========================================
"""
voltajes = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
corrientes = [0.25, 0.24, 0.22, 0.18, 0.12, 0.06, 0.0]
irradiancia = 1000  # W/m²
area_celda = 0.0025 # m² (0.25 cm²)
titulo_grafica = "Celda de Perovskita Experimental"
"""

# ========================================
# EJEMPLO 4: Celda orgánica (OPV)
# ========================================
"""
voltajes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
corrientes = [0.08, 0.075, 0.07, 0.06, 0.045, 0.025, 0.01, 0.0]
irradiancia = 1000  # W/m²
area_celda = 0.01   # m² (1 cm²)
titulo_grafica = "Celda Solar Orgánica (OPV)"
"""

# ========================================
# NOTAS IMPORTANTES:
# ========================================
"""
1. Los voltajes deben estar en orden ascendente
2. Las corrientes generalmente decrecen con el voltaje
3. El número de voltajes debe ser igual al de corrientes
4. Para mayor precisión, usa más puntos de medición
5. La irradiancia típica es 1000 W/m² (condiciones STC)
6. El área debe estar en metros cuadrados (m²)
"""
