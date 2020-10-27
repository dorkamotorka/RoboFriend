#!/usr/bin/python

import subprocess
import speech_recognition as sr


def speak(text):
    subprocess.call(["espeak", text])

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
	    return None

    return said

if __name__ == '__main__':
	while True:
		text = get_audio()
		if text:
			if "hello" in text:
			    speak("hello, Teo!")
			elif "what is your name" in text:
			    speak("My name is Zumo")
