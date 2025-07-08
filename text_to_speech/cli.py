import click
import re
from .tts import text_to_speech


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("text")
@click.option("-v", "--voice", default="hm_omega", help="Voice to use.")
@click.option("-l", "--lang", default="en-us", help="Language code.")
@click.option(
    "-o",
    "--output",
    help="Output wav file name. If not provided, it will be generated from the text.",
)
def cli(text, voice, lang, output):
    """Text to speech using Kokoro"""
    if output is None:
        # Generate output filename from text
        # Take the first 8 words, lowercase, replace spaces with hyphens
        slug = "-".join(text.lower().split()[:8])
        # Remove any characters that are not alphanumeric or hyphens
        # and replace multiple hyphens with a single one.
        slug = re.sub(r"[^\w]+", "-", slug)
        output = slug.strip("-") + ".wav"

    text_to_speech(text, voice, lang, output)
