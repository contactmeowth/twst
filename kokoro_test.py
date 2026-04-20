import os
import urllib.request
from kokoro_onnx import Kokoro
import soundfile as sf

# 1. Models download karne ka function
def download_assets():
    links = {
        "kokoro-v1.0.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx",
        "voices-v1.0.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
    }
    for name, url in links.items():
        if not os.path.exists(name):
            print(f"Downloading {name}...")
            urllib.request.urlretrieve(url, name)

# 2. Main Execution
if __name__ == "__main__":
    download_assets()
    
    # Kokoro initialize
    kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
    
    text = "Namaste Sanja! Ye GitHub Actions se generate kiya gaya pehla fully automated audio hai. Ab hum 30 minute ka manga explanation background mein bana sakte hain."
    
    # Hindi/English mix ke liye 'af_bella' mast hai
    samples, sample_rate = kokoro.create(text, voice="af_bella", speed=1.0, lang="en-us")
    
    sf.write("github_output.wav", samples, sample_rate)
    print("✅ Audio generated: github_output.wav")
    
