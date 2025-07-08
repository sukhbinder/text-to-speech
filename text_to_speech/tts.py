import sys
import soundfile as sf
from pathlib import Path
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer


def text_to_speech(text, voice, lang, output_file):
    if not Path("kokoro-v1.0.onnx").exists() or not Path("voices-v1.0.bin").exists():
        print(
            "Error: kokoro-v1.0.onnx and voices-v1.0.bin must be in the current directory."
        )
        print("Download with:")
        print(
            "  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx"
        )
        print(
            "  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
        )
        sys.exit(1)

    kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
    tokenizer = Tokenizer()
    phonemes = tokenizer.phonemize(text, lang=lang)
    print(f'Generating speech using voice "{voice}"...')
    samples, sample_rate = kokoro.create(
        phonemes, voice=voice, speed=1.0, lang=lang, is_phonemes=True
    )
    sf.write(output_file, samples, sample_rate)
