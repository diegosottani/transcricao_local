# 🎯 Guia Completo - Sistema de Transcrição Local

> **Sistema criado para Diego Sottani**  
> Transcrição local de vídeos longos com Whisper - Zero custos de API

---

## 📦 Instalação Rápida

### 1. Preparar Ambiente

```bash
# Criar pasta do projeto
mkdir transcricao_local
cd transcricao_local

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate  # Windows

# Instalar dependências
pip install openai-whisper
pip install ffmpeg-python
```

### 2. Instalar FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Mac:**
```bash
brew install ffmpeg
```

**Windows:**
- Baixar de: https://ffmpeg.org/download.html
- Adicionar ao PATH do sistema

**Verificar instalação:**
```bash
ffmpeg -version
```

---

## 🚀 Uso Básico

### Transcrever um Único Vídeo

```bash
python transcricao_videos.py \
  --input video_aula.mp4 \
  --output transcricoes/
```

### Transcrever Pasta Inteira (Lote)

```bash
python transcricao_videos.py \
  --input pasta_videos/ \
  --output transcricoes/
```

### Com Modelo Mais Preciso

```bash
python transcricao_videos.py \
  --input video.mp4 \
  --output transcricoes/ \
  --modelo medium
```

### Em Inglês

```bash
python transcricao_videos.py \
  --input video.mp4 \
  --output transcricoes/ \
  --idioma en
```

---

## 📊 Modelos Disponíveis

| Modelo | Tamanho | Velocidade | Precisão | Uso Recomendado |
|--------|---------|------------|----------|-----------------|
| `tiny` | 39MB | ⚡⚡⚡⚡ | ⭐⭐ | Testes rápidos |
| `base` | 74MB | ⚡⚡⚡ | ⭐⭐⭐ | **USO GERAL** |
| `small` | 244MB | ⚡⚡ | ⭐⭐⭐⭐ | Boa precisão |
| `medium` | 769MB | ⚡ | ⭐⭐⭐⭐⭐ | **PORTUGUÊS** |
| `large` | 1550MB | 🐌 | ⭐⭐⭐⭐⭐ | Máxima precisão |

**Recomendação:** Comece com `base`, se precisar de mais precisão use `medium`.

---

## 📁 Estrutura de Saída

Para cada vídeo processado, o sistema gera 3 arquivos:

```
transcricoes/
├── video_aula.md      # Markdown formatado (Obsidian)
├── video_aula.txt     # Texto puro
└── video_aula.json    # Dados completos (metadados + segmentos)
```

### Exemplo de Markdown Gerado

```markdown
# 📹 video_aula

---

## 📊 Metadados

| Campo | Valor |
|-------|-------|
| **Arquivo Original** | `video_aula.mp4` |
| **Data Transcrição** | 2025-11-12 10:30:00 |
| **Duração** | 1:23:45 |
| **Idioma** | pt |
| **Segmentos** | 342 |

---

## 📝 Transcrição Completa

[Texto completo sem timestamps]

---

## ⏱️ Transcrição com Timestamps

**[00:00:00 → 00:00:15]**
Olá pessoal, bem-vindos à aula de hoje...

**[00:00:15 → 00:00:32]**
Vamos começar falando sobre...
```

---

## ⚡ Casos de Uso Práticos

### 1. Transcrever Vídeos de Curso

```bash
# Organizar estrutura
mkdir -p cursos/modulo1/videos
mkdir -p cursos/modulo1/transcricoes

# Transcrever
python transcricao_videos.py \
  --input cursos/modulo1/videos/ \
  --output cursos/modulo1/transcricoes/
```

### 2. Extrair Insights de Reuniões

```bash
python transcricao_videos.py \
  --input reuniao_equipe_2025-11-12.mp4 \
  --output reunioes/transcricoes/ \
  --modelo medium
```

### 3. Criar Notas de Podcasts

```bash
python transcricao_videos.py \
  --input podcast_ep001.mp3 \
  --output podcast/notas/
```

---

## 🔧 Troubleshooting

### Erro: "FFmpeg not found"

**Solução:**
```bash
# Verificar se FFmpeg está instalado
which ffmpeg  # Linux/Mac
where ffmpeg  # Windows

# Se não estiver, instalar conforme seção "Instalação"
```

### Erro: "CUDA not available"

**Não é problema!** Whisper funciona perfeitamente em CPU, apenas será um pouco mais lento.

**Para acelerar (opcional):**
```bash
# Instalar PyTorch com CUDA (se tiver GPU NVIDIA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Vídeo muito longo / Travando

**Soluções:**
1. Usar modelo menor (`tiny` ou `base`)
2. Processar vídeos individualmente
3. Dividir vídeo em partes menores:

```bash
# Dividir vídeo em chunks de 30 minutos
ffmpeg -i video_longo.mp4 -c copy -map 0 -segment_time 00:30:00 -f segment output%03d.mp4
```

### Transcrição com erros/palavras incorretas

**Soluções:**
1. Usar modelo maior (`medium` ou `large`)
2. Melhorar qualidade do áudio:

```bash
# Limpar áudio antes de transcrever
ffmpeg -i video.mp4 -af "highpass=f=200, lowpass=f=3000" audio_limpo.wav
```

---

## 🎯 Otimizações para Seu Workflow

### 1. Integração com Obsidian

Salvar transcrições diretamente no seu vault:

```bash
python transcricao_videos.py \
  --input video.mp4 \
  --output ~/Obsidian/MeuVault/Transcricoes/
```

### 2. Script de Automação

Criar um alias no seu `.bashrc` ou `.zshrc`:

```bash
# Adicionar ao ~/.bashrc ou ~/.zshrc
alias transcrever='python ~/projetos/transcricao_local/transcricao_videos.py'

# Usar:
transcrever --input video.mp4 --output transcricoes/
```

### 3. Processar Pasta do Google Drive

```bash
# Sincronizar pasta do Drive
cd ~/GoogleDrive/Videos

# Transcrever tudo
python transcricao_videos.py \
  --input . \
  --output ../Transcricoes/
```

---

## 📈 Estimativas de Tempo

| Duração Vídeo | Modelo Base | Modelo Medium |
|---------------|-------------|---------------|
| 10 minutos | ~2-3 min | ~5-8 min |
| 30 minutos | ~6-10 min | ~15-20 min |
| 1 hora | ~12-20 min | ~30-40 min |
| 2 horas | ~25-40 min | ~60-80 min |

*Tempos aproximados em CPU moderna (i5/Ryzen 5 ou superior)*

---

## 🎮 Comandos Úteis

### Listar Vídeos Disponíveis

```bash
# Linux/Mac
ls -lh pasta_videos/*.mp4

# Windows
dir pasta_videos\*.mp4
```

### Verificar Espaço em Disco

```bash
# Linux/Mac
du -sh transcricoes/

# Windows
dir /s transcricoes\
```

### Mover Transcrições para Obsidian

```bash
# Linux/Mac
cp -r transcricoes/*.md ~/Obsidian/MeuVault/Videos/

# Windows
xcopy transcricoes\*.md C:\Obsidian\MeuVault\Videos\ /s
```

---

## 💡 Dicas Pro

### 1. Processar Durante a Noite

```bash
# Linux/Mac - Agendar com cron
crontab -e
# Adicionar: 0 2 * * * cd ~/transcricao_local && python transcricao_videos.py --input videos/ --output transcricoes/
```

### 2. Backup Automático

```bash
# Após transcrever, fazer backup
python transcricao_videos.py --input videos/ --output transcricoes/
tar -czf backup_transcricoes_$(date +%Y%m%d).tar.gz transcricoes/
```

### 3. Notificação ao Concluir

```bash
# Linux
python transcricao_videos.py --input videos/ --output transcricoes/ && notify-send "Transcrição Concluída!"

# Mac
python transcricao_videos.py --input videos/ --output transcricoes/ && osascript -e 'display notification "Transcrição Concluída!"'
```

---

## 🔗 Recursos Adicionais

- [Documentação Whisper](https://github.com/openai/whisper)
- [FFmpeg Guia](https://ffmpeg.org/documentation.html)
- [Obsidian Markdown](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax)

---

## 📞 Suporte

Se encontrar problemas:
1. Verificar se FFmpeg está instalado
2. Confirmar que o ambiente virtual está ativado
3. Testar com modelo `tiny` primeiro
4. Verificar se o vídeo não está corrompido

---

**Sistema criado por Diego Sottani - 2025**  
*Arquitetura da Clareza aplicada à transcrição de vídeos*
