import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import os
from dotenv import load_dotenv
import threading

# Load environment variables
load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")


def convert_audio_to_wav(file_path: str) -> str:
    """
    Converts an MP3 file to WAV format with PCM encoding, 16kHz, mono channel.
    Returns the path to the converted WAV file.
    """
    wav_file_path = file_path.replace(".mp3", ".wav")
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export(wav_file_path, format="wav")
    return wav_file_path


def transcribe_speech_from_file(file_path: str, language: str = "en-US") -> str:
    """
    Transcribes speech from an audio file using Azure Speech Service.
    Handles long audio using continuous recognition.
    """
    try:
        # Convert MP3 to WAV if needed
        if file_path.endswith(".mp3"):
            file_path = convert_audio_to_wav(file_path)

        # Configure the speech recognizer
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        speech_config.speech_recognition_language = language
        audio_config = speechsdk.audio.AudioConfig(filename=file_path)
        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # List to store transcription results
        all_results = []
        done = threading.Event()

        def handle_result(evt):
            if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                all_results.append(evt.result.text)
            elif evt.result.reason == speechsdk.ResultReason.Canceled:
                print(f"Recognition canceled: {evt.result.cancellation_details.reason}")

        def stop_recognition(evt):
            print("Recognition stopped.")
            done.set()

        recognizer.recognized.connect(handle_result)
        recognizer.session_stopped.connect(stop_recognition)
        recognizer.canceled.connect(stop_recognition)

        # Start recognition
        recognizer.start_continuous_recognition()
        done.wait()  # Wait for recognition to finish
        recognizer.stop_continuous_recognition()

        return " ".join(all_results) if all_results else "No transcription available."

    except Exception as e:
        return f"Error: {e}"
