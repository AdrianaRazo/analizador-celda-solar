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
    if len(voltage) != len(current):
        raise ValueError("Los arrays de voltaje y corriente deben tener la misma longitud")
    if len(voltage) < 3:
        raise ValueError("Se requieren al menos 3 puntos de medición")
    
    # Convertir a arrays NumPy
    V = np.array(voltage, dtype=float)
    I = np.array(current, dtype=float)
    
    print("=" * 50)
    print(f"🔋 {titulo}")
    print("=" * 50)
    print(f"📊 Analizando {len(V)} puntos de medición...")
    print(f"📅 Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Cálculo de Isc: punto donde V es más cercano a 0
    Isc = I[np.argmin(np.abs(V))]
    
    # Cálculo de Voc: Interpolación para obtener V cuando I = 0.
    try:
        f_iv = interpolate.interp1d(I, V, kind='linear', fill_value="extrapolate")
        Voc = float(f_iv(0.0))
    except ValueError:
        Voc = V[I > 0][-1] if len(V[I > 0]) > 0 else V[-1]
    
    # Cálculo de potencia y puntos de máxima potencia
    P = V * I
    idx_max = np.argmax(P)
    Vmp, Imp, Pmp = V[idx_max], I[idx_max], P[idx_max]
    
    # Calcular Fill Factor
    FF = Pmp / (Isc * Voc) if (Isc > 0 and Voc > 0) else 0
    if FF == 0:
        print("⚠️  Advertencia: No se puede calcular FF (Isc o Voc es cero)")
    
    # Calcular eficiencia si se proporcionan irradiancia y área
    eta = None
    if irradiancia is not None and area is not None and irradiancia > 0 and area > 0:
        Pin = irradiancia * area  # Potencia de entrada
        eta = Pmp / Pin if Pin > 0 else 0
    
    # Mostrar resultados
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
    
    # Exportar resultados a CSV
    print("💾 Exportando resultados a CSV...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_csv = f"resultados_celda_{timestamp}.csv"
    try:
        with open(archivo_csv, mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([f"Análisis de Celda Solar - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])
            writer.writerow(["=== DATOS EXPERIMENTALES ==="])
            writer.writerow(["Voltaje (V)", "Corriente (A)", "Potencia (W)"])
            for v, i_val, p in zip(V, I, P):
                writer.writerow([f"{v:.4f}", f"{i_val:.4f}", f"{p:.4f}"])
            writer.writerow([])
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
        archivo_csv = "resultados_celda.csv"  # Fallback
    
    # Generar gráficas
    print("📈 Generando gráficas...")
    try:
        plt.style.use('default')
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 1.2
        plt.rcParams['grid.alpha'] = 0.3
    
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(titulo, fontsize=16, fontweight='bold')
    
        # Gráfica I-V
        ax[0].plot(V, I, '-o', linewidth=2, markersize=6, label='Curva I-V', color='#2E86AB')
        ax[0].plot([Vmp], [Imp], 'ko', markersize=8, label=f'Pmax = {Pmp:.3f} W')
        ax[0].plot([0, Voc], [Isc, 0], 'r--', linewidth=2, alpha=0.7, label='Rectángulo ideal')
        ax[0].plot([Vmp, Vmp], [0, Imp], 'k--', linewidth=1, alpha=0.5)
        ax[0].plot([0, Vmp], [Imp, Imp], 'k--', linewidth=1, alpha=0.5)
        ax[0].set_title("Curva Corriente-Voltaje (I-V)", fontweight='bold')
        ax[0].set_xlabel("Voltaje (V)")
        ax[0].set_ylabel("Corriente (A)")
        ax[0].grid(True, alpha=0.3)
        ax[0].legend(frameon=True, fancybox=True, shadow=True)
    
        if eta is not None and mostrar_eficiencia:
            ax[0].text(0.05 * Voc, 0.9 * Isc, f"η = {eta*100:.2f}%", fontsize=12,
                       fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))
    
        # Gráfica P-V
        ax[1].plot(V, P, '-o', linewidth=2, markersize=6, color='#A23B72', label='Curva P-V')
        ax[1].plot(Vmp, Pmp, 'ks', markersize=8, label=f'Pmax = {Pmp:.3f} W')
        ax[1].set_title("Curva Potencia-Voltaje (P-V)", fontweight='bold')
        ax[1].set_xlabel("Voltaje (V)")
        ax[1].set_ylabel("Potencia (W)")
        ax[1].grid(True, alpha=0.3)
        ax[1].legend(frameon=True, fancybox=True, shadow=True)
    
        plt.tight_layout()
        
        if guardar_imagen:
            timestamp_img = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_imagen = f"curvas_IV_PV_{timestamp_img}.png"
            plt.savefig(nombre_imagen, dpi=300, bbox_inches='tight')
            print(f"✅ Gráficas guardadas en: {nombre_imagen}")
    
        plt.show()
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
    
    print("\n🎉 Análisis completado exitosamente!")
    return resultados


def cargar_datos_csv(archivo_csv):
    """
    Carga datos de voltaje y corriente desde un archivo CSV.
    
    El archivo CSV puede tener varios formatos:
    1. Dos columnas: Voltaje, Corriente
    2. Columnas con nombres: V, I, Voltage, Current, etc.
    3. Separadores: coma, punto y coma o tabulación
    
    Parámetros:
    -----------
    archivo_csv : str
        Ruta al archivo CSV con los datos
    
    Retorna:
    --------
    tuple : (voltajes, corrientes) como listas
    """
    if not os.path.exists(archivo_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_csv}")
    
    print(f"📂 Cargando datos desde: {archivo_csv}")
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            sample = file.read(1024)
            file.seek(0)
            separadores = [",", ";", "\t"]
            separador = max(separadores, key=lambda sep: sample.count(sep))
        
        try:
            df = pd.read_csv(archivo_csv, sep=separador)
            voltage_cols = ['V', 'Voltage', 'Voltaje', 'voltage', 'v', 'voltaje']
            current_cols = ['I', 'Current', 'Corriente', 'current', 'i', 'corriente']
    
            voltage_col, current_col = None, None
            for col in df.columns:
                col_clean = col.strip()
                if col_clean in voltage_cols or 'volt' in col_clean.lower():
                    voltage_col = col
                elif col_clean in current_cols or 'curr' in col_clean.lower() or 'amp' in col_clean.lower():
                    current_col = col
            
            if voltage_col is None or current_col is None:
                if len(df.columns) >= 2:
                    voltage_col, current_col = df.columns[0], df.columns[1]
                    print(f"⚠️  Usando columnas por posición: '{voltage_col}' como voltaje, '{current_col}' como corriente")
                else:
                    raise ValueError("El archivo CSV debe tener al menos 2 columnas")
    
            voltajes = df[voltage_col].dropna().tolist()
            corrientes = df[current_col].dropna().tolist()
    
        except ImportError:
            voltajes, corrientes = [], []
            with open(archivo_csv, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=separador)
                primera_fila = next(reader, None)
                try:
                    float(primera_fila[0])
                    float(primera_fila[1])
                    voltajes.append(float(primera_fila[0]))
                    corrientes.append(float(primera_fila[1]))
                except (ValueError, IndexError):
                    pass
                for fila in reader:
                    if len(fila) >= 2:
                        try:
                            v = float(fila[0].replace(",", "."))
                            i = float(fila[1].replace(",", "."))
                            voltajes.append(v)
                            corrientes.append(i)
                        except ValueError:
                            continue
        
        if not voltajes or not corrientes:
            raise ValueError("No se pudieron cargar datos válidos del archivo CSV")
        if len(voltajes) != len(corrientes):
            m = min(len(voltajes), len(corrientes))
            voltajes, corrientes = voltajes[:m], corrientes[:m]
            print(f"⚠️  Ajustando longitud de arrays: {m} puntos")
    
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
    Carga la configuración desde el archivo config.py.
    
    Retorna:
    --------
    dict : Diccionario con la configuración cargada
    """
    try:
        usar_csv = getattr(config, 'usar_archivo_csv', False)
        voltajes, corrientes, fuente_datos = [], [], ""
    
        if usar_csv:
            archivo_csv = getattr(config, 'archivo_csv', 'datos_medidos.csv')
            try:
                if not os.path.exists(archivo_csv):
                    print(f"⚠️  No se encontró el archivo: {archivo_csv}")
                    respuesta = input("💡 ¿Deseas crear un archivo CSV de ejemplo? (s/n): ").lower().strip()
                    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                        crear_csv_ejemplo()
                        print("✅ Archivo de ejemplo creado: datos_ejemplo.csv")
                        print("📝 Puedes usar este archivo como plantilla o cambiar la ruta en config.py")
                        archivo_csv = "datos_ejemplo.csv"
                    else:
                        print("❌ No se puede continuar sin datos. Verifica config.py")
                        return None
                voltajes, corrientes = cargar_datos_csv(archivo_csv)
                fuente_datos = f"Archivo CSV: {archivo_csv}"
            except Exception as e:
                print(f"❌ Error al cargar archivo CSV: {e}")
                print("💡 Revisa el archivo y el formato, cambiando a datos directos de config.py...")
                usar_csv = False
    
        if not usar_csv:
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
    Función principal del programa.
    """
    print("🔋" + "="*58 + "🔋")
    print("   ANALIZADOR DE CELDAS SOLARES - ADRIANA RAZO DE LEÓN")
    print("🔋" + "="*58 + "🔋\n")
    
    config_data = cargar_configuracion()
    
    if config_data and config_data['voltajes'] and config_data['corrientes']:
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
        print("📊 Usando datos de ejemplo")
        print("💡 Para usar tus propios datos, modifica el archivo config.py\n")
        V_ejemplo = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
        I_ejemplo = [0.5, 0.48, 0.45, 0.40, 0.30, 0.0]
    
        resultados = analiza_celda(
            voltage=V_ejemplo,
            current=I_ejemplo,
            irradiancia=1000,
            area=0.01,
            titulo="Análisis de Celda Solar (Datos de Ejemplo)"
        )
    
    print("\n📝 INFORMACIÓN ADICIONAL:")
    print("-" * 40)
    print("• Para usar datos CSV: cambia 'usar_archivo_csv = True' en config.py")
    print("• Para datos directos: modifica los arrays en config.py")
    print("• Los resultados se guardan automáticamente en formato CSV")
    print("• Las gráficas se guardan como archivos PNG")
    print("• Consulta el README.md para más información")
    
    return resultados


if __name__ == "__main__":
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
