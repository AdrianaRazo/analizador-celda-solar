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
    Calcula parámetros en unidades de mA/cm², mW/cm², etc., como en el notebook.
    Retorna resultados y las figuras de matplotlib.
    """
    if len(voltage) != len(current):
        raise ValueError("Los arrays de voltaje y corriente deben tener la misma longitud")
    if len(voltage) < 3:
        raise ValueError("Se requieren al menos 3 puntos de medición")

    # Convertir a arrays NumPy
    V = np.array(voltage, dtype=float)
    I = np.array(current, dtype=float)

    # --- Cálculo de parámetros al estilo del notebook ---
    # 1. Jsc (Densidad de corriente de cortocircuito): I(V=0)
    try:
        f_v = interpolate.interp1d(V, I, kind='linear', fill_value='extrapolate')
        Jsc = float(f_v(0.0))
    except Exception:
        Jsc = I[np.argmin(np.abs(V))]

    # 2. Voc (Voltaje de circuito abierto): V(I=0)
    try:
        f_i = interpolate.interp1d(I, V, kind='linear', fill_value='extrapolate')
        Voc = float(f_i(0.0))
    except Exception:
        Voc = V[np.argmax(V)]

    # 3. Pmax, Vmp, Imp (usar corriente absoluta para potencia útil)
    I_inver = -I  # Corriente invertida para que P sea positiva
    P = V * I_inver
    idx_max = np.argmax(P)
    Vmp = V[idx_max]
    Imp = I_inver[idx_max]
    Pmax = Vmp * Imp

    # 4. FF (Factor de llenado, %)
    if Jsc != 0 and Voc != 0:
        FF = (abs(Pmax)) / (abs(Jsc) * abs(Voc)) * 100
    else:
        FF = 0

    # 5. PCE relativa (sin área ni irradiancia)
    PCE = abs(Jsc) * abs(Voc) * FF / 100

    # 6. Si hay irradiancia y área, calcular eficiencia absoluta
    eficiencia = None
    if irradiancia and area and irradiancia > 0 and area > 0:
        Pin = irradiancia * area
        eficiencia = Pmax / Pin if Pin > 0 else None
    else:
        eficiencia = PCE  # PCE relativa (%)

    # Mostrar resultados
    print("=" * 50)
    print(f"🔋 {titulo}")
    print("=" * 50)
    print(f"📊 Analizando {len(V)} puntos de medición...")
    print(f"📅 Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("📈 PARÁMETROS PRINCIPALES:")
    print(f"  • Jsc (Densidad de corriente cortocircuito): {Jsc:.4f} mA/cm²")
    print(f"  • Voc (Voltaje circuito abierto): {Voc:.4f} V")
    print(f"  • Imp (Corriente máxima potencia): {Imp:.4f} mA/cm²")
    print(f"  • Vmp (Voltaje máxima potencia): {Vmp:.4f} V")
    print(f"  • Pmax (Potencia máxima): {Pmax:.4f} mW/cm²")
    print(f"  • FF (Factor de llenado): {FF:.2f}%")
    print(f"  • η (Eficiencia/PCE relativa): {eficiencia:.2f}%")
    print()

    resultados = {
        'Jsc': abs(Jsc),
        'Voc': abs(Voc),
        'Imp': abs(Imp),
        'Vmp': abs(Vmp),
        'Pmax': abs(Pmax),
        'FF': FF,
        'Eficiencia': eficiencia,
        'Voltajes': V,
        'DensidadCorriente': I_inver,
        'Potencias': P
    }

    # Exportar resultados a CSV (opcional)
    print("💾 Exportando resultados a CSV...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_csv = f"resultados_celda_{timestamp}.csv"
    try:
        with open(archivo_csv, mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([f"Análisis de Celda Solar - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])
            writer.writerow(["=== DATOS EXPERIMENTALES ==="])
            writer.writerow(["Voltaje (V)", "Corriente (A)", "Potencia (mW/cm²)"])
            for v, i_val, p in zip(V, I, P):
                writer.writerow([f"{v:.4f}", f"{i_val:.4f}", f"{p:.4f}"])
            writer.writerow([])
            writer.writerow(["=== PARÁMETROS CARACTERÍSTICOS ==="])
            writer.writerow(["Parámetro", "Valor", "Unidad"])
            writer.writerow(["Densidad de corriente cortocircuito (Jsc)", f"{Jsc:.4f}", "mA/cm²"])
            writer.writerow(["Voltaje de circuito abierto (Voc)", f"{Voc:.4f}", "V"])
            writer.writerow(["Corriente máx. potencia (Imp)", f"{Imp:.4f}", "mA/cm²"])
            writer.writerow(["Voltaje máx. potencia (Vmp)", f"{Vmp:.4f}", "V"])
            writer.writerow(["Potencia máxima (Pmax)", f"{Pmax:.4f}", "mW/cm²"])
            writer.writerow(["Factor de llenado (FF)", f"{FF:.2f}", "%"])
            writer.writerow(["Eficiencia (η)", f"{eficiencia:.2f}", "%"])
            if irradiancia is not None:
                writer.writerow(["Irradiancia", f"{irradiancia}", "W/m²"])
            if area is not None:
                writer.writerow(["Área de la celda", f"{area}", "m²"])
        print(f"✅ Resultados guardados en: {archivo_csv}")
    except Exception as e:
        print(f"❌ Error al guardar CSV: {e}")
        archivo_csv = "resultados_celda.csv"  # Fallback

    # Generar figuras y retornarlas
    print("📈 Generando gráficas (retornando objetos de figura)...")
    try:
        plt.style.use('default')
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 1.2
        plt.rcParams['grid.alpha'] = 0.3

        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(titulo, fontsize=16, fontweight='bold')

        # Gráfica I-V (Densidad de corriente)
        ax[0].plot(V, I_inver, '-o', linewidth=2, markersize=6, label='Curva I-V', color='#2E86AB')
        ax[0].plot([Vmp], [Imp], 'ko', markersize=8, label=f'Pmax = {Pmax:.3f} mW/cm²')
        ax[0].plot([0, Voc], [Jsc, 0], 'r--', linewidth=2, alpha=0.7, label='Rectángulo ideal')
        ax[0].plot([Vmp, Vmp], [0, Imp], 'k--', linewidth=1, alpha=0.5)
        ax[0].plot([0, Vmp], [Imp, Imp], 'k--', linewidth=1, alpha=0.5)
        ax[0].set_title("Curva Corriente-Voltaje (I-V)", fontweight='bold')
        ax[0].set_xlabel("Voltaje (V)")
        ax[0].set_ylabel("Densidad de corriente (mA/cm²)")
        ax[0].grid(True, alpha=0.3)
        ax[0].legend(frameon=True, fancybox=True, shadow=True)
        ax[0].text(0.05 * Voc, 0.9 * Jsc, f"η = {eficiencia:.2f}%", fontsize=12,
                   fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))

        # Gráfica P-V (Potencia por área)
        ax[1].plot(V, P, '-o', linewidth=2, markersize=6, color='#A23B72', label='Curva P-V')
        ax[1].plot(Vmp, Pmax, 'ks', markersize=8, label=f'Pmax = {Pmax:.3f} mW/cm²')
        ax[1].set_title("Curva Potencia-Voltaje (P-V)", fontweight='bold')
        ax[1].set_xlabel("Voltaje (V)")
        ax[1].set_ylabel("Potencia (mW/cm²)")
        ax[1].grid(True, alpha=0.3)
        ax[1].legend(frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        # No mostrar ni guardar aquí, solo retornar la figura
        print("✅ Figuras generadas y retornadas")
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
        fig = None

    print("\n🎉 Análisis completado exitosamente!")
    return resultados, fig


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
        resultados, _ = analiza_celda(
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
    
        resultados, _ = analiza_celda(
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
    print("• Las gráficas se guardan como archivos PNG")
    print("• Consulta el README.md para más información")


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
    print("• Las gráficas se guardan como archivos PNG")
    print("• Consulta el README.md para más información")
