from openai import OpenAI
import os
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

audio_file= open("/path/to/file/audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)


print(transcription.text)