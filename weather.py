import requests
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for city name")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Please repeat.")
            return ""
        except sr.RequestError:
            print("Connection error.")
            return ""
        return command.lower()

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temp}°C with {desc}.")
    else:
        speak(f"Sorry, I couldn't find weather for {city}.")

def run_weather_assistant():
    speak("Hello! I can give you weather updates. Say 'exit' to stop.")
    while True:
        speak("Please tell me the city name.")
        city = listen_command()
        if city == "" or city == "exit":
            speak("Stopping Weather Reporter.")
            break
        get_weather(city)

if __name__ == "__main__":
    run_weather_assistant()
