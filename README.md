# text-to-speech

[![PyPI](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/text-to-speech?include_prereleases&label=changelog)](https://github.com/sukhbinder/text-to-speech/releases)
[![Tests](https://github.com/sukhbinder/text-to-speech/actions/workflows/test.yml/badge.svg)](https://github.com/sukhbinder/text-to-speech/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/text-to-speech/blob/master/LICENSE)

Text to speech using Kokoro

## Installation

Install this tool using `pip`:
```bash
pip install text-to-speech
```
## Usage

For help, run:
```bash
txt2speech --help
```
You can also use:
```bash
python -m txt2speech --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd text-to-speech
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
