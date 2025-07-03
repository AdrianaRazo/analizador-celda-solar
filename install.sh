#!/bin/bash

echo "========================================"
echo "Instalador de Analizador de Celdas Solares"
echo "Creado por: Adriana Razo De León"
echo "========================================"
echo

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no está instalado."
    echo "Para instalar Python3:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  CentOS/RHEL: sudo yum install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

echo "Python3 encontrado!"
echo

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 no está instalado."
    echo "Para instalar pip3:"
    echo "  Ubuntu/Debian: sudo apt install python3-pip"
    echo "  CentOS/RHEL: sudo yum install python3-pip"
    exit 1
fi

echo "Instalando dependencias..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias."
    echo "Verifica tu conexión a internet e intenta de nuevo."
    exit 1
fi

echo
echo "========================================"
echo "Instalación completada exitosamente!"
echo "========================================"
echo
echo "Para ejecutar el programa, ejecuta: ./run.sh"
echo "O desde la terminal: python3 graph_I_V.py"
echo
