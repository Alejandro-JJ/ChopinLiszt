import speech_recognition as sr
import pyaudio
import os
import sys

# Suppress ALSA/JACK output
stderr_fd = sys.stderr.fileno()
devnull = os.open(os.devnull, os.O_WRONLY)
old_stderr = os.dup(stderr_fd)
os.dup2(devnull, stderr_fd)


r = sr.Recognizer()
r.pause_threshold = 2        # seconds of silence allowed before stopping
LANG = 'de-DE'
#LANG = 'es-ES'
# List available devices

p = pyaudio.PyAudio()

print("Available audio devices:\n")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Index {i}: {info['name']}, Input Channels: {info['maxInputChannels']}")


# Use device index 0 for your built-in microphone
mic_index = 7

with sr.Microphone(device_index=mic_index) as source:
    print("Say something!")
    audio = r.listen(source, phrase_time_limit=10)#timeout=5, phrase_time_limit=10)

try:
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio, language=LANG))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Request error: {e}")
