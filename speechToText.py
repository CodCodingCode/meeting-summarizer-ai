from openai import OpenAI
import os
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

audio_file= open("/Users/owner/Documents/GitHub/meeting-summarizer-ai/downloaded_file.mp3", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

# Summarize the transcription

message = [
    {"role": "system", "content": f"Summarize the transcription {transcription.text}"}
]

stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = message,
        stream = True, 
        max_tokens=100,
        temperature=0.1,
)


reply = ""
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
    reply += chunk.choices[0].delta.content or ""
print()