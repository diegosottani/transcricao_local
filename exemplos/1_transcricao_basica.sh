#!/bin/bash
# 🎯 Exemplo 1: Transcrição Básica
# Transcreve um único vídeo com configurações padrão

echo "🎬 Exemplo: Transcrição Básica"
echo "================================"

# Ativar ambiente virtual
source ../venv/bin/activate

# Transcrever vídeo único
python ../transcricao_videos.py \
  --input "seu_video.mp4" \
  --output "transcricoes/" \
  --modelo base \
  --idioma pt

echo "✅ Transcrição concluída!"
echo "📁 Verifique a pasta 'transcricoes/'"
