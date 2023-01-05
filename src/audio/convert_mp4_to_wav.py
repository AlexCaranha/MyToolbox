import ffmpeg

input = "C:\\Temp\\input.mp4"
output = "C:\\Temp\\output.wav"

# Carregue o arquivo de áudio MP4 usando o ffmpeg
stream = ffmpeg.input(input)

# Defina as opções de codificação para o formato WAV
stream = ffmpeg.output(stream, output, acodec='pcm_s16le')

# Execute a conversão
ffmpeg.run(stream)