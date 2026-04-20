import asyncio
import edge_tts

TEXT = "Hey Sanja! Main tumhara AI collaborator hoon. Kya hum manga explanation shuru karein? [shouting] Ye bahut exciting hone wala hai!"
VOICE = "hi-IN-MadhurNeural" # Hindi voice (Male) ya "hi-IN-SwararaNeural" (Female) use kar sakte ho
OUTPUT_FILE = "test_output.mp3"

async def generate_voice():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_voice())
  
