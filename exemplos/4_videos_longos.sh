#!/bin/bash
# 🎯 Exemplo 4: Dividir e Transcrever Vídeos Longos
# Para vídeos de 2+ horas

echo "🎬 Exemplo: Vídeos Longos"
echo "=========================="

# Ativar ambiente virtual
source ../venv/bin/activate

# Configurações
VIDEO_LONGO="video_longo.mp4"
DURACAO_CHUNK=20  # minutos
MODELO="base"     # use "medium" para melhor precisão

# Criar diretórios
mkdir -p chunks
mkdir -p transcricoes_parciais
mkdir -p transcricao_final

echo ""
echo "✂️  ETAPA 1: Dividindo vídeo em chunks de ${DURACAO_CHUNK} minutos..."
python ../preprocessar_videos.py dividir \
  --input "$VIDEO_LONGO" \
  --output chunks/ \
  --duracao $DURACAO_CHUNK

echo ""
echo "📝 ETAPA 2: Transcrevendo todos os chunks..."
python ../transcrever.py \
  --input chunks/ \
  --output transcricoes_parciais/ \
  --modelo $MODELO

echo ""
echo "📋 ETAPA 3: Combinando transcrições..."
# Combinar todos os arquivos .txt em um só
cat transcricoes_parciais/*.txt > transcricao_final/completo.txt

# Combinar todos os .md preservando estrutura
echo "# 📹 Transcrição Completa - $VIDEO_LONGO" > transcricao_final/completo.md
echo "" >> transcricao_final/completo.md
echo "---" >> transcricao_final/completo.md
echo "" >> transcricao_final/completo.md

for arquivo in transcricoes_parciais/*.md; do
    nome_parte=$(basename "$arquivo" .md)
    echo "## 🎬 $nome_parte" >> transcricao_final/completo.md
    echo "" >> transcricao_final/completo.md
    # Pular as linhas de cabeçalho
    tail -n +5 "$arquivo" >> transcricao_final/completo.md
    echo "" >> transcricao_final/completo.md
    echo "---" >> transcricao_final/completo.md
    echo "" >> transcricao_final/completo.md
done

echo ""
echo "✅ Processamento concluído!"
echo "📁 Arquivos:"
echo "   chunks/                 - Vídeo dividido"
echo "   transcricoes_parciais/  - Transcrições de cada parte"
echo "   transcricao_final/      - Transcrição completa unificada"
