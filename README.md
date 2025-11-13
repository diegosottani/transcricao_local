# 🎯 Sistema de Transcrição Local de Vídeos

> **Transcreva vídeos longos localmente usando Whisper - Zero custos de API**  
> Criado por Diego Sottani - Arquitetura da Clareza

---

## 🌟 Visão Geral

Sistema completo para transcrever vídeos de qualquer duração usando **Whisper da OpenAI** rodando 100% localmente no seu computador.

### ✨ Características

- ✅ **100% Local** - Sem custos de API ou envio de dados para nuvem
- ✅ **Múltiplos Formatos** - Suporta MP4, AVI, MOV, MKV, MP3, WAV e mais
- ✅ **Processamento em Lote** - Transcreva múltiplos vídeos automaticamente
- ✅ **Timestamps Precisos** - Cada segmento com marcação de tempo
- ✅ **Markdown para Obsidian** - Formatação otimizada para second brain
- ✅ **Metadados Completos** - Duração, idioma, modelo usado, etc.
- ✅ **Múltiplos Idiomas** - Português, Inglês, Espanhol e 90+ idiomas

---

## 🚀 Quick Start (5 minutos)

### 1. Instalação Rápida

```bash
# Clone ou baixe este repositório
cd transcricao_local

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependências
pip install openai-whisper ffmpeg-python

# Instalar FFmpeg (se ainda não tiver)
# Ubuntu/Debian: sudo apt install ffmpeg
# Mac: brew install ffmpeg
# Windows: baixar de https://ffmpeg.org/download.html
```

### 2. Transcrever Seu Primeiro Vídeo

```bash
python transcricao_videos.py \
  --input seu_video.mp4 \
  --output transcricoes/
```

**Pronto!** Suas transcrições estarão em `transcricoes/` em 3 formatos:
- `.md` - Markdown formatado (Obsidian)
- `.txt` - Texto puro
- `.json` - Dados completos com metadados

---

## 📁 Estrutura do Projeto

```
transcricao_local/
├── transcricao_videos.py      # 🎯 Script principal de transcrição
├── preprocessar_videos.py     # 🛠️ Utilitários de pré-processamento
├── GUIA_USO.md                # 📖 Guia completo de uso
├── README.md                  # 📄 Este arquivo
├── requirements.txt           # 📦 Dependências Python
└── exemplos/                  # 💡 Exemplos de uso
    ├── transcricao_basica.sh
    ├── transcricao_lote.sh
    └── workflow_completo.sh
```

---

## 🎮 Casos de Uso

### 1. Transcrever Vídeos de Curso

```bash
python transcricao_videos.py \
  --input "Curso Completo/videos/" \
  --output "Curso Completo/transcricoes/" \
  --modelo medium
```

### 2. Extrair Insights de Reuniões

```bash
# Extrair áudio primeiro (melhor performance)
python preprocessar_videos.py extrair \
  --input reuniao.mp4 \
  --output audios/

# Transcrever
python transcricao_videos.py \
  --input audios/reuniao.wav \
  --output transcricoes/
```

### 3. Dividir e Transcrever Vídeos Longos

```bash
# Dividir em chunks de 20 minutos
python preprocessar_videos.py dividir \
  --input video_3h.mp4 \
  --output chunks/ \
  --duracao 20

# Transcrever todos os chunks
python transcricao_videos.py \
  --input chunks/ \
  --output transcricoes/
```

### 4. Pipeline Completo (Produção)

```bash
# 1. Ver informações dos vídeos
python preprocessar_videos.py info --input videos/

# 2. Extrair e limpar áudios
python preprocessar_videos.py extrair --input videos/ --output audios/
python preprocessar_videos.py limpar --input audios/ --output audios_limpos/

# 3. Transcrever com modelo preciso
python transcricao_videos.py \
  --input audios_limpos/ \
  --output transcricoes/ \
  --modelo medium

# 4. Copiar para Obsidian
cp transcricoes/*.md ~/Obsidian/MeuVault/Transcricoes/
```

---

## 🎯 Modelos Whisper

| Modelo | RAM | Velocidade | Precisão | Quando Usar |
|--------|-----|------------|----------|-------------|
| `tiny` | ~1GB | ⚡⚡⚡⚡ | ⭐⭐ | Testes rápidos |
| `base` | ~1GB | ⚡⚡⚡ | ⭐⭐⭐ | **Uso geral** (recomendado) |
| `small` | ~2GB | ⚡⚡ | ⭐⭐⭐⭐ | Boa precisão |
| `medium` | ~5GB | ⚡ | ⭐⭐⭐⭐⭐ | **Português BR** (melhor) |
| `large` | ~10GB | 🐌 | ⭐⭐⭐⭐⭐ | Máxima precisão |

**Recomendação:** 
- Comece com `base` para testar
- Use `medium` para trabalho sério em português
- Reserve `large` para casos críticos

---

## 📊 Performance Esperada

### Tempos de Transcrição (CPU i5/Ryzen 5)

| Duração Vídeo | Modelo Base | Modelo Medium |
|---------------|-------------|---------------|
| 10 minutos | 2-3 min | 5-8 min |
| 30 minutos | 6-10 min | 15-20 min |
| 1 hora | 12-20 min | 30-40 min |
| 2 horas | 25-40 min | 60-80 min |

**Com GPU (CUDA):** Até 3-5x mais rápido!

---

## 🛠️ Ferramentas Incluídas

### 1. `transcricao_videos.py` - Transcritor Principal

```bash
# Ver todas as opções
python transcricao_videos.py --help

# Exemplos
python transcricao_videos.py -i video.mp4 -o output/
python transcricao_videos.py -i videos/ -o output/ -m medium
python transcricao_videos.py -i video.mp4 -o output/ -l en
```

### 2. `preprocessar_videos.py` - Utilitários

```bash
# Ver todas as opções
python preprocessar_videos.py --help

# Operações disponíveis
extrair  - Extrair áudio de vídeos
limpar   - Limpar e normalizar áudio
dividir  - Dividir vídeos longos
info     - Ver metadados de vídeos
```

---

## 🎨 Exemplo de Saída

### Markdown Gerado (`.md`)

```markdown
# 📹 aula_python_avancado

---

## 📊 Metadados

| Campo | Valor |
|-------|-------|
| **Arquivo Original** | `aula_python_avancado.mp4` |
| **Data Transcrição** | 2025-11-12 10:30:00 |
| **Duração** | 1:23:45 |
| **Idioma** | pt |
| **Segmentos** | 342 |

---

## 📝 Transcrição Completa

[Texto completo aqui...]

---

## ⏱️ Transcrição com Timestamps

**[00:00:00 → 00:00:15]**
Olá pessoal, bem-vindos à aula de Python avançado...

**[00:00:15 → 00:00:32]**
Hoje vamos falar sobre decoradores e metaclasses...
```

---

## ⚙️ Configuração Avançada

### Acelerar com GPU (Opcional)

Se você tem GPU NVIDIA:

```bash
# Instalar PyTorch com CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Whisper detectará automaticamente a GPU
python transcricao_videos.py -i video.mp4 -o output/
```

### Integração com Obsidian

Adicione ao seu workflow:

```bash
# Configurar output direto para Obsidian
OBSIDIAN_PATH="$HOME/Obsidian/MeuVault"

python transcricao_videos.py \
  --input videos/ \
  --output "$OBSIDIAN_PATH/Transcricoes/"
```

### Automação com Cron (Linux/Mac)

```bash
# Editar crontab
crontab -e

# Adicionar (executa todo dia às 2h da manhã)
0 2 * * * cd /path/to/transcricao_local && python transcricao_videos.py -i videos/ -o transcricoes/
```

---

## 🐛 Troubleshooting

### Problema: "FFmpeg not found"

```bash
# Verificar se está instalado
which ffmpeg  # Linux/Mac
where ffmpeg  # Windows

# Instalar se necessário
# Ubuntu/Debian: sudo apt install ffmpeg
# Mac: brew install ffmpeg
```

### Problema: Transcrição com muitos erros

**Soluções:**
1. Usar modelo maior: `--modelo medium` ou `--modelo large`
2. Limpar áudio antes: `python preprocessar_videos.py limpar`
3. Verificar qualidade do áudio original

### Problema: Muito lento

**Soluções:**
1. Usar modelo menor: `--modelo tiny` ou `--modelo base`
2. Extrair áudio primeiro: `preprocessar_videos.py extrair`
3. Instalar CUDA se tiver GPU NVIDIA
4. Dividir vídeo em partes menores

### Problema: Falta de memória

**Soluções:**
1. Usar modelo menor
2. Processar vídeos individualmente (não em lote)
3. Dividir vídeos longos antes de transcrever

---

## 📚 Recursos Adicionais

- **[GUIA_USO.md](GUIA_USO.md)** - Guia detalhado com mais exemplos
- **[Documentação Whisper](https://github.com/openai/whisper)** - Repositório oficial
- **[FFmpeg Guide](https://ffmpeg.org/documentation.html)** - Documentação FFmpeg

---

## 🎯 Próximos Passos

Depois de dominar o básico:

1. **Integre com IA** - Use as transcrições como input para análise com LLMs
2. **Crie Workflows** - Automatize todo o processo
3. **Analise Padrões** - Use as transcrições para extrair insights
4. **Second Brain** - Organize no Obsidian com tags e links

---

## 💡 Dicas Pro

### 1. Processamento Noturno

Configure para transcrever enquanto dorme:

```bash
# Script simples
#!/bin/bash
cd ~/transcricao_local
source venv/bin/activate
python transcricao_videos.py -i ~/videos_novos/ -o ~/transcricoes/ -m medium
```

### 2. Backup Automático

```bash
# Após transcrever, fazer backup
python transcricao_videos.py -i videos/ -o transcricoes/
tar -czf backup_$(date +%Y%m%d).tar.gz transcricoes/
```

### 3. Notificações

```bash
# Linux
python transcricao_videos.py -i videos/ -o out/ && notify-send "Pronto!"

# Mac  
python transcricao_videos.py -i videos/ -o out/ && osascript -e 'display notification "Pronto!"'
```

---

## 🤝 Contribuindo

Melhorias são bem-vindas! Áreas de interesse:

- [ ] Interface gráfica (GUI)
- [ ] Suporte a mais idiomas
- [ ] Integração com mais ferramentas
- [ ] Otimizações de performance
- [ ] Análise de sentimentos
- [ ] Sumarização automática

---

## 📄 Licença

Este projeto é de código aberto e disponível para uso pessoal e comercial.

---

## 👨‍💻 Autor

**Diego Sottani**  
Arquiteto de Sistemas | INTJ-A  
*"Transformando complexidade em clareza"*

---

## 🌟 Agradecimentos

- OpenAI pela criação do Whisper
- Comunidade Python
- Todos que contribuíram com feedback

---

**💡 Lembre-se:** Este sistema roda 100% localmente. Suas transcrições nunca saem do seu computador!

---

*Última atualização: Novembro 2025*
