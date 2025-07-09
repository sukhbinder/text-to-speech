import sys
from pathlib import Path
from kokoro_onnx import Kokoro

# The script is in text_to_speech/, and the models are in the parent directory.
project_root = Path(__file__).resolve().parent.parent
KOKORO_MODEL = project_root / "kokoro-v1.0.onnx"
VOICES_MODEL = project_root / "voices-v1.0.bin"

kokoro_instance = None
voices = []

try:
    if KOKORO_MODEL.exists() and VOICES_MODEL.exists():
        kokoro_instance = Kokoro(str(KOKORO_MODEL), str(VOICES_MODEL))
        voices = list(kokoro_instance.get_voices())
except Exception as e:
    # Silently fail, so CLI can still be used for --help
    # The error will be properly handled in text_to_speech
    pass


def check_models():
    """Checks if the models exist and prints an error message if they don't."""
    if not kokoro_instance:
        print(
            f"Error: Could not load Kokoro models. Make sure {KOKORO_MODEL.name} and {VOICES_MODEL.name} are in the project root directory: {project_root}"
        )
        print("You can download them from:")
        print(
            f"  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/{KOKORO_MODEL.name}"
        )
        print(
            f"  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/{VOICES_MODEL.name}"
        )
        sys.exit(1)
