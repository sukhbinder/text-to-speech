import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
import numpy as np

from text_to_speech import cli
from text_to_speech import tts

# Mock data
MOCK_SAMPLES = np.array([0.1, 0.2, 0.3])
MOCK_SAMPLE_RATE = 16000

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_generates_output_filename(runner):
    """Test that the CLI generates a correct output filename from the text."""
    with patch('text_to_speech.cli.text_to_speech') as mock_tts:
        result = runner.invoke(cli.cli, ["Hello world, this is a test."])
        assert result.exit_code == 0
        # Expected filename: hello-world-this-is-a-test.wav (takes first 8 words)
        expected_filename = "hello-world-this-is-a-test.wav"
        mock_tts.assert_called_once_with(
            "Hello world, this is a test.", "hm_omega", "en-us", expected_filename
        )

def test_cli_uses_provided_output_filename(runner):
    """Test that the CLI uses the user-provided output filename."""
    with patch('text_to_speech.cli.text_to_speech') as mock_tts:
        result = runner.invoke(cli.cli, ["Hello", "--output", "my-file.wav"])
        assert result.exit_code == 0
        mock_tts.assert_called_once_with(
            "Hello", "hm_omega", "en-us", "my-file.wav"
        )

@patch('pathlib.Path.exists', return_value=False)
def test_text_to_speech_missing_model_files(mock_path_exists):
    """Test that text_to_speech exits if model files are missing."""
    with pytest.raises(SystemExit) as e:
        tts.text_to_speech("test", "voice", "lang", "out.wav")
    assert e.type == SystemExit
    assert e.value.code == 1