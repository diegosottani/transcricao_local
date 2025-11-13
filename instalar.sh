#!/bin/bash
# 🚀 Script de Instalação Automatizada
# Sistema de Transcrição Local de Vídeos
# Autor: Diego Sottani

set -e  # Parar em caso de erro

echo "╔════════════════════════════════════════════════════════════╗"
echo "║   🎯 Instalação - Sistema de Transcrição Local           ║"
echo "║   Criado por Diego Sottani                                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Função para verificar comando
comando_existe() {
    command -v "$1" >/dev/null 2>&1
}

# Função para mensagens de sucesso
sucesso() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Função para mensagens de aviso
aviso() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Função para mensagens de erro
erro() {
    echo -e "${RED}❌ $1${NC}"
}

echo "📋 Verificando requisitos..."
echo ""

# 1. Verificar Python
echo -n "🐍 Verificando Python... "
if comando_existe python3; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    sucesso "Python $PYTHON_VERSION encontrado"
else
    erro "Python 3 não encontrado!"
    echo "   Instale Python 3.8+ de: https://www.python.org/downloads/"
    exit 1
fi

# 2. Verificar pip
echo -n "📦 Verificando pip... "
if comando_existe pip3; then
    sucesso "pip encontrado"
else
    erro "pip não encontrado!"
    echo "   Instale com: python3 -m ensurepip --upgrade"
    exit 1
fi

# 3. Verificar FFmpeg
echo -n "🎬 Verificando FFmpeg... "
if comando_existe ffmpeg; then
    FFMPEG_VERSION=$(ffmpeg -version 2>&1 | head -n 1 | awk '{print $3}')
    sucesso "FFmpeg $FFMPEG_VERSION encontrado"
else
    aviso "FFmpeg não encontrado!"
    echo ""
    echo "   FFmpeg é necessário para processar vídeos."
    echo "   Instale com:"
    echo ""
    echo "   Ubuntu/Debian: sudo apt install ffmpeg"
    echo "   Mac: brew install ffmpeg"
    echo "   Windows: https://ffmpeg.org/download.html"
    echo ""
    read -p "   Deseja continuar sem FFmpeg? (s/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "📁 Criando estrutura de diretórios..."

# Criar diretórios necessários
mkdir -p exemplos
mkdir -p videos
mkdir -p transcricoes

sucesso "Diretórios criados"

echo ""
echo "🔧 Configurando ambiente virtual..."

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    python3 -m venv venv
    sucesso "Ambiente virtual criado"
else
    aviso "Ambiente virtual já existe"
fi

# Ativar ambiente virtual
source venv/bin/activate || source venv/Scripts/activate 2>/dev/null

sucesso "Ambiente virtual ativado"

echo ""
echo "📥 Instalando dependências Python..."
echo "   (isso pode demorar alguns minutos)"
echo ""

# Atualizar pip
pip install --upgrade pip --quiet

# Instalar dependências
pip install -r requirements.txt

sucesso "Dependências instaladas"

echo ""
echo "🎯 Baixando modelo Whisper base..."
echo "   (primeiro download pode demorar)"
echo ""

# Baixar modelo base (será usado no primeiro run)
python -c "import whisper; whisper.load_model('base')" 2>&1 | grep -v "FutureWarning" || true

sucesso "Modelo base baixado"

echo ""
echo "🧪 Testando instalação..."
echo ""

# Criar arquivo de teste simples
cat > teste_instalacao.py << 'EOF'
import whisper
import sys

try:
    model = whisper.load_model("tiny")
    print("✅ Whisper OK")
    sys.exit(0)
except Exception as e:
    print(f"❌ Erro: {e}")
    sys.exit(1)
EOF

python teste_instalacao.py
TESTE_STATUS=$?
rm teste_instalacao.py

if [ $TESTE_STATUS -eq 0 ]; then
    sucesso "Todos os testes passaram"
else
    erro "Alguns testes falharam"
    exit 1
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   ✨ Instalação Concluída com Sucesso!                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "🎯 Próximos Passos:"
echo ""
echo "1️⃣  Ativar ambiente virtual:"
echo "   source venv/bin/activate  # Linux/Mac"
echo "   venv\\Scripts\\activate    # Windows"
echo ""
echo "2️⃣  Transcrever seu primeiro vídeo:"
echo "   python transcricao_videos.py --input video.mp4 --output transcricoes/"
echo ""
echo "3️⃣  Ver todos os exemplos:"
echo "   ls exemplos/"
echo ""
echo "4️⃣  Ler o guia completo:"
echo "   cat GUIA_USO.md"
echo ""
echo "📚 Recursos:"
echo "   README.md    - Visão geral do projeto"
echo "   GUIA_USO.md  - Guia detalhado de uso"
echo "   exemplos/    - Scripts de exemplo prontos"
echo ""
echo "💡 Dica: Comece com o modelo 'base' para testes rápidos,"
echo "   depois use 'medium' para melhor precisão em português."
echo ""
echo "🚀 Bom trabalho!"
echo ""
