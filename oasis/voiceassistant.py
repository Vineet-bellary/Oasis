import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return None

def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        
        if command is None:
            continue
        
        if "hello" in command:
            speak("Hello! How can I help you?")
        
        elif "time" in command:
            now = datetime.datetime.now()
            speak(f"The current time is {now.strftime('%H:%M:%S')}")
        
        elif "date" in command:
            today = datetime.date.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}")
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
        
        elif "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
