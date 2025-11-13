#!/usr/bin/env python3
"""
🛠️ Utilitários de Pré-Processamento de Vídeos
Autor: Diego Sottani

Ferramentas para preparar vídeos antes da transcrição:
- Extrair áudio de vídeos
- Limpar e normalizar áudio
- Dividir vídeos longos
- Verificar qualidade do áudio
"""

import os
import subprocess
import argparse
from pathlib import Path
import json


class PreProcessadorVideo:
    """Classe para pré-processar vídeos antes da transcrição"""
    
    EXTENSOES_VIDEO = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm'}
    EXTENSOES_AUDIO = {'.mp3', '.wav', '.m4a', '.flac', '.ogg'}
    
    @staticmethod
    def verificar_ffmpeg():
        """Verifica se FFmpeg está instalado"""
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         capture_output=True, 
                         check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ FFmpeg não encontrado! Instale com:")
            print("   Ubuntu/Debian: sudo apt install ffmpeg")
            print("   Mac: brew install ffmpeg")
            print("   Windows: https://ffmpeg.org/download.html")
            return False
    
    def extrair_audio(self, video_path, output_dir, formato='wav', 
                     sample_rate=16000, mono=True):
        """
        Extrai áudio de vídeo otimizado para Whisper
        
        Args:
            video_path: Caminho do vídeo
            output_dir: Diretório de saída
            formato: Formato do áudio (wav, mp3)
            sample_rate: Taxa de amostragem (16000 Hz é ideal para Whisper)
            mono: Converter para mono (True recomendado)
        """
        if not self.verificar_ffmpeg():
            return False
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            nome_arquivo = Path(video_path).stem
            output_path = os.path.join(output_dir, f"{nome_arquivo}.{formato}")
            
            print(f"🎵 Extraindo áudio de: {os.path.basename(video_path)}")
            
            # Comando FFmpeg
            cmd = [
                'ffmpeg', '-i', video_path,
                '-vn',  # Sem vídeo
                '-ar', str(sample_rate),  # Sample rate
                '-ac', '1' if mono else '2',  # Canais
                '-y',  # Sobrescrever sem perguntar
                output_path
            ]
            
            result = subprocess.run(cmd, 
                                  capture_output=True, 
                                  text=True)
            
            if result.returncode == 0:
                print(f"✅ Áudio extraído: {output_path}")
                return True
            else:
                print(f"❌ Erro ao extrair áudio: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return False
    
    def limpar_audio(self, audio_path, output_dir):
        """
        Limpa e normaliza áudio para melhor transcrição
        
        Aplica:
        - Remoção de ruído de fundo
        - Normalização de volume
        - Filtro passa-alta/passa-baixa
        """
        if not self.verificar_ffmpeg():
            return False
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            nome_arquivo = Path(audio_path).stem
            output_path = os.path.join(output_dir, f"{nome_arquivo}_limpo.wav")
            
            print(f"🧹 Limpando áudio: {os.path.basename(audio_path)}")
            
            # Comando FFmpeg com filtros
            cmd = [
                'ffmpeg', '-i', audio_path,
                '-af', 'highpass=f=200,lowpass=f=3000,loudnorm',
                '-ar', '16000',
                '-ac', '1',
                '-y',
                output_path
            ]
            
            result = subprocess.run(cmd, 
                                  capture_output=True, 
                                  text=True)
            
            if result.returncode == 0:
                print(f"✅ Áudio limpo: {output_path}")
                return True
            else:
                print(f"❌ Erro ao limpar áudio: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return False
    
    def dividir_video(self, video_path, output_dir, duracao_chunk=30):
        """
        Divide vídeo em chunks menores
        
        Args:
            video_path: Caminho do vídeo
            output_dir: Diretório de saída
            duracao_chunk: Duração de cada chunk em minutos
        """
        if not self.verificar_ffmpeg():
            return False
        
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            nome_arquivo = Path(video_path).stem
            output_pattern = os.path.join(output_dir, f"{nome_arquivo}_parte_%03d.mp4")
            
            print(f"✂️  Dividindo vídeo em chunks de {duracao_chunk} minutos")
            
            # Comando FFmpeg
            cmd = [
                'ffmpeg', '-i', video_path,
                '-c', 'copy',
                '-map', '0',
                '-segment_time', f'00:{duracao_chunk:02d}:00',
                '-f', 'segment',
                '-reset_timestamps', '1',
                '-y',
                output_pattern
            ]
            
            result = subprocess.run(cmd, 
                                  capture_output=True, 
                                  text=True)
            
            if result.returncode == 0:
                # Contar quantos arquivos foram criados
                chunks = list(Path(output_dir).glob(f"{nome_arquivo}_parte_*.mp4"))
                print(f"✅ Vídeo dividido em {len(chunks)} partes")
                return True
            else:
                print(f"❌ Erro ao dividir vídeo: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return False
    
    def obter_info_video(self, video_path):
        """
        Obtém informações detalhadas do vídeo
        
        Returns:
            dict: Metadados do vídeo
        """
        if not self.verificar_ffmpeg():
            return None
        
        try:
            cmd = [
                'ffprobe', '-v', 'quiet',
                '-print_format', 'json',
                '-show_format', '-show_streams',
                video_path
            ]
            
            result = subprocess.run(cmd, 
                                  capture_output=True, 
                                  text=True)
            
            if result.returncode == 0:
                info = json.loads(result.stdout)
                
                # Extrair informações relevantes
                formato = info.get('format', {})
                video_stream = next((s for s in info.get('streams', []) 
                                   if s['codec_type'] == 'video'), {})
                audio_stream = next((s for s in info.get('streams', []) 
                                   if s['codec_type'] == 'audio'), {})
                
                metadados = {
                    'arquivo': os.path.basename(video_path),
                    'tamanho_mb': round(int(formato.get('size', 0)) / 1024 / 1024, 2),
                    'duracao_segundos': round(float(formato.get('duration', 0)), 2),
                    'duracao_formatada': self._formatar_duracao(float(formato.get('duration', 0))),
                    'codec_video': video_stream.get('codec_name', 'N/A'),
                    'resolucao': f"{video_stream.get('width', 0)}x{video_stream.get('height', 0)}",
                    'fps': eval(video_stream.get('r_frame_rate', '0/1')),
                    'codec_audio': audio_stream.get('codec_name', 'N/A'),
                    'sample_rate': audio_stream.get('sample_rate', 'N/A'),
                    'canais_audio': audio_stream.get('channels', 'N/A'),
                }
                
                return metadados
            else:
                print(f"❌ Erro ao obter informações: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return None
    
    def _formatar_duracao(self, segundos):
        """Formata segundos em HH:MM:SS"""
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        segs = int(segundos % 60)
        return f"{horas:02d}:{minutos:02d}:{segs:02d}"
    
    def processar_lote(self, input_dir, output_dir, operacao='extrair'):
        """
        Processa múltiplos vídeos em lote
        
        Args:
            input_dir: Diretório com vídeos
            output_dir: Diretório de saída
            operacao: 'extrair', 'limpar', 'dividir', 'info'
        """
        # Buscar vídeos/áudios
        arquivos = []
        extensoes = self.EXTENSOES_VIDEO if operacao != 'limpar' else self.EXTENSOES_AUDIO
        
        for ext in extensoes:
            arquivos.extend(Path(input_dir).glob(f"*{ext}"))
        
        if not arquivos:
            print(f"❌ Nenhum arquivo encontrado em {input_dir}")
            return
        
        print(f"\n{'='*60}")
        print(f"📦 Encontrados {len(arquivos)} arquivos")
        print(f"🔧 Operação: {operacao}")
        print(f"{'='*60}")
        
        sucesso = 0
        
        for i, arquivo in enumerate(arquivos, 1):
            print(f"\n📊 Progresso: {i}/{len(arquivos)}")
            
            if operacao == 'extrair':
                if self.extrair_audio(str(arquivo), output_dir):
                    sucesso += 1
            elif operacao == 'limpar':
                if self.limpar_audio(str(arquivo), output_dir):
                    sucesso += 1
            elif operacao == 'dividir':
                if self.dividir_video(str(arquivo), output_dir):
                    sucesso += 1
            elif operacao == 'info':
                info = self.obter_info_video(str(arquivo))
                if info:
                    print(f"\n📹 {info['arquivo']}")
                    print(f"   Tamanho: {info['tamanho_mb']} MB")
                    print(f"   Duração: {info['duracao_formatada']}")
                    print(f"   Resolução: {info['resolucao']}")
                    print(f"   Áudio: {info['codec_audio']} @ {info['sample_rate']} Hz")
                    sucesso += 1
        
        print(f"\n{'='*60}")
        print(f"✅ {sucesso}/{len(arquivos)} arquivos processados com sucesso")
        print(f"{'='*60}")


def main():
    """Função principal - interface CLI"""
    
    parser = argparse.ArgumentParser(
        description='🛠️ Utilitários de Pré-Processamento de Vídeos',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  # Extrair áudio de vídeo
  python preprocessar_videos.py extrair --input video.mp4 --output audios/

  # Extrair áudio de todos os vídeos
  python preprocessar_videos.py extrair --input pasta_videos/ --output audios/

  # Limpar áudio para melhor transcrição
  python preprocessar_videos.py limpar --input audio.wav --output audios_limpos/

  # Dividir vídeo longo em chunks de 20 minutos
  python preprocessar_videos.py dividir --input video_longo.mp4 --output chunks/ --duracao 20

  # Obter informações de vídeos
  python preprocessar_videos.py info --input video.mp4
        """
    )
    
    parser.add_argument(
        'operacao',
        choices=['extrair', 'limpar', 'dividir', 'info'],
        help='Operação a realizar'
    )
    
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Arquivo ou diretório de entrada'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Diretório de saída (não necessário para "info")'
    )
    
    parser.add_argument(
        '--duracao', '-d',
        type=int,
        default=30,
        help='Duração dos chunks em minutos (apenas para "dividir")'
    )
    
    args = parser.parse_args()
    
    # Validar entrada
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Erro: '{args.input}' não encontrado")
        return
    
    # Validar output para operações que precisam
    if args.operacao != 'info' and not args.output:
        print(f"❌ Erro: --output é obrigatório para operação '{args.operacao}'")
        return
    
    # Inicializar processador
    processador = PreProcessadorVideo()
    
    # Executar operação
    if input_path.is_file():
        # Arquivo único
        if args.operacao == 'extrair':
            processador.extrair_audio(str(input_path), args.output)
        elif args.operacao == 'limpar':
            processador.limpar_audio(str(input_path), args.output)
        elif args.operacao == 'dividir':
            processador.dividir_video(str(input_path), args.output, args.duracao)
        elif args.operacao == 'info':
            info = processador.obter_info_video(str(input_path))
            if info:
                print(f"\n{'='*60}")
                print(f"📹 Informações do Vídeo")
                print(f"{'='*60}")
                for chave, valor in info.items():
                    print(f"{chave}: {valor}")
    else:
        # Diretório (lote)
        if args.operacao == 'info':
            processador.processar_lote(str(input_path), None, args.operacao)
        else:
            processador.processar_lote(str(input_path), args.output, args.operacao)


if __name__ == '__main__':
    main()
