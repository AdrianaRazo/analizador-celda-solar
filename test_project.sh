#!/bin/bash

# Script para probar el proyecto completo
echo "🧪 PROBANDO PROYECTO COMPLETO"
echo "=============================="
echo

# Probar instalación
echo "📦 Probando instalación..."
if ./install.sh; then
    echo "✅ Instalación exitosa"
else
    echo "❌ Error en instalación"
    exit 1
fi

echo

# Probar ejecución
echo "🚀 Probando ejecución..."
if ./run.sh; then
    echo "✅ Ejecución exitosa"
else
    echo "❌ Error en ejecución"
    exit 1
fi

echo
echo "🎉 ¡Todas las pruebas pasaron!"
echo "📁 Archivos generados:"
ls -la *.csv *.png 2>/dev/null | head -5
echo
echo "✨ El proyecto está listo para GitHub ✨"
