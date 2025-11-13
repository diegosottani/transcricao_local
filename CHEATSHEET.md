# 🚀 Cheatsheet - Comandos Rápidos

> **Cola rápida dos comandos mais usados**

---

## 🎯 Comandos Essenciais

### Instalação Inicial

```bash
# Instalar tudo automaticamente
./instalar.sh

# OU manualmente:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ativar Ambiente

```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

---

## 📝 Transcrição

### Um Vídeo

```bash
python transcricao_videos.py -i video.mp4 -o transcricoes/
```

### Pasta Inteira

```bash
python transcricao_videos.py -i videos/ -o transcricoes/
```

### Com Modelo Específico

```bash
# Base (rápido, bom para português)
python transcricao_videos.py -i video.mp4 -o out/ -m base

# Medium (melhor para português)
python transcricao_videos.py -i video.mp4 -o out/ -m medium

# Large (máxima precisão)
python transcricao_videos.py -i video.mp4 -o out/ -m large
```

### Em Outro Idioma

```bash
# Inglês
python transcricao_videos.py -i video.mp4 -o out/ -l en

# Espanhol
python transcricao_videos.py -i video.mp4 -o out/ -l es
```

---

## 🛠️ Pré-Processamento

### Ver Info do Vídeo

```bash
python preprocessar_videos.py info -i video.mp4
python preprocessar_videos.py info -i videos/  # pasta
```

### Extrair Áudio

```bash
# Um vídeo
python preprocessar_videos.py extrair -i video.mp4 -o audios/

# Pasta inteira
python preprocessar_videos.py extrair -i videos/ -o audios/
```

### Limpar Áudio

```bash
python preprocessar_videos.py limpar -i audio.wav -o audios_limpos/
python preprocessar_videos.py limpar -i audios/ -o audios_limpos/
```

### Dividir Vídeo Longo

```bash
# Chunks de 20 minutos (padrão: 30)
python preprocessar_videos.py dividir -i video.mp4 -o chunks/ -d 20
```

---

## 🎮 Workflows Completos

### Pipeline Básico

```bash
# 1. Extrair áudio
python preprocessar_videos.py extrair -i video.mp4 -o audios/

# 2. Transcrever
python transcricao_videos.py -i audios/ -o transcricoes/ -m base
```

### Pipeline de Produção

```bash
# 1. Ver informações
python preprocessar_videos.py info -i videos/

# 2. Extrair áudios
python preprocessar_videos.py extrair -i videos/ -o 1_audios/

# 3. Limpar áudios
python preprocessar_videos.py limpar -i 1_audios/ -o 2_audios_limpos/

# 4. Transcrever com modelo preciso
python transcricao_videos.py -i 2_audios_limpos/ -o 3_transcricoes/ -m medium

# 5. Copiar para Obsidian
cp 3_transcricoes/*.md ~/Obsidian/MeuVault/Videos/
```

### Vídeo Longo (2+ horas)

```bash
# 1. Dividir em chunks
python preprocessar_videos.py dividir -i video_longo.mp4 -o chunks/ -d 20

# 2. Transcrever chunks
python transcricao_videos.py -i chunks/ -o transcricoes/ -m base

# 3. Combinar (Linux/Mac)
cat transcricoes/*.txt > transcricao_completa.txt
```

---

## 📁 Estrutura Recomendada

```
meu_projeto/
├── videos_originais/       # Vídeos fonte
├── 1_audios/              # Áudios extraídos
├── 2_audios_limpos/       # Áudios processados
├── 3_transcricoes/        # Saída final
└── 4_obsidian/           # Para second brain
```

---

## ⚡ Aliases Úteis

Adicione ao seu `.bashrc` ou `.zshrc`:

```bash
# Atalho para transcrever
alias transcrever='python ~/transcricao_local/transcricao_videos.py'

# Atalho para preprocessar
alias prepvideo='python ~/transcricao_local/preprocessar_videos.py'

# Uso:
transcrever -i video.mp4 -o out/
prepvideo info -i video.mp4
```

---

## 🐛 Troubleshooting Rápido

### FFmpeg não encontrado

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Mac
brew install ffmpeg

# Verificar
ffmpeg -version
```

### Ambiente virtual não ativa

```bash
# Recriar
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Transcrição com erros

```bash
# 1. Usar modelo maior
python transcricao_videos.py -i video.mp4 -o out/ -m medium

# 2. Limpar áudio primeiro
python preprocessar_videos.py limpar -i video.mp4 -o limpo/
python transcricao_videos.py -i limpo/ -o out/ -m medium
```

### Muito lento

```bash
# 1. Usar modelo menor
python transcricao_videos.py -i video.mp4 -o out/ -m tiny

# 2. Processar só áudio (sem vídeo)
python preprocessar_videos.py extrair -i video.mp4 -o audios/
python transcricao_videos.py -i audios/ -o out/
```

---

## 📊 Escolha de Modelo

| Situação | Modelo | Comando |
|----------|--------|---------|
| Teste rápido | tiny | `-m tiny` |
| Uso geral | base | `-m base` |
| Português - qualidade | medium | `-m medium` |
| Máxima precisão | large | `-m large` |

---

## 🎯 Exemplos Práticos

### Aula de Curso

```bash
python transcricao_videos.py \
  -i "Aula 01 - Introdução.mp4" \
  -o "Curso/Transcricoes/" \
  -m medium \
  -l pt
```

### Reunião

```bash
python preprocessar_videos.py extrair -i reuniao.mp4 -o temp/
python transcricao_videos.py -i temp/ -o reunioes/ -m base
```

### Podcast

```bash
python transcricao_videos.py \
  -i "podcast_ep001.mp3" \
  -o "Podcasts/Notas/" \
  -m base
```

### Lote de Vídeos

```bash
python transcricao_videos.py \
  -i "Nova Pasta de Videos/" \
  -o "Todas Transcricoes/" \
  -m base
```

---

## 🔧 Comandos do Sistema

### Listar Vídeos

```bash
# Linux/Mac
ls -lh videos/*.mp4

# Windows
dir videos\*.mp4
```

### Verificar Espaço

```bash
# Linux/Mac
du -sh transcricoes/

# Windows  
dir /s transcricoes\
```

### Limpar Cache

```bash
# Remover arquivos temporários
rm -rf __pycache__
rm -rf *.pyc

# Limpar ambiente virtual
rm -rf venv
```

---

## 💾 Backup

```bash
# Fazer backup das transcrições
tar -czf backup_$(date +%Y%m%d).tar.gz transcricoes/

# Extrair backup
tar -xzf backup_20251112.tar.gz
```

---

## 🚀 Automação

### Processar Durante a Noite

```bash
# Criar script
cat > transcrever_noturno.sh << 'EOF'
#!/bin/bash
cd ~/transcricao_local
source venv/bin/activate
python transcricao_videos.py -i videos/ -o transcricoes/ -m medium
EOF

chmod +x transcrever_noturno.sh

# Agendar (cron)
crontab -e
# Adicionar: 0 2 * * * /home/usuario/transcricao_local/transcrever_noturno.sh
```

---

## 📚 Ajuda

### Ver Todas as Opções

```bash
# Transcritor
python transcricao_videos.py --help

# Preprocessador
python preprocessar_videos.py --help
```

### Verificar Versão

```bash
python --version
ffmpeg -version
pip list | grep whisper
```

---

**💡 Dica:** Guarde este arquivo! É sua referência rápida para uso diário.

---

*Cheatsheet criado por Diego Sottani - 2025*
