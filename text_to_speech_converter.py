"""
Author: Jacob Pitsenberger
Program: text_to_speech_converter.py
Version: 1.0
Project: Image Text to Speech Converter
Date: 8/22/2023
Purpose: This program processes an input image, detects text using OCR,
         converts the detected text to speech, and plays the resulting audio before deleting its file.
"""

from gtts import gTTS
from playsound import playsound
import easyocr
import cv2
import numpy as np
import os


class TextToSpeechConverter:
    def __init__(self, img_path: str, target_language: str, gpu: bool = True,
                 confidence_threshold: float = 0.25):
        """
        Initialize the TextToSpeechConverter instance.

        Parameters:
            img_path: Path to the input image.
            target_language: Target language for text-to-speech conversion.
            gpu: Whether to use GPU for text detection.
            confidence_threshold: Confidence threshold for text detection.

        Returns:
            None
        """
        self.img_path = img_path
        self.target_language = target_language
        self.gpu = gpu
        self.confidence_threshold = confidence_threshold

    def read_image(self) -> np.ndarray:
        """
        Read and return the input image.

        Returns:
            np.ndarray: The input image as a NumPy array.
        """
        img = cv2.imread(self.img_path)
        return img

    def detect_text(self, img: np.ndarray) -> str:
        """
        Detect text in the input image and return the detected text.

        Parameters:
            img (np.ndarray): The input image as a NumPy array.

        Returns:
            str: Detected text as a string.
        """
        reader = easyocr.Reader([self.target_language], gpu=self.gpu)
        detected_text = reader.readtext(img)
        text_list = []

        for t in detected_text:
            bbox, text, score = t
            if score > self.confidence_threshold:
                text_list.append(text)

        return ' '.join(text_list)

    def convert_to_speech(self, text: str) -> None:
        """
        Convert the given text to speech and save it as an audio file.

        Parameters:
             text (str): Text to be converted to speech.

        Returns:
            None
        """
        text_converter = gTTS(text=text, lang=self.target_language, slow=False)
        text_converter.save("found_text.mp3")

    @staticmethod
    def play_audio() -> None:
        """
        Play the saved audio file and delete it afterward.
        """
        audio_file_path = 'found_text.mp3'
        playsound(audio_file_path)
        os.remove(audio_file_path)

    def process_image(self) -> None:
        """
        Process the input image: detect text, convert to speech, and play the audio.
        """
        try:
            img = self.read_image()
        except Exception as img_read_error:
            print("Error reading the image:", img_read_error)
            return

        try:
            detected_text = self.detect_text(img)
        except Exception as text_detection_error:
            print("Error detecting text:", text_detection_error)
            return

        try:
            self.convert_to_speech(detected_text)
        except Exception as text_conversion_error:
            print("Error converting text to speech:", text_conversion_error)
            return

        try:
            self.play_audio()
        except Exception as audio_playback_error:
            print("Error playing audio:", audio_playback_error)
            return


if __name__ == "__main__":
    # Dictionary mapping human-readable language names to language codes for text-to-speech conversion.
    languages = {
        'Arabic':   'ar',
        'Bengali':  'bn',
        'English':  'en',
        'French':   'fr',
        'German':   'de',
        'Greek':    'gre',
        'Hebrew':   'he',
        'Hindi':    'hi',
        'Japanese': 'ja',
        'Spanish':  'es',
    }
    # Image paths to detect text from and play as audio.
    english_typed_txt = 'images/english_typed.png'
    english_sign_txt = 'images/english_sign.png'
    spanish_sign_txt = 'images/spanish.png'
    japanese_sign_txt = 'images/japanese.png'
    # Create converter for the image path and language to detect.
    converter = TextToSpeechConverter(english_sign_txt, 'en')
    # Process the image and play it as audio.
    converter.process_image()
