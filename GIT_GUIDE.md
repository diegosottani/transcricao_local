# 🚀 Guia Git Para o Projeto

> **Comandos prontos para inicializar e gerenciar seu repositório**

---

## 📦 Inicialização do Repositório

### Opção 1: Criar Repositório Local e Depois Subir para GitHub

```bash
# 1. Ir para a pasta do projeto
cd ~/dev/transcricao_local

# 2. Inicializar Git
git init

# 3. Adicionar todos os arquivos (o .gitignore vai filtrar o que não deve ir)
git add .

# 4. Primeiro commit
git commit -m "feat: sistema inicial de transcrição local de vídeos

- Script principal de transcrição com Whisper
- Utilitários de pré-processamento
- Documentação completa
- Scripts de exemplo
- Instalador automatizado"

# 5. Criar repositório no GitHub primeiro (https://github.com/new)
#    Nome sugerido: transcricao-local ou video-transcription-local

# 6. Conectar com o repositório remoto (substituir USER pelo seu usuário)
git remote add origin https://github.com/USER/transcricao-local.git

# 7. Subir para GitHub
git branch -M main
git push -u origin main
```

### Opção 2: Clonar de um Repositório Existente

```bash
# Se você já criou o repo no GitHub
git clone https://github.com/USER/transcricao-local.git
cd transcricao-local

# Copiar seus arquivos para dentro
# Depois fazer commit
git add .
git commit -m "feat: adiciona sistema de transcrição"
git push
```

---

## 🔄 Workflow Diário

### Verificar Status

```bash
# Ver o que mudou
git status

# Ver diferenças detalhadas
git diff

# Ver histórico de commits
git log --oneline --graph
```

### Adicionar Mudanças

```bash
# Adicionar arquivo específico
git add transcricao_videos.py

# Adicionar todos os arquivos modificados
git add .

# Adicionar interativamente (escolher o que commitar)
git add -p
```

### Fazer Commit

```bash
# Commit simples
git commit -m "fix: corrige erro ao processar vídeos sem áudio"

# Commit com descrição longa
git commit -m "feat: adiciona suporte para subtítulos

- Implementa geração de SRT
- Implementa geração de VTT
- Adiciona timestamps precisos
- Atualiza documentação"

# Alterar último commit (se ainda não fez push)
git commit --amend
```

### Enviar para GitHub

```bash
# Enviar branch atual
git push

# Enviar branch específica
git push origin main

# Forçar push (use com cuidado!)
git push -f origin main
```

---

## 🌿 Trabalhando com Branches

### Criar e Usar Branches

```bash
# Criar nova branch
git checkout -b feature/gui

# Listar branches
git branch

# Mudar de branch
git checkout main

# Criar branch e fazer checkout
git checkout -b fix/audio-processing
```

### Merge de Branches

```bash
# Ir para branch principal
git checkout main

# Fazer merge de outra branch
git merge feature/gui

# Deletar branch após merge
git branch -d feature/gui
```

---

## 🔄 Sincronizar com GitHub

### Atualizar Repositório Local

```bash
# Baixar mudanças
git fetch origin

# Baixar e aplicar mudanças
git pull origin main

# Pull com rebase (mantém histórico linear)
git pull --rebase origin main
```

---

## 🎯 Comandos Específicos Para Este Projeto

### Ignorar Arquivos Já Commitados

```bash
# Se você já commitou vídeos/transcrições por engano:

# Remover da staging, mas manter no disco
git rm --cached transcricoes/*.txt
git rm --cached videos/*.mp4

# Remover pasta inteira
git rm -r --cached transcricoes/

# Commit a remoção
git commit -m "chore: remove arquivos de transcrição do git"
git push
```

### Limpar Cache do Git

```bash
# Se o .gitignore não está funcionando para arquivos já rastreados
git rm -r --cached .
git add .
git commit -m "chore: atualiza .gitignore e limpa cache"
```

### Verificar o Que Vai Ser Commitado

```bash
# Ver arquivos staged
git diff --cached

# Ver tamanho do que será commitado
git diff --cached --stat
```

---

## 🚫 Desfazer Mudanças

### Antes do Commit

```bash
# Descartar mudanças em arquivo específico
git checkout -- transcricao_videos.py

# Descartar todas as mudanças não commitadas
git reset --hard HEAD

# Remover arquivo da staging area
git reset HEAD transcricao_videos.py
```

### Depois do Commit

```bash
# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Desfazer último commit (descarta mudanças)
git reset --hard HEAD~1

# Reverter commit específico (cria novo commit)
git revert abc123
```

---

## 🏷️ Tags e Releases

### Criar Tags

```bash
# Tag simples
git tag v1.0.0

# Tag anotada (recomendado)
git tag -a v1.0.0 -m "Versão 1.0.0 - Release inicial"

# Ver tags
git tag

# Enviar tags para GitHub
git push origin v1.0.0

# Enviar todas as tags
git push origin --tags
```

---

## 🔍 Inspecionar e Buscar

### Histórico

```bash
# Ver histórico completo
git log

# Ver histórico resumido
git log --oneline --graph --all

# Ver mudanças em arquivo específico
git log -p transcricao_videos.py

# Buscar por texto nos commits
git log --grep="transcrição"

# Buscar por autor
git log --author="Diego"
```

### Buscar no Código

```bash
# Buscar texto em todos os arquivos
git grep "whisper"

# Buscar em commit específico
git grep "whisper" v1.0.0
```

---

## 🛠️ Configuração

### Configuração Inicial

```bash
# Configurar nome e email (se ainda não fez)
git config --global user.name "Diego Sottani"
git config --global user.email "seu.email@example.com"

# Configurar editor padrão
git config --global core.editor "vim"

# Ver configurações
git config --list
```

### Aliases Úteis

```bash
# Criar atalhos
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --oneline --graph --all --decorate'

# Usar aliases
git st           # = git status
git visual       # = git log --oneline --graph --all --decorate
```

---

## 📊 Estatísticas do Repositório

```bash
# Contar commits por autor
git shortlog -sn

# Ver tamanho do repositório
git count-objects -vH

# Ver arquivos maiores
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | awk '/^blob/ {print substr($0,6)}' | sort --numeric-sort --key=2 | tail -n 10
```

---

## 🔐 Autenticação GitHub

### HTTPS com Token

```bash
# Quando pedir senha, usar Personal Access Token do GitHub
# Criar em: https://github.com/settings/tokens

# Cache de credenciais (Linux)
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'

# Store de credenciais (salva permanentemente)
git config --global credential.helper store
```

### SSH (Recomendado)

```bash
# 1. Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@example.com"

# 2. Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# 3. Adicionar no GitHub: https://github.com/settings/ssh/new

# 4. Testar conexão
ssh -T git@github.com

# 5. Mudar remote para SSH
git remote set-url origin git@github.com:USER/transcricao-local.git
```

---

## ⚠️ Avisos Importantes Para Este Projeto

### ❌ NUNCA Commitar

```bash
# Estes arquivos são ignorados pelo .gitignore, mas cuidado:
- Vídeos (*.mp4, *.avi, etc) - podem ser MUITO grandes
- Áudios (*.mp3, *.wav, etc)
- Transcrições (podem ser muitas)
- Pasta venv/ (ambiente virtual)
- Modelos Whisper baixados (*.pt)
```

### ✅ SEMPRE Commitar

```bash
# Estes arquivos SÃO importantes:
- transcricao_videos.py
- preprocessar_videos.py
- requirements.txt
- README.md e documentação
- .gitignore
- exemplos/
```

---

## 🎯 Workflow Recomendado Para Você

### Desenvolvimento Normal

```bash
# 1. Fazer mudanças
vim transcricao_videos.py

# 2. Testar
python transcricao_videos.py -i teste.mp4 -o out/ -m tiny

# 3. Verificar o que mudou
git status
git diff

# 4. Commitar
git add transcricao_videos.py
git commit -m "feat: adiciona suporte para legendas SRT"

# 5. Enviar para GitHub
git push
```

### Nova Feature Grande

```bash
# 1. Criar branch
git checkout -b feature/interface-grafica

# 2. Desenvolver e commitar
git add .
git commit -m "feat: adiciona interface gráfica básica"

# 3. Mais commits...
git commit -m "feat: adiciona seleção de modelo na GUI"

# 4. Voltar para main e fazer merge
git checkout main
git merge feature/interface-grafica

# 5. Push
git push
```

---

## 🆘 Comandos de Emergência

```bash
# Salvou mudanças não commitadas temporariamente
git stash

# Recuperar mudanças salvas
git stash pop

# Voltar arquivo para versão anterior
git checkout HEAD -- arquivo.py

# Desfazer tudo desde último commit
git reset --hard HEAD

# Ver o que foi deletado
git log --diff-filter=D --summary
```

---

## 📚 Resumo dos Comandos Mais Usados

```bash
# Setup inicial
git init
git add .
git commit -m "feat: commit inicial"
git remote add origin https://github.com/USER/repo.git
git push -u origin main

# Workflow diário
git status                    # Ver mudanças
git add .                     # Adicionar tudo
git commit -m "mensagem"      # Commitar
git push                      # Enviar para GitHub

# Sincronizar
git pull                      # Baixar mudanças

# Branches
git checkout -b nova-branch   # Criar e mudar
git checkout main             # Voltar para main
git merge outra-branch        # Merge
```

---

**💡 Dica:** Commite frequentemente com mensagens claras. É melhor muitos commits pequenos do que um commit gigante!

---

*Guia Git criado por Diego Sottani - 2025*