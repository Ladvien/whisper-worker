import os
import numpy as np
import speech_recognition as sr
import whisper
import torch
from rich import print
import logging

from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform

from src import Settings
from src.recording_device import RecordingDevice
from src.whisper_worker import WhisperWorker


def transcription_callback(data: str):
    print(data)


def main():
    args = Settings.load("settings.yaml")
    logging.info("Using settings: ")
    logging.info(args)

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    print(args)
    recording_device = RecordingDevice(args.mic_settings)
    whisper_worker = WhisperWorker(
        args.whisper_worker,
        recording_device,
    )

    transcription = [""]

    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    whisper_worker.listen(transcription_callback)

    print("\n\nTranscription:")

    for line in transcription:
        print(line)


if __name__ == "__main__":
    main()
