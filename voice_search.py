import speech_recognition as sr

def search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=3)
        # convert speech to text
        city = r.recognize_google(audio_data)
        # type = str(type).title()
        return city
        
