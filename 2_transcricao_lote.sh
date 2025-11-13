#!/bin/bash
# 🎯 Exemplo 2: Transcrição em Lote
# Transcreve múltiplos vídeos de uma pasta

echo "🎬 Exemplo: Transcrição em Lote"
echo "================================"

# Ativar ambiente virtual
source ../venv/bin/activate

# Criar diretórios se não existirem
mkdir -p videos
mkdir -p transcricoes

# Transcrever todos os vídeos da pasta
python ../transcricao_videos.py \
  --input "videos/" \
  --output "transcricoes/" \
  --modelo base \
  --idioma pt

echo "✅ Todos os vídeos foram transcritos!"
echo "📁 Verifique a pasta 'transcricoes/'"
