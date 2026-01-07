# 🤝 Guia de Contribuição

> Obrigado por considerar contribuir com o Sistema de Transcrição Local!

---

## 🎯 Como Contribuir

### 1. Reportar Bugs

Se encontrar um bug:

1. Verifique se já não foi reportado nas [Issues](../../issues)
2. Abra uma nova Issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Sistema operacional e versão do Python
   - Logs de erro (se houver)

**Template:**
```markdown
## Descrição
[Descreva o bug]

## Como Reproduzir
1. ...
2. ...

## Comportamento Esperado
[O que deveria acontecer]

## Ambiente
- SO: Ubuntu 22.04 / Windows 11 / macOS 13
- Python: 3.12.3
- Whisper: 20231117
```

### 2. Sugerir Melhorias

Tem uma ideia? Ótimo!

1. Abra uma Issue com tag `enhancement`
2. Descreva:
   - O problema que resolve
   - Sua solução proposta
   - Exemplos de uso

### 3. Enviar Pull Request

#### Processo

1. **Fork** o repositório
2. **Clone** seu fork
3. **Crie** uma branch para sua feature: `git checkout -b feature/minha-feature`
4. **Faça** suas alterações
5. **Teste** suas alterações
6. **Commit** com mensagens claras: `git commit -m "feat: adiciona suporte para legenda"`
7. **Push** para seu fork: `git push origin feature/minha-feature`
8. Abra um **Pull Request**

#### Padrões de Código

- **Python:** PEP 8
- **Docstrings:** Google Style
- **Tipos:** Type hints quando possível
- **Comentários:** Em português ou inglês

**Exemplo:**
```python
def transcrever_video(video_path: str, modelo: str = 'base') -> dict:
    """
    Transcreve um vídeo usando Whisper.
    
    Args:
        video_path: Caminho para o arquivo de vídeo
        modelo: Modelo Whisper a usar (tiny, base, small, medium, large)
        
    Returns:
        Dicionário com transcrição e metadados
        
    Raises:
        FileNotFoundError: Se o vídeo não for encontrado
    """
    # Implementação...
```

#### Mensagens de Commit

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, sem mudança de código
- `refactor:` - Refatoração de código
- `test:` - Adicionar/modificar testes
- `chore:` - Manutenção, build, etc.

**Exemplos:**
```bash
git commit -m "feat: adiciona suporte para subtítulos SRT"
git commit -m "fix: corrige erro ao processar vídeos sem áudio"
git commit -m "docs: atualiza README com novos exemplos"
```

---

## 🧪 Testes

Antes de enviar PR:

```bash
# Testar instalação
./instalar.sh

# Testar script principal
python transcrever.py -i teste.mp4 -o out/ -m tiny

# Testar preprocessamento
python preprocessar_videos.py info -i teste.mp4
```

---

## 📝 Documentação

Se adicionar funcionalidade:

1. Atualizar `README.md`
2. Atualizar `CLAUDE.md` (se necessário)
3. Adicionar exemplo em `exemplos/` (se aplicável)

---

## 🎯 Áreas Que Precisam de Ajuda

- [ ] Interface gráfica (GUI)
- [ ] Suporte a mais formatos de saída
- [ ] Otimizações de performance
- [ ] Testes automatizados
- [ ] Integração com outras ferramentas (Notion, etc)
- [ ] Suporte a legendas (SRT, VTT)
- [ ] Análise de sentimentos
- [ ] Sumarização automática

---

## 💡 Ideias de Contribuição

### Fácil
- Adicionar mais exemplos
- Melhorar documentação
- Corrigir typos
- Adicionar badges ao README

### Médio
- Adicionar suporte a novos formatos
- Criar testes unitários
- Melhorar tratamento de erros
- Adicionar progress bar melhor

### Avançado
- Interface gráfica
- API REST
- Integração com serviços externos
- Processamento paralelo

---

## ❓ Dúvidas?

- Abra uma [Issue](../../issues) com tag `question`
- Entre em contato via [discussões](../../discussions)

---

## 🙏 Agradecimentos

Obrigado por contribuir para tornar este projeto melhor!

---

**Desenvolvido com ☕ e 🎯 por Diego Sottani**