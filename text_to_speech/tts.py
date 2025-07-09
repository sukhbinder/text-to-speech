import soundfile as sf
from .common import kokoro_instance, check_models
from kokoro_onnx.tokenizer import Tokenizer


def text_to_speech(text, voice, lang, output_file):
    check_models()
    tokenizer = Tokenizer()
    phonemes = tokenizer.phonemize(text, lang=lang)
    print(f'Generating speech using voice "{voice}"...')
    samples, sample_rate = kokoro_instance.create(
        phonemes, voice=voice, speed=1.0, lang=lang, is_phonemes=True
    )
    sf.write(output_file, samples, sample_rate)
