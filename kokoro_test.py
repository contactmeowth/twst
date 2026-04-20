import os
import urllib.request
from kokoro_onnx import Kokoro
import soundfile as sf

def download_assets():
    links = {
        "kokoro-v1.0.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx",
        "voices-v1.0.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
    }
    for name, url in links.items():
        if not os.path.exists(name):
            print(f"Downloading {name}...")
            urllib.request.urlretrieve(url, name)

if __name__ == "__main__":
    download_assets()
    kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
    
    # script.txt se content padhna
    with open("script.txt", "r") as f:
        full_script = f.read()
    
    # English voice 'af_bella' use kar rahe hain
    samples, sample_rate = kokoro.create(
        full_script, 
        voice="af_bella", 
        speed=1.0, 
        lang="en-us"
    )
    
    sf.write("manga_recap_english.wav", samples, sample_rate)
    print("✅ English Audio Generated!")
    
