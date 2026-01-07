# Sistema de Transcricao Local de Videos

> Transcreva videos localmente usando Whisper - Zero custos de API

Criado por Diego Sottani

---

## O que faz

Sistema completo para transcrever videos de qualquer duracao usando **Whisper da OpenAI** rodando 100% localmente.

- **100% Local** - Sem custos de API ou envio de dados para nuvem
- **Multiplos Formatos** - MP4, AVI, MOV, MKV, MP3, WAV e mais
- **Processamento em Lote** - Transcreva multiplos videos automaticamente
- **Timestamps Precisos** - Cada segmento com marcacao de tempo
- **Markdown para Obsidian** - Formatacao otimizada para second brain
- **90+ Idiomas** - Portugues, Ingles, Espanhol e outros

---

## Instalacao

### Requisitos

- Python 3.8+
- FFmpeg instalado no sistema

### Passos

```bash
# 1. Entrar na pasta do projeto
cd transcricao_local

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar FFmpeg (se nao tiver)
# Ubuntu/Debian: sudo apt install ffmpeg
# Mac: brew install ffmpeg
# Windows: https://ffmpeg.org/download.html
```

Ou use o instalador automatico: `./instalar.sh`

---

## Uso Basico

### Transcrever um video

```bash
python transcrever.py -i video.mp4 -o output/
```

### Transcrever pasta inteira

```bash
python transcrever.py -i input/ -o output/
```

### Com modelo mais preciso (recomendado para portugues)

```bash
python transcrever.py -i video.mp4 -o output/ -m medium
```

### Saida gerada

Para cada video, sao criados 3 arquivos:
- `.md` - Markdown formatado (Obsidian)
- `.txt` - Texto puro
- `.json` - Dados completos com metadados

---

## Modelos Disponiveis

| Modelo | RAM | Velocidade | Quando Usar |
|--------|-----|------------|-------------|
| `tiny` | ~1GB | Muito rapido | Testes |
| `base` | ~1GB | Rapido | **Uso geral** |
| `small` | ~2GB | Medio | Boa precisao |
| `medium` | ~5GB | Lento | **Portugues BR** |
| `large` | ~10GB | Muito lento | Maxima precisao |

**Recomendacao:** Comece com `base`. Use `medium` para trabalho serio em portugues.

---

## Utilitarios de Pre-processamento

O script `preprocessar_videos.py` oferece ferramentas adicionais:

```bash
# Ver informacoes do video
python preprocessar_videos.py info -i video.mp4

# Extrair audio (melhora performance)
python preprocessar_videos.py extrair -i video.mp4 -o audios/

# Limpar audio (remove ruido)
python preprocessar_videos.py limpar -i audio.wav -o audios_limpos/

# Dividir video longo em partes de 20 minutos
python preprocessar_videos.py dividir -i video_longo.mp4 -o chunks/ -d 20
```

---

## Tempos Estimados (CPU)

| Duracao Video | Modelo Base | Modelo Medium |
|---------------|-------------|---------------|
| 10 minutos | 2-3 min | 5-8 min |
| 30 minutos | 6-10 min | 15-20 min |
| 1 hora | 12-20 min | 30-40 min |
| 2 horas | 25-40 min | 60-80 min |

**Com GPU NVIDIA:** Ate 5x mais rapido.

---

## Exemplos Praticos

### Transcrever curso completo

```bash
python transcrever.py \
  -i "Curso Python/input/" \
  -o "Curso Python/output/" \
  -m medium
```

### Pipeline completo para video longo

```bash
# 1. Dividir video de 3h em partes de 30min
python preprocessar_videos.py dividir -i video_3h.mp4 -o chunks/ -d 30

# 2. Transcrever todas as partes
python transcrever.py -i chunks/ -o output/ -m medium

# 3. Copiar para Obsidian
cp output/*.md ~/Obsidian/MeuVault/
```

### Transcrever podcast

```bash
python transcrever.py -i podcast.mp3 -o notas/ -m base
```

---

## Troubleshooting

### FFmpeg not found

```bash
# Verificar instalacao
which ffmpeg  # Linux/Mac
where ffmpeg  # Windows

# Instalar
# Ubuntu: sudo apt install ffmpeg
# Mac: brew install ffmpeg
```

### Transcricao com muitos erros

1. Usar modelo maior: `-m medium` ou `-m large`
2. Limpar audio primeiro: `preprocessar_videos.py limpar`
3. Verificar qualidade do audio original

### Muito lento

1. Usar modelo menor: `-m tiny` ou `-m base`
2. Extrair audio primeiro: `preprocessar_videos.py extrair`
3. Instalar CUDA se tiver GPU NVIDIA
4. Dividir video em partes menores

### Falta de memoria

1. Usar modelo menor
2. Processar videos um por vez (nao em lote)
3. Dividir videos longos antes de transcrever

---

## Estrutura do Projeto

```
transcricao_local/
├── transcrever.py   # Script principal
├── preprocessar_videos.py  # Utilitarios
├── requirements.txt        # Dependencias
├── instalar.sh             # Instalador automatico
├── exemplos/               # Scripts de exemplo
└── CONTRIBUTING.md         # Guia de contribuicao
```

---

## Acelerar com GPU (Opcional)

Se tiver GPU NVIDIA:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

O Whisper detectara automaticamente a GPU.

---

## Referencia Rapida

### Transcricao

```bash
python transcrever.py -i video.mp4 -o out/           # Um video
python transcrever.py -i input/ -o out/              # Pasta
python transcrever.py -i video.mp4 -o out/ -m medium # Modelo
python transcrever.py -i video.mp4 -o out/ -l en     # Idioma
```

### Pre-processamento

```bash
python preprocessar_videos.py info -i video.mp4             # Info
python preprocessar_videos.py extrair -i video.mp4 -o out/  # Extrair audio
python preprocessar_videos.py limpar -i audio.wav -o out/   # Limpar audio
python preprocessar_videos.py dividir -i video.mp4 -o out/ -d 20  # Dividir
```

### Atalhos (opcional)

Adicionar ao `~/.bashrc`:

```bash
alias transcrever='python ~/transcricao_local/transcrever.py'
alias prepvideo='python ~/transcricao_local/preprocessar_videos.py'
```

---

## Links

- [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir
- [Whisper (OpenAI)](https://github.com/openai/whisper) - Documentacao oficial

---

## Licenca

Codigo aberto para uso pessoal e comercial.

---

*Desenvolvido por Diego Sottani - "Transformando complexidade em clareza"*
