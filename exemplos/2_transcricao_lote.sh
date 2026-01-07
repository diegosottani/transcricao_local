#!/bin/bash
# 🎯 Exemplo 2: Transcrição em Lote
# Transcreve múltiplos vídeos de uma pasta

echo "🎬 Exemplo: Transcrição em Lote"
echo "================================"

# Ativar ambiente virtual
source ../venv/bin/activate

# Criar diretórios se não existirem
mkdir -p input
mkdir -p output

# Transcrever todos os vídeos da pasta
python ../transcrever.py \
  --input "input/" \
  --output "output/" \
  --modelo base \
  --idioma pt

echo "✅ Todos os vídeos foram transcritos!"
echo "📁 Verifique a pasta 'output/'"
