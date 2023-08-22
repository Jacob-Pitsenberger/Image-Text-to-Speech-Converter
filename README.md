# Text to Speech Converter

Author: Jacob Pitsenberger  
Version: 1.0  
Date: 8/21/2023  

## Description

This Python script processes an input image, detects text using Optical Character Recognition (OCR), converts the detected text to speech, and plays the resulting audio. It demonstrates how to use the `gtts` (Google Text-to-Speech) and `easyocr` libraries to accomplish these tasks.

## Prerequisites

Before using this script, ensure you have the required libraries installed:

- `gtts` (Google Text-to-Speech): Used to convert text to speech and generate audio files.
- `playsound`: Used to play audio files.
- `easyocr`: Used for text detection using Optical Character Recognition (OCR).
- `cv2` (OpenCV): Used for reading and processing images.

You can install the required libraries using the following command:

```bash
pip install gtts playsound easyocr opencv-python
```

## Usage

1. Place the input image in the 'images' directory.
2. Modify the `image_path` and `target_language` variables in the `__main__` block of the script to match your image and language preferences.
3. Run the script using the following command:

```bash
python text_to_speech_converter.py
```

## Supported Languages

The script contains a dictionary that supports text-to-speech conversion for the following languages:

- Arabic (ar)
- Bengali (bn)
- English (en)
- French (fr)
- German (de)
- Greek (gre)
- Hebrew (he)
- Hindi (hi)
- Japanese (ja)
- Spanish (es)

To change the target language, update the `target_language` variable in the `__main__` block.
Note, other target languages supported by easyOCR can be used by specifying the target language with its respective language code.

## License

This project is licensed under the [MIT License](LICENSE).
