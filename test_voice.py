import asyncio
import edge_tts

# Hindi Voices Options:
# hi-IN-MadhurNeural (Male)
# hi-IN-SwararaNeural (Female)

TEXT = "Namaste Sanja! Main manga explanation ke liye taiyaar hoon. Agar video 3 ghante ka hai, toh hume script par mehnat karni hogi. Kya hum shuru karein?"
VOICE = "hi-IN-MadhurNeural"
OUTPUT_FILE = "test_output.mp3"

async def generate_voice():
    # Rate: +10% (Thoda fast, boring na lage)
    # Pitch: -5Hz (Thodi gehri awaaz, mature lagegi)
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="+10%", pitch="-5Hz")
    await communicate.save(OUTPUT_FILE)
    print(f"Audio generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_voice())
    
