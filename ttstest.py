import pyttsx3
engine = pyttsx3.init()
engine.save_to_file(text='Stay on task, I have my eye on you', filename='nudge.wav')
engine.runAndWait()

import soundfile as sf
import soundcard as sc

default_speaker = sc.default_speaker()
samples, samplerate = sf.read('nudge.wav')
default_speaker.play(samples, samplerate=samplerate)