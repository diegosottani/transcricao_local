#!/usr/bin/env python3
"""
🎯 Sistema de Transcrição Local de Vídeos
Autor: Diego Sottani
Descrição: Transcreve vídeos longos usando Whisper local, com timestamps e formatação para Obsidian

Uso:
    python transcricao_videos.py --input pasta_videos --output pasta_saida --modelo base
"""

import whisper
import os
import argparse
from pathlib import Path
from datetime import datetime, timedelta
import json


class TranscritorVideos:
    """Classe para gerenciar transcrição de vídeos com Whisper"""
    
    MODELOS_DISPONIVEIS = {
        'tiny': '39MB - Mais rápido, menos preciso',
        'base': '74MB - Bom equilíbrio (RECOMENDADO)',
        'small': '244MB - Melhor precisão',
        'medium': '769MB - Excelente para português',
        'large': '1550MB - Máxima precisão'
    }
    
    EXTENSOES_VIDEO = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm'}
    
    def __init__(self, modelo='base', idioma='pt'):
        """
        Inicializa o transcritor
        
        Args:
            modelo: Nome do modelo Whisper a usar
            idioma: Código do idioma (pt, en, es, etc)
        """
        self.idioma = idioma
        print(f"🔄 Carregando modelo Whisper '{modelo}'...")
        self.model = whisper.load_model(modelo)
        print(f"✅ Modelo carregado com sucesso!")
        
    def _formatar_timestamp(self, segundos):
        """Converte segundos em formato HH:MM:SS"""
        return str(timedelta(seconds=int(segundos)))
    
    def _gerar_metadados(self, video_path, result):
        """Gera dicionário de metadados da transcrição"""
        return {
            'arquivo': os.path.basename(video_path),
            'data_transcricao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'duracao_video': self._formatar_timestamp(result['segments'][-1]['end']),
            'idioma_detectado': result.get('language', self.idioma),
            'total_segmentos': len(result['segments']),
            'modelo_usado': self.model.__class__.__name__
        }
    
    def _gerar_markdown(self, video_path, result, metadados):
        """Gera arquivo markdown formatado para Obsidian"""
        nome_arquivo = Path(video_path).stem
        
        markdown = f"""# 📹 {nome_arquivo}

---

## 📊 Metadados

| Campo | Valor |
|-------|-------|
| **Arquivo Original** | `{metadados['arquivo']}` |
| **Data Transcrição** | {metadados['data_transcricao']} |
| **Duração** | {metadados['duracao_video']} |
| **Idioma** | {metadados['idioma_detectado']} |
| **Segmentos** | {metadados['total_segmentos']} |
| **Modelo** | {metadados['modelo_usado']} |

---

## 📝 Transcrição Completa

{result['text']}

---

## ⏱️ Transcrição com Timestamps

"""
        # Adicionar segmentos com timestamps
        for segment in result['segments']:
            inicio = self._formatar_timestamp(segment['start'])
            fim = self._formatar_timestamp(segment['end'])
            texto = segment['text'].strip()
            markdown += f"**[{inicio} → {fim}]**\n{texto}\n\n"
        
        # Adicionar tags e links
        markdown += f"""---

## 🏷️ Tags

#transcricao #video #whisper

---

## 🔗 Links Relacionados

- [[Index de Vídeos]]
- [[{nome_arquivo}]]

---

*Transcrição gerada automaticamente por Whisper Local*
*Sistema criado por Diego Sottani - {datetime.now().year}*
"""
        
        return markdown
    
    def transcrever_video(self, video_path, output_dir):
        """
        Transcreve um único vídeo
        
        Args:
            video_path: Caminho do vídeo
            output_dir: Diretório para salvar transcrições
            
        Returns:
            bool: True se sucesso, False se erro
        """
        try:
            nome_arquivo = Path(video_path).stem
            print(f"\n{'='*60}")
            print(f"🎬 Processando: {os.path.basename(video_path)}")
            print(f"{'='*60}")
            
            # Transcrever
            print(f"🔄 Transcrevendo... (pode demorar alguns minutos)")
            result = self.model.transcribe(
                video_path, 
                language=self.idioma,
                verbose=False  # Menos output durante transcrição
            )
            
            # Gerar metadados
            metadados = self._gerar_metadados(video_path, result)
            
            # Criar diretório de saída se não existir
            os.makedirs(output_dir, exist_ok=True)
            
            # Salvar arquivos
            # 1. Markdown formatado
            md_path = os.path.join(output_dir, f"{nome_arquivo}.md")
            markdown = self._gerar_markdown(video_path, result, metadados)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"✅ Markdown salvo: {md_path}")
            
            # 2. Texto puro
            txt_path = os.path.join(output_dir, f"{nome_arquivo}.txt")
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            print(f"✅ Texto puro salvo: {txt_path}")
            
            # 3. JSON com dados completos
            json_path = os.path.join(output_dir, f"{nome_arquivo}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'metadados': metadados,
                    'texto_completo': result['text'],
                    'segmentos': result['segments']
                }, f, ensure_ascii=False, indent=2)
            print(f"✅ JSON salvo: {json_path}")
            
            print(f"\n✨ Transcrição concluída com sucesso!")
            print(f"📄 {len(result['segments'])} segmentos transcritos")
            print(f"⏱️  Duração: {metadados['duracao_video']}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao transcrever {video_path}: {str(e)}")
            return False
    
    def transcrever_lote(self, input_dir, output_dir):
        """
        Transcreve todos os vídeos de um diretório
        
        Args:
            input_dir: Diretório com vídeos
            output_dir: Diretório para salvar transcrições
        """
        # Buscar vídeos
        videos = []
        for ext in self.EXTENSOES_VIDEO:
            videos.extend(Path(input_dir).glob(f"*{ext}"))
        
        if not videos:
            print(f"❌ Nenhum vídeo encontrado em {input_dir}")
            return
        
        print(f"\n{'='*60}")
        print(f"🎯 Encontrados {len(videos)} vídeos para transcrever")
        print(f"{'='*60}")
        
        # Processar cada vídeo
        sucesso = 0
        falhas = 0
        
        for i, video in enumerate(videos, 1):
            print(f"\n📊 Progresso: {i}/{len(videos)}")
            if self.transcrever_video(str(video), output_dir):
                sucesso += 1
            else:
                falhas += 1
        
        # Resumo final
        print(f"\n{'='*60}")
        print(f"🏁 PROCESSAMENTO CONCLUÍDO")
        print(f"{'='*60}")
        print(f"✅ Sucessos: {sucesso}")
        print(f"❌ Falhas: {falhas}")
        print(f"📁 Transcrições salvas em: {output_dir}")


def main():
    """Função principal - interface CLI"""
    
    parser = argparse.ArgumentParser(
        description='🎯 Sistema de Transcrição Local de Vídeos com Whisper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  # Transcrever um único vídeo
  python transcricao_videos.py --input video.mp4 --output transcricoes/

  # Transcrever todos os vídeos de uma pasta
  python transcricao_videos.py --input pasta_videos/ --output transcricoes/

  # Usar modelo mais preciso
  python transcricao_videos.py --input video.mp4 --output transcricoes/ --modelo medium

  # Transcrever em inglês
  python transcricao_videos.py --input video.mp4 --output transcricoes/ --idioma en

Modelos disponíveis:
  tiny   - 39MB  - Mais rápido, menos preciso
  base   - 74MB  - Bom equilíbrio (RECOMENDADO)
  small  - 244MB - Melhor precisão
  medium - 769MB - Excelente para português
  large  - 1550MB- Máxima precisão
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Arquivo de vídeo ou diretório com vídeos'
    )
    
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Diretório para salvar transcrições'
    )
    
    parser.add_argument(
        '--modelo', '-m',
        default='base',
        choices=['tiny', 'base', 'small', 'medium', 'large'],
        help='Modelo Whisper a usar (padrão: base)'
    )
    
    parser.add_argument(
        '--idioma', '-l',
        default='pt',
        help='Código do idioma (pt, en, es, etc. - padrão: pt)'
    )
    
    args = parser.parse_args()
    
    # Validar entrada
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Erro: '{args.input}' não encontrado")
        return
    
    # Inicializar transcritor
    transcritor = TranscritorVideos(modelo=args.modelo, idioma=args.idioma)
    
    # Processar
    if input_path.is_file():
        # Arquivo único
        transcritor.transcrever_video(str(input_path), args.output)
    else:
        # Diretório (lote)
        transcritor.transcrever_lote(str(input_path), args.output)


if __name__ == '__main__':
    main()
