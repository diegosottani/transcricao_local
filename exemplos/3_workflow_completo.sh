#!/bin/bash
# 🎯 Exemplo 3: Workflow Completo de Produção
# Pipeline completo: info → extrair → limpar → transcrever

echo "🎬 Exemplo: Workflow Completo"
echo "=============================="

# Ativar ambiente virtual
source ../venv/bin/activate

# Criar estrutura de diretórios
mkdir -p videos
mkdir -p 1_audios_originais
mkdir -p 2_audios_limpos
mkdir -p 3_transcricoes
mkdir -p 4_obsidian

echo ""
echo "📊 ETAPA 1: Analisando vídeos..."
python ../preprocessar_videos.py info --input videos/

echo ""
echo "🎵 ETAPA 2: Extraindo áudios..."
python ../preprocessar_videos.py extrair \
  --input videos/ \
  --output 1_audios_originais/

echo ""
echo "🧹 ETAPA 3: Limpando áudios..."
python ../preprocessar_videos.py limpar \
  --input 1_audios_originais/ \
  --output 2_audios_limpos/

echo ""
echo "📝 ETAPA 4: Transcrevendo com modelo preciso..."
python ../transcricao_videos.py \
  --input 2_audios_limpos/ \
  --output 3_transcricoes/ \
  --modelo medium \
  --idioma pt

echo ""
echo "📋 ETAPA 5: Copiando para Obsidian..."
cp 3_transcricoes/*.md 4_obsidian/

echo ""
echo "✅ Workflow completo concluído!"
echo "📁 Estrutura final:"
echo "   videos/              - Vídeos originais"
echo "   1_audios_originais/  - Áudios extraídos"
echo "   2_audios_limpos/     - Áudios normalizados"
echo "   3_transcricoes/      - Transcrições (.md, .txt, .json)"
echo "   4_obsidian/          - Prontos para Obsidian"
