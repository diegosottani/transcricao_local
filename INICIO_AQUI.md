# 🎯 COMECE AQUI - Sistema de Transcrição Local

> **Diego, este é seu sistema completo para transcrever vídeos localmente!**  
> Siga os passos abaixo para começar em 10 minutos.

---

## 📦 O Que Você Recebeu

```
📁 transcricao_local/
│
├── 🚀 instalar.sh                    ← EXECUTE PRIMEIRO!
├── 📝 transcricao_videos.py          ← Script principal
├── 🛠️ preprocessar_videos.py         ← Utilitários
├── 📋 requirements.txt               ← Dependências
│
├── 📖 README.md                      ← Visão geral completa
├── 📚 GUIA_USO.md                    ← Guia detalhado
├── ⚡ CHEATSHEET.md                  ← Comandos rápidos
│
└── 💡 exemplos/                      ← Scripts prontos
    ├── 1_transcricao_basica.sh
    ├── 2_transcricao_lote.sh
    ├── 3_workflow_completo.sh
    └── 4_videos_longos.sh
```

---

## 🚀 Instalação (5 minutos)

### Opção 1: Instalação Automática (RECOMENDADO)

```bash
# 1. Abrir terminal na pasta do projeto
cd transcricao_local

# 2. Executar instalador
./instalar.sh

# 3. Pronto! Pular para "Primeiro Uso"
```

### Opção 2: Instalação Manual

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Instalar FFmpeg (se ainda não tiver)
# Ubuntu/Debian: sudo apt install ffmpeg
# Mac: brew install ffmpeg
# Windows: https://ffmpeg.org/download.html
```

---

## 🎬 Primeiro Uso (2 minutos)

### Teste Rápido

```bash
# 1. Ativar ambiente (se não estiver ativo)
source venv/bin/activate

# 2. Colocar um vídeo de teste na pasta
# (copie qualquer vídeo MP4 para a pasta do projeto)

# 3. Transcrever
python transcricao_videos.py \
  --input seu_video.mp4 \
  --output transcricoes/

# 4. Ver resultado
ls transcricoes/
# Você verá: .md (Obsidian), .txt (texto puro), .json (dados completos)
```

---

## 🎯 Casos de Uso Imediatos

### 1. Transcrever Seus Vídeos de 1 Hora

```bash
# Criar pasta para seus vídeos
mkdir meus_videos
mkdir minhas_transcricoes

# Copiar vídeos para meus_videos/

# Transcrever com modelo adequado para português
python transcricao_videos.py \
  --input meus_videos/ \
  --output minhas_transcricoes/ \
  --modelo medium
```

**Tempo estimado:** ~30-40 minutos por vídeo de 1 hora

### 2. Vídeo MUITO Longo (2+ horas)

```bash
# Dividir em partes menores primeiro
python preprocessar_videos.py dividir \
  --input video_longo.mp4 \
  --output chunks/ \
  --duracao 30

# Transcrever as partes
python transcricao_videos.py \
  --input chunks/ \
  --output transcricoes/
```

### 3. Workflow Completo de Produção

```bash
# Use o script pronto!
cd exemplos
./3_workflow_completo.sh

# Ele fará:
# 1. Extrair áudios
# 2. Limpar/normalizar
# 3. Transcrever
# 4. Organizar para Obsidian
```

---

## 📊 Qual Modelo Usar?

| Seus Vídeos | Modelo Recomendado | Comando |
|-------------|-------------------|---------|
| Teste inicial | `base` | `--modelo base` |
| Português (melhor qualidade) | `medium` | `--modelo medium` |
| Inglês ou outros idiomas | `base` ou `small` | `--modelo base` |
| Áudio de baixa qualidade | `medium` ou `large` | `--modelo medium` |

**Recomendação inicial:** Comece com `base` para testar, depois use `medium` para seus vídeos principais.

---

## ⚡ Comandos Que Você Mais Vai Usar

```bash
# Transcrever um vídeo
python transcricao_videos.py -i video.mp4 -o out/

# Transcrever pasta inteira
python transcricao_videos.py -i videos/ -o out/

# Com modelo específico
python transcricao_videos.py -i video.mp4 -o out/ -m medium

# Ver informações de um vídeo
python preprocessar_videos.py info -i video.mp4
```

---

## 🔧 Se Algo Der Errado

### Erro: "FFmpeg not found"

```bash
# Instalar FFmpeg
# Ubuntu/Debian:
sudo apt install ffmpeg

# Mac:
brew install ffmpeg

# Verificar:
ffmpeg -version
```

### Erro: "No module named 'whisper'"

```bash
# Ativar ambiente virtual primeiro
source venv/bin/activate

# Reinstalar dependências
pip install -r requirements.txt
```

### Transcrição com muitos erros

```bash
# Usar modelo maior
python transcricao_videos.py -i video.mp4 -o out/ -m medium

# OU limpar áudio primeiro
python preprocessar_videos.py limpar -i video.mp4 -o limpo/
python transcricao_videos.py -i limpo/ -o out/
```

---

## 📚 Próximos Passos

1. **Leia o README.md** - Visão completa do sistema
2. **Consulte o CHEATSHEET.md** - Comandos rápidos
3. **Explore os exemplos/** - Scripts prontos para usar
4. **Integre com Obsidian** - Copie `.md` para seu vault

---

## 🎯 Workflow Sugerido Para Você

Baseado no seu perfil (INTJ, perfeccionista, organizado):

```bash
# 1. Organizar estrutura
mkdir -p projetos/videos_cursos/{originais,transcricoes}

# 2. Copiar vídeos
cp ~/Downloads/*.mp4 projetos/videos_cursos/originais/

# 3. Transcrever com qualidade
python transcricao_videos.py \
  -i projetos/videos_cursos/originais/ \
  -o projetos/videos_cursos/transcricoes/ \
  -m medium

# 4. Mover para Obsidian
cp projetos/videos_cursos/transcricoes/*.md \
   ~/Obsidian/MeuVault/Aprendizado/Cursos/
```

---

## 💡 Dicas Alinhadas com Sua Essência

### Para Sua "Zona de Genialidade"

Este sistema é **arquitetura da clareza** aplicada:
- ✅ Estrutura bem definida
- ✅ Processos replicáveis
- ✅ Documentação completa
- ✅ Zero desperdício (100% local)
- ✅ Organização otimizada

### Automações Possíveis

```bash
# Criar alias para agilizar
echo "alias transcrever='python ~/transcricao_local/transcricao_videos.py'" >> ~/.bashrc

# Usar:
transcrever -i video.mp4 -o out/
```

### Integração com Seu "Segundo Cérebro"

As transcrições em Markdown são perfeitas para:
- Tags e links no Obsidian
- Busca full-text
- Referências cruzadas
- Sistema Zettelkasten

---

## 📞 Recursos de Suporte

- **GUIA_USO.md** - Troubleshooting completo
- **CHEATSHEET.md** - Referência rápida
- **exemplos/** - Scripts comentados

---

## ✅ Checklist Inicial

- [ ] Executei `./instalar.sh` com sucesso
- [ ] FFmpeg está instalado e funcionando
- [ ] Testei com um vídeo pequeno
- [ ] Explorei os arquivos de exemplo
- [ ] Li o README.md
- [ ] Salvei o CHEATSHEET.md em favoritos

---

## 🎯 Seu Primeiro Objetivo

**Meta:** Transcrever seus primeiros 3 vídeos de 1 hora hoje

1. Coloque os vídeos na pasta `meus_videos/`
2. Execute:
   ```bash
   python transcricao_videos.py -i meus_videos/ -o transcricoes/ -m medium
   ```
3. Enquanto processa (~90-120 min total), explore a documentação
4. Quando terminar, revise as transcrições em `transcricoes/`
5. Copie os `.md` para seu Obsidian

---

## 🚀 Está Pronto!

Você tem agora um sistema completo, profissional e 100% local para transcrever qualquer vídeo.

**Características alinhadas com você:**
- ✅ Controle total (100% local)
- ✅ Zero custos recorrentes
- ✅ Alta qualidade (modelo Medium)
- ✅ Organização impecável
- ✅ Processos documentados
- ✅ Escalável e automatizável

---

**Construído com excelência, para você.**

*Sistema criado por Diego Sottani - Novembro 2025*  
*"Transformando complexidade em clareza"*
