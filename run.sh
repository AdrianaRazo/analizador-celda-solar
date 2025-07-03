#!/bin/bash

echo "========================================"
echo "Analizador de Celdas Solares"
echo "Creado por: Adriana Razo De León"
echo "========================================"
echo

python3 graph_I_V.py

if [ $? -ne 0 ]; then
    echo
    echo "ERROR: No se pudo ejecutar el programa."
    echo "Asegúrate de haber ejecutado ./install.sh primero."
    echo
fi
