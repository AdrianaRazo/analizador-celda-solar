"""
Analizador de Celdas Solares - Análisis de Curvas I-V y P-V
===========================================================

Este programa analiza datos experimentales de corriente y voltaje de celdas solares,
calculando parámetros característicos y generando gráficas de análisis.

Creado por: Adriana Razo De León
Proyecto: Celdas Solares
Versión: 2.0
Fecha: 2025

Funcionalidades:
- Análisis de curvas I-V y P-V
- Cálculo de parámetros característicos (Isc, Voc, Pmax, FF, η)
- Generación de gráficas profesionales
- Exportación de resultados a CSV
- Configuración fácil de datos de entrada

Uso:
    python graph_I_V.py

Dependencias:
    - numpy: Cálculos numéricos
    - matplotlib: Generación de gráficas
    - scipy: Interpolación de datos
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import csv
import config
import os
import pandas as pd
from datetime import datetime

def analiza_celda(voltage, current, irradiancia=None, area=None, 
                 titulo="Análisis de Celda Solar", mostrar_eficiencia=True, 
                 guardar_imagen=True):
    """
    Analiza una celda solar a partir de datos de corriente y voltaje.
    
    Parámetros:
    -----------
    voltage : list o array
        Valores de voltaje medidos (V)
    current : list o array  
        Valores de corriente medidos (A)
    irradiancia : float, opcional
        Irradiancia solar en W/m² (default: None)
    area : float, opcional
        Área de la celda en m² (default: None)
    titulo : str, opcional
        Título para las gráficas (default: "Análisis de Celda Solar")
    mostrar_eficiencia : bool, opcional
        Mostrar eficiencia en la gráfica I-V (default: True)
    guardar_imagen : bool, opcional
        Guardar gráficas como archivo PNG (default: True)
    
    Retorna:
    --------
    dict : Diccionario con todos los parámetros calculados
    """
    # Validación de datos de entrada
    if len(voltage) != len(current):
        raise ValueError("Los arrays de voltaje y corriente deben tener la misma longitud")
    
    if len(voltage) < 3:
        raise ValueError("Se requieren al menos 3 puntos de medición")
    
    # Conversión a arrays de NumPy para cálculos
    V = np.array(voltage, dtype=float)
    I = np.array(current, dtype=float)
    
    print("=" * 50)  # Línea más corta
    print(f"🔋 {titulo}")
    print("=" * 50)  # Línea más corta
    print(f"📊 Analizando {len(V)} puntos de medición...")
    print(f"📅 Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Cálculo de Isc (corriente de cortocircuito)
    # Busca el punto donde V es más cercano a 0

    # Busca el punto donde V es más cercano a 0
    Isc = I[np.argmin(np.abs(V))]
    
    # Cálculo de Voc (voltaje de circuito abierto)
    # Interpola para encontrar el voltaje cuando I = 0
    try:
        f_iv = interpolate.interp1d(I, V, kind='linear', fill_value='extrapolate')
        Voc = float(f_iv(0.0))
    except ValueError:
        # Si la interpolación falla, usa el último punto donde I > 0
        Voc = V[I > 0][-1] if len(V[I > 0]) > 0 else V[-1]
    
    # Cálculo de potencia y punto de máxima potencia
    P = V * I
    idx_max = np.argmax(P)
    Vmp, Imp, Pmp = V[idx_max], I[idx_max], P[idx_max]
    
    # Cálculo del Factor de Llenado (Fill Factor)
    if Isc > 0 and Voc > 0:
        FF = Pmp / (Isc * Voc)
    else:
        FF = 0
        print("⚠️  Advertencia: No se puede calcular FF (Isc o Voc es cero)")
    
    # Cálculo de eficiencia (si se proporcionan irradiancia y área)
    eta = None
    if irradiancia is not None and area is not None and irradiancia > 0 and area > 0:
        Pin = irradiancia * area  # Potencia de entrada
        eta = Pmp / Pin if Pin > 0 else 0

        eta = Pmp / Pin if Pin > 0 else 0
    
    # Mostrar resultados en consola
    print("📋 RESULTADOS DEL ANÁLISIS:")
    print("-" * 40)
    print(f"🔌 Corriente de cortocircuito (Isc): {Isc:.4f} A")
    print(f"⚡ Voltaje de circuito abierto (Voc): {Voc:.4f} V")
    print(f"🔋 Corriente en punto máx. potencia (Imp): {Imp:.4f} A")
    print(f"🔋 Voltaje en punto máx. potencia (Vmp): {Vmp:.4f} V")
    print(f"⚡ Potencia máxima (Pmax): {Pmp:.4f} W")
    print(f"📊 Factor de llenado (FF): {FF*100:.2f} %")
    
    if eta is not None:
        print(f"🌟 Eficiencia (η): {eta*100:.2f} %")
        print(f"   📝 Condiciones: {irradiancia} W/m², área: {area} m²")
    else:
        print("ℹ️  Eficiencia no calculada (falta irradiancia o área)")
    
    print()
    
    # Crear diccionario con resultados
    resultados = {
        'Isc': Isc,
        'Voc': Voc,
        'Imp': Imp,
        'Vmp': Vmp,
        'Pmax': Pmp,
        'FF': FF,
        'Eficiencia': eta,
        'Voltajes': V,
        'Corrientes': I,
        'Potencias': P
    }
    
    # === EXPORTAR RESULTADOS A CSV ===
    print("💾 Exportando resultados a CSV...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_csv = f"resultados_celda_{timestamp}.csv"
    
    try:
        with open(archivo_csv, mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Escribir encabezado con información del análisis
            writer.writerow([f"Análisis de Celda Solar - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])
            
            # Escribir datos experimentales
            writer.writerow(["=== DATOS EXPERIMENTALES ==="])
            writer.writerow(["Voltaje (V)", "Corriente (A)", "Potencia (W)"])
            for v, i, p in zip(V, I, P):
                writer.writerow([f"{v:.4f}", f"{i:.4f}", f"{p:.4f}"])
            
            writer.writerow([])
            
            # Escribir parámetros característicos
            writer.writerow(["=== PARÁMETROS CARACTERÍSTICOS ==="])
            writer.writerow(["Parámetro", "Valor", "Unidad"])
            writer.writerow(["Corriente de cortocircuito (Isc)", f"{Isc:.4f}", "A"])
            writer.writerow(["Voltaje de circuito abierto (Voc)", f"{Voc:.4f}", "V"])
            writer.writerow(["Corriente máx. potencia (Imp)", f"{Imp:.4f}", "A"])
            writer.writerow(["Voltaje máx. potencia (Vmp)", f"{Vmp:.4f}", "V"])
            writer.writerow(["Potencia máxima (Pmax)", f"{Pmp:.4f}", "W"])
            writer.writerow(["Factor de llenado (FF)", f"{FF*100:.2f}", "%"])
            
            if eta is not None:
                writer.writerow(["Eficiencia (η)", f"{eta*100:.2f}", "%"])
                writer.writerow(["Irradiancia", f"{irradiancia}", "W/m²"])
                writer.writerow(["Área de la celda", f"{area}", "m²"])
            
        print(f"✅ Resultados guardados en: {archivo_csv}")
        
    except Exception as e:
        print(f"❌ Error al guardar CSV: {e}")
        archivo_csv = "resultados_celda.csv"  # Fallback al nombre original

        archivo_csv = "resultados_celda.csv"  # Fallback al nombre original
    
    # === GENERAR GRÁFICAS ===
    print("📈 Generando gráficas...")
    
    try:
        # Configurar estilo de matplotlib para gráficas profesionales
        plt.style.use('default')
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 1.2
        plt.rcParams['grid.alpha'] = 0.3
        
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(titulo, fontsize=16, fontweight='bold')

        # === GRÁFICA I-V ===
        ax[0].plot(V, I, '-o', linewidth=2, markersize=6, label='Curva I-V', color='#2E86AB')
        ax[0].plot([Vmp], [Imp], 'ko', markersize=8, label=f'Pmax = {Pmp:.3f} W')
        ax[0].plot([0, Voc], [Isc, 0], 'r--', linewidth=2, alpha=0.7, label='Rectángulo ideal')
        
        # Líneas del punto de máxima potencia
        ax[0].plot([Vmp, Vmp], [0, Imp], 'k--', linewidth=1, alpha=0.5)
        ax[0].plot([0, Vmp], [Imp, Imp], 'k--', linewidth=1, alpha=0.5)
        
        ax[0].set_title("Curva Corriente-Voltaje (I-V)", fontweight='bold')
        ax[0].set_xlabel("Voltaje (V)")
        ax[0].set_ylabel("Corriente (A)")
        ax[0].grid(True, alpha=0.3)
        ax[0].legend(frameon=True, fancybox=True, shadow=True)
        
        # Mostrar eficiencia en la gráfica si está disponible
        if eta is not None and mostrar_eficiencia:
            texto_eficiencia = f"η = {eta*100:.2f}%"
            ax[0].text(0.05 * Voc, 0.9 * Isc, texto_eficiencia, 
                      fontsize=12, fontweight='bold',
                      bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))

        # === GRÁFICA P-V ===
        ax[1].plot(V, P, '-o', linewidth=2, markersize=6, color='#A23B72', label='Curva P-V')
        ax[1].plot(Vmp, Pmp, 'ks', markersize=8, label=f'Pmax = {Pmp:.3f} W')
        
        ax[1].set_title("Curva Potencia-Voltaje (P-V)", fontweight='bold')
        ax[1].set_xlabel("Voltaje (V)")
        ax[1].set_ylabel("Potencia (W)")
        ax[1].grid(True, alpha=0.3)
        ax[1].legend(frameon=True, fancybox=True, shadow=True)

        # Ajustar diseño
        plt.tight_layout()
        
        # Guardar imagen si se solicita
        if guardar_imagen:
            timestamp_img = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_imagen = f"curvas_IV_PV_{timestamp_img}.png"
            plt.savefig(nombre_imagen, dpi=300, bbox_inches='tight')
            print(f"✅ Gráficas guardadas en: {nombre_imagen}")
        
        # Mostrar gráficas
        try:
            plt.savefig(nombre_imagen, dpi=300, bbox_inches='tight')
            plt.show()
        except:
            print("ℹ️  Gráficas guardadas pero no se pueden mostrar (entorno sin interfaz gráfica)")
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
    
    print("\n🎉 Análisis completado exitosamente!")
    return resultados



def cargar_datos_csv(archivo_csv):
    """
    Carga datos de voltaje y corriente desde un archivo CSV.
    
    El archivo CSV puede tener varios formatos:
    1. Dos columnas: Voltaje, Corriente
    2. Columnas con nombres: V, I o Voltage, Current o similar
    3. Separadores: coma, punto y coma, o tabulación
    
    Parámetros:
    -----------
    archivo_csv : str
        Ruta al archivo CSV con los datos
    
    Retorna:
    --------
    tuple : (voltajes, corrientes) como listas
    
    Raises:
    -------
    FileNotFoundError : Si el archivo no existe
    ValueError : Si el formato del archivo no es válido
    """
    if not os.path.exists(archivo_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_csv}")
    
    print(f"📂 Cargando datos desde: {archivo_csv}")
    
    try:
        # Intentar detectar el separador automáticamente
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            sample = file.read(1024)
            file.seek(0)
            
            # Detectar separador más común
            separadores = [',', ';', '\t']
            separador = ','
            max_count = 0
            for sep in separadores:
                count = sample.count(sep)
                if count > max_count:
                    max_count = count
                    separador = sep
        
        # Leer el archivo CSV
        try:
            # Intentar con pandas si está disponible (más robusto)
            df = pd.read_csv(archivo_csv, sep=separador)
            
            # Buscar columnas de voltaje y corriente
            voltage_cols = ['V', 'Voltage', 'Voltaje', 'voltage', 'v', 'voltaje']
            current_cols = ['I', 'Current', 'Corriente', 'current', 'i', 'corriente']
            
            voltage_col = None
            current_col = None
            
            for col in df.columns:
                col_clean = col.strip()
                if col_clean in voltage_cols or 'volt' in col_clean.lower():
                    voltage_col = col
                elif col_clean in current_cols or 'curr' in col_clean.lower() or 'amp' in col_clean.lower():
                    current_col = col
            
            # Si no se encuentran columnas con nombres, usar las primeras dos
            if voltage_col is None or current_col is None:
                if len(df.columns) >= 2:
                    voltage_col = df.columns[0]
                    current_col = df.columns[1]
                    print(f"⚠️  Usando columnas por posición: '{voltage_col}' como voltaje, '{current_col}' como corriente")
                else:
                    raise ValueError("El archivo CSV debe tener al menos 2 columnas")
            
            voltajes = df[voltage_col].dropna().tolist()
            corrientes = df[current_col].dropna().tolist()
            
        except ImportError:
            # Si pandas no está disponible, usar el módulo csv estándar
            voltajes = []
            corrientes = []
            
            with open(archivo_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=separador)
                
                # Leer encabezado si existe
                primera_fila = next(reader, None)
                if primera_fila is None:
                    raise ValueError("El archivo CSV está vacío")
                
                # Verificar si la primera fila son números (sin encabezado)
                try:
                    float(primera_fila[0])
                    float(primera_fila[1])
                    # Es una fila de datos, procesarla
                    voltajes.append(float(primera_fila[0]))
                    corrientes.append(float(primera_fila[1]))
                except (ValueError, IndexError):
                    # Es un encabezado, saltarla
                    pass
                
                # Leer el resto de datos
                for fila in reader:
                    if len(fila) >= 2:
                        try:
                            v = float(fila[0].replace(',', '.'))  # Manejar decimales con coma
                            i = float(fila[1].replace(',', '.'))
                            voltajes.append(v)
                            corrientes.append(i)
                        except ValueError:
                            continue  # Saltar filas con datos inválidos
        
        # Validar datos cargados
        if len(voltajes) == 0 or len(corrientes) == 0:
            raise ValueError("No se pudieron cargar datos válidos del archivo CSV")
        
        if len(voltajes) != len(corrientes):
            min_len = min(len(voltajes), len(corrientes))
            voltajes = voltajes[:min_len]
            corrientes = corrientes[:min_len]
            print(f"⚠️  Ajustando longitud de arrays: {min_len} puntos")
        
        print(f"✅ Datos cargados exitosamente: {len(voltajes)} puntos")
        print(f"   📊 Rango de voltaje: {min(voltajes):.3f} - {max(voltajes):.3f} V")
        print(f"   📊 Rango de corriente: {min(corrientes):.6f} - {max(corrientes):.6f} A")
        
        return voltajes, corrientes
        
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {e}")


def crear_csv_ejemplo():
    """
    Crea un archivo CSV de ejemplo con datos típicos de una celda solar.
    """
    archivo_ejemplo = "datos_ejemplo.csv"
    
    # Datos de ejemplo
    voltajes = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    corrientes = [0.52, 0.51, 0.50, 0.48, 0.45, 0.41, 0.35, 0.27, 0.16, 0.08, 0.0]
    
    try:
        with open(archivo_ejemplo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Voltaje (V)', 'Corriente (A)'])
            for v, i in zip(voltajes, corrientes):
                writer.writerow([v, i])
        
        print(f"✅ Archivo de ejemplo creado: {archivo_ejemplo}")
        return archivo_ejemplo
        
    except Exception as e:
        print(f"❌ Error al crear archivo de ejemplo: {e}")
        return None


def cargar_configuracion():
    """
    Carga la configuración desde el archivo config.py
    
    Retorna:
    --------
    dict : Diccionario con la configuración cargada
    """
    try:
        # Importar configuración
        
        # Verificar si se debe usar archivo CSV
        usar_csv = getattr(config, 'usar_archivo_csv', False)
        
        # Inicializar datos de voltaje y corriente
        voltajes = []
        corrientes = []
        fuente_datos = ""
        
        if usar_csv:
            # === CARGAR DATOS DESDE ARCHIVO CSV ===
            archivo_csv = getattr(config, 'archivo_csv', 'datos_medidos.csv')
            
            try:
                # Verificar si el archivo existe
                if not os.path.exists(archivo_csv):
                    print(f"⚠️  No se encontró el archivo: {archivo_csv}")
                    print("💡 ¿Deseas crear un archivo CSV de ejemplo? (s/n): ", end="")
                    respuesta = input().lower().strip()
                    
                    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                        crear_csv_ejemplo()
                        print(f"✅ Archivo de ejemplo creado: datos_ejemplo.csv")
                        print("📝 Puedes usar este archivo como plantilla o cambiar la ruta en config.py")
                        archivo_csv = "datos_ejemplo.csv"
                    else:
                        print("❌ No se puede continuar sin datos. Verificar config.py")
                        return None
                
                # Cargar datos desde CSV
                voltajes, corrientes = cargar_datos_csv(archivo_csv)
                fuente_datos = f"Archivo CSV: {archivo_csv}"
                
            except Exception as e:
                print(f"❌ Error al cargar archivo CSV: {e}")
                print("💡 Revisa que el archivo exista y tenga el formato correcto")
                print("📖 Consulta el README.md para más información sobre formatos CSV")
                print("🔄 Cambiando a datos directos de config.py...")
                usar_csv = False
        
        if not usar_csv:
            # === USAR DATOS DIRECTOS DE CONFIG.PY ===
            voltajes = getattr(config, 'voltajes', [])
            corrientes = getattr(config, 'corrientes', [])
            fuente_datos = "Datos directos (config.py)"
        
        configuracion = {
            'voltajes': voltajes,
            'corrientes': corrientes,
            'irradiancia': getattr(config, 'irradiancia', None),
            'area_celda': getattr(config, 'area_celda', None),
            'titulo_grafica': getattr(config, 'titulo_grafica', "Análisis de Celda Solar"),
            'mostrar_eficiencia': getattr(config, 'mostrar_eficiencia', True),
            'guardar_imagen': getattr(config, 'guardar_imagen', True),
            'fuente_datos': fuente_datos,
            'usar_csv': usar_csv
        }
        
        # Validar datos
        if len(voltajes) != len(corrientes):
            print(f"❌ Error: Número diferente de valores de voltaje ({len(voltajes)}) y corriente ({len(corrientes)})")
            return None
        
        if len(voltajes) < 3:
            print("❌ Error: Se necesitan al menos 3 puntos de datos para el análisis")
            return None
        
        print(f"✅ Configuración cargada: {fuente_datos}")
        print(f"📊 Puntos de datos: {len(voltajes)}")
        print(f"📈 Rango de voltaje: {min(voltajes):.3f} - {max(voltajes):.3f} V")
        print(f"📈 Rango de corriente: {min(corrientes):.6f} - {max(corrientes):.6f} A")
        
        return configuracion
        
    except ImportError:
        print("⚠️  No se encontró config.py, usando datos por defecto")
        return None
    except Exception as e:
        print(f"❌ Error al cargar configuración: {e}")
        return None


def main():
    """
    Función principal del programa
    """
    print("🔋" + "="*58 + "🔋")
    print("   ANALIZADOR DE CELDAS SOLARES - ADRIANA RAZO DE LEÓN")
    print("🔋" + "="*58 + "🔋")
    print()
    
    # Intentar cargar configuración desde archivo
    config_data = cargar_configuracion()
    
    if config_data and config_data['voltajes'] and config_data['corrientes']:
        # Usar datos del archivo de configuración o CSV
        fuente = config_data.get('fuente_datos', 'configuración')
        print(f"📂 Usando datos de: {fuente}")
        
        resultados = analiza_celda(
            voltage=config_data['voltajes'],
            current=config_data['corrientes'],
            irradiancia=config_data['irradiancia'],
            area=config_data['area_celda'],
            titulo=config_data['titulo_grafica'],
            mostrar_eficiencia=config_data['mostrar_eficiencia'],
            guardar_imagen=config_data['guardar_imagen']
        )
        
    else:
        # Usar datos por defecto (datos de ejemplo)
        print("📊 Usando datos de ejemplo")
        print("💡 Para usar tus propios datos, modifica el archivo config.py")
        print()
        
        # Datos de ejemplo (celda solar típica)
        V_ejemplo = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
        I_ejemplo = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]
        
        resultados = analiza_celda(
            voltage=V_ejemplo,
            current=I_ejemplo,
            irradiancia=1000,  # Condiciones estándar STC
            area=0.01,         # 1 cm²
            titulo="Análisis de Celda Solar (Datos de Ejemplo)"
        )
    
    # Mostrar información adicional
    print("\n📝 INFORMACIÓN ADICIONAL:")
    print("-" * 40)
    print("• Para usar datos CSV: cambiar 'usar_archivo_csv = True' en config.py")
    print("• Para datos directos: modificar arrays en config.py")
    print("• Los resultados se guardan automáticamente en formato CSV")
    print("• Las gráficas se guardan como archivos PNG")
    print("• Consulta el README.md para más información")
    
    return resultados


if __name__ == "__main__":
    # Ejecutar programa principal
    try:
        resultados = main()
        print("\n✨ ¡Programa ejecutado exitosamente! ✨")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Programa interrumpido por el usuario")
        
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("📞 Si el problema persiste, consulta la documentación o contacta soporte")
        
    finally:
        input("\n🔚 Presiona Enter para salir...")
