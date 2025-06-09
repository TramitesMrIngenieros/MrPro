#!/bin/bash

echo "🚀 Configurando entorno para MRPro+ APK..."
echo "============================================"

# Actualizar sistema
echo "📦 Actualizando sistema..."
sudo apt update

# Instalar dependencias esenciales para compilación APK
echo "🔧 Instalando dependencias..."
sudo apt install -y \
    python3-pip \
    git \
    zip \
    unzip \
    openjdk-11-jdk \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev

# Configurar Java
echo "☕ Configurando Java..."
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
echo 'export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"' >> ~/.bashrc

# Instalar buildozer
echo "🔨 Instalando buildozer..."
pip3 install --user buildozer

# Instalar Cython (requerido para compilación)
echo "🐍 Instalando Cython..."
pip3 install --user Cython

# Configurar PATH
echo "⚙️ Configurando PATH..."
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/.local/bin:$PATH"

# Instalar dependencias Python si existe requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📋 Instalando dependencias Python..."
    pip3 install --user -r requirements.txt
fi

# Crear directorio de trabajo
echo "📁 Preparando directorio de trabajo..."
mkdir -p ~/android_build
cd ~/android_build

# Configurar buildozer para primera ejecución
echo "🔧 Preparando buildozer..."
export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"
echo 'export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"' >> ~/.bashrc

echo ""
echo "============================================"
echo "✅ Configuración completada!"
echo "============================================"
echo ""
echo "🎯 Para compilar APK, ejecuta:"
echo "   buildozer android debug"
echo ""
echo "⏳ La primera compilación tomará 15-20 minutos"
echo "   (descarga Android SDK automáticamente)"
echo ""
echo "🔍 Verificar instalación:"
echo "   java -version"
echo "   buildozer --version"
echo ""

# Recargar bashrc para aplicar cambios
source ~/.bashrc 