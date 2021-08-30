import pyttsx3
import speech_recognition as sr

tts = pyttsx3.init() # Initiating text-to-speech
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id) # Change the number for a different voice

def assistant_response(text):
    # Says out loud the text parameter using text-to-speech
    print(text)
    tts.say(text)
    tts.runAndWait()

def listen():
    # Listens microphone and returns detected sound in string format

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)  # Ambient noise adjustment
        print("I am listening...")  # Signals user that Lucy is ready to take requests
        audio = r.listen(source)  # Save audio to a variable
    data = ""
    try:
        data = r.recognize_google(audio)  # Transform audio to string using speech recognition
        print("You said: " + data)  # Print detected sentence
        data = data.lower()  # Lower case detected string for better processing in other functions
        data += ','
    except sr.UnknownValueError:  # If detected audio couldn't be transformed into string
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data