# CLAUDE.md - Guia para Claude Code

> Instruções para Claude Code trabalhar neste projeto

## Visao Geral do Projeto

Sistema de transcricao local de videos usando Whisper (OpenAI). Processa videos/audios e gera transcricoes em 3 formatos: Markdown (Obsidian), texto puro e JSON.

**Autor:** Diego Sottani

## Estrutura do Projeto

```
transcricao_local/
├── transcricao_videos.py    # Script principal - classe TranscritorVideos
├── preprocessar_videos.py   # Utilitarios - classe PreProcessadorVideo
├── requirements.txt         # Dependencias Python
├── instalar.sh              # Script de instalacao automatica
├── exemplos/                # Scripts shell de exemplo
│   ├── 1_transcricao_basica.sh
│   ├── 2_transcricao_lote.sh
│   ├── 3_workflow_completo.sh
│   └── 4_videos_longos.sh
├── videos/                  # Pasta para videos de entrada (gitignore)
├── transcricoes/            # Pasta para saidas (gitignore)
└── venv/                    # Ambiente virtual Python (gitignore)
```

## Arquivos Principais

### transcricao_videos.py

- **Classe:** `TranscritorVideos`
- **Funcao:** Transcreve videos usando Whisper
- **Metodos principais:**
  - `transcrever_video(video_path, output_dir)` - Transcreve um video
  - `transcrever_lote(input_dir, output_dir)` - Transcreve pasta inteira
  - `_gerar_markdown()` - Formata saida para Obsidian
- **CLI:** `python transcricao_videos.py -i <input> -o <output> -m <modelo> -l <idioma>`

### preprocessar_videos.py

- **Classe:** `PreProcessadorVideo`
- **Funcao:** Prepara videos antes da transcricao
- **Operacoes:**
  - `extrair` - Extrai audio de video (WAV 16kHz mono)
  - `limpar` - Aplica filtros de audio (highpass, lowpass, loudnorm)
  - `dividir` - Divide video longo em chunks
  - `info` - Mostra metadados do video
- **CLI:** `python preprocessar_videos.py <operacao> -i <input> -o <output>`

## Dependencias

- `openai-whisper` - Engine de transcricao
- `ffmpeg-python` - Manipulacao de video/audio
- `torch` - Backend ML (GPU opcional com CUDA)
- FFmpeg deve estar instalado no sistema

## Modelos Whisper Disponiveis

| Modelo | RAM | Uso |
|--------|-----|-----|
| tiny | ~1GB | Testes rapidos |
| base | ~1GB | Uso geral |
| small | ~2GB | Boa precisao |
| medium | ~5GB | Melhor para portugues |
| large | ~10GB | Maxima precisao |

## Comandos Uteis para Desenvolvimento

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Testar transcricao
python transcricao_videos.py -i video.mp4 -o out/ -m tiny

# Ver info de video
python preprocessar_videos.py info -i video.mp4

# Extrair audio
python preprocessar_videos.py extrair -i video.mp4 -o audios/
```

## Convencoes de Codigo

- **Estilo:** PEP 8
- **Docstrings:** Google Style
- **Type hints:** Quando possivel
- **Idioma codigo:** Portugues (variaveis, comentarios)
- **Commits:** Conventional Commits (feat, fix, docs, etc)

## Extensoes de Arquivos Suportadas

- **Video:** .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm
- **Audio:** .mp3, .wav, .m4a, .flac, .ogg

## Saidas Geradas

Para cada video transcrito, sao gerados 3 arquivos:

1. `nome.md` - Markdown formatado (metadados + texto + timestamps)
2. `nome.txt` - Texto puro da transcricao
3. `nome.json` - Dados completos com segmentos

## Como Adicionar Features

1. **Nova operacao de preprocessamento:**
   - Adicionar metodo em `PreProcessadorVideo`
   - Atualizar `processar_lote()` e `main()` com nova opcao

2. **Novo formato de saida:**
   - Adicionar metodo `_gerar_<formato>()` em `TranscritorVideos`
   - Chamar no `transcrever_video()`

3. **Novo modelo/configuracao:**
   - Verificar se Whisper suporta
   - Adicionar em `MODELOS_DISPONIVEIS` se necessario

## Troubleshooting Comum

- **FFmpeg not found:** Instalar via apt/brew
- **CUDA not available:** Funciona em CPU, apenas mais lento
- **Memoria insuficiente:** Usar modelo menor ou dividir video
- **Transcricao com erros:** Usar modelo maior ou limpar audio

## Arquivos Ignorados pelo Git

- `venv/` - Ambiente virtual
- `videos/` - Videos de entrada
- `transcricoes/` - Saidas geradas
- `*.mp4`, `*.wav`, etc - Arquivos de midia
- `*.pt` - Modelos Whisper baixados
