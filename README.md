# Weather-Reporter
A Voice-Based Weather Assistant built using Python that provides real-time weather updates for any city. It uses the OpenWeatherMap API to fetch live temperature and conditions, and SpeechRecognition with Pyttsx3 for interactive voice responses. A simple yet smart project demonstrating the blend of voice interaction and API integration.


========================
README.md
========================

# Weather Reporter Assistant

This is a beginner-friendly Python desktop assistant that tells you the current weather of any city using voice commands. You speak the city name, and it tells you the temperature and weather description.

## Features
- Get current weather for any city
- Speaks the temperature and weather
- Stop the assistant by saying “exit”
- Beginner-friendly and easy to run

## How to Run
1. Make sure Python (3.9+) is installed
2. Install required libraries:  pip install -r requirements.txt
3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/)  
4. Replace `"YOUR_OPENWEATHERMAP_API_KEY"` in `weather_assistant.py` with your key  
5. Run the assistant:
python weather_assistant.py
6. Speak the city name clearly. Say **exit** to stop.

## Tech Stack
- Python
- SpeechRecognition (for voice input)
- pyttsx3 (for text-to-speech)
- requests (to get weather from API)




========================
requirements.txt
========================

SpeechRecognition
PyAudio
pyttsx3
requests
