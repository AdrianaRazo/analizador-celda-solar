#!/bin/bash

echo "🔋 CONFIGURACIÓN INICIAL - ANALIZADOR DE CELDAS SOLARES"
echo "Creado por: Adriana Razo De León"
echo "======================================================="
echo

# Verificar si config.py existe
if [ ! -f "config.py" ]; then
    echo "📋 Creando archivo de configuración inicial..."
    cp config_ejemplo.py config.py
    echo "✅ Archivo 'config.py' creado desde plantilla"
    echo
    echo "📝 SIGUIENTE PASO:"
    echo "   1. Edita el archivo 'config.py' con tus datos"
    echo "   2. Ejecuta './run.sh' para analizar tu celda solar"
    echo
else
    echo "✅ Archivo 'config.py' ya existe"
    echo "💡 Puedes editarlo para cambiar los datos de entrada"
    echo
fi

# Verificar dependencias
echo "🔍 Verificando dependencias..."
if python3 -c "import numpy, matplotlib, scipy" 2>/dev/null; then
    echo "✅ Todas las dependencias están instaladas"
else
    echo "⚠️  Faltan dependencias. Ejecutando instalación..."
    ./install.sh
fi

echo
echo "🎯 RESUMEN DE ARCHIVOS:"
echo "======================"
echo "📄 config.py          - Tu configuración de datos"
echo "📖 README.md          - Documentación completa"
echo "▶️  run.sh             - Ejecutar análisis"
echo "🔧 install.sh         - Instalar dependencias"
echo "📊 graph_I_V.py       - Código principal"
echo
echo "🚀 ¡Todo listo! Ejecuta './run.sh' para comenzar"
