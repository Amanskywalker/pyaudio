#!/usr/bin/env python
import sys, os, pyaudio
import speech_recognition as sr

# obtain audio from the microphone
#Recognizer(language = "en-US")
r = sr.Recognizer()
with sr.Microphone(5) as source:
    print("Say something!")
	#r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source, 5)

# recognize speech
try:
    print("I thinks you said " + r.recognize(audio))
except sr.UnknownValueError:
    print("I could not understand audio")
except sr.RequestError as e:
    print("Error; {0}".format(e))

# write audio to a RAW file
with open("microphone-results.raw", "wb") as f:
    f.write(audio.get_raw_data())

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# write audio to an AIFF file
with open("microphone-results.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# write audio to a FLAC file
with open("microphone-results.flac", "wb") as f:
    f.write(audio.get_flac_data())

'''

import pyaudio
import sphinx
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
 	audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

try:
 f=open('myfile.txt','w')
 f.write(r.recognize_google(audio))
 f.close()
except LookupError:
 print("Could not understand audio")
 '''
