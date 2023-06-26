import speech_recognition as sr
import pyttsx3
import time
import openai

# Initialize the speech recognition and synthesis engines
r = sr.Recognizer()
engine = pyttsx3.init()
# Replace with your OpenAI API key
openai.api_key = 'OPENAI_API_KEY'


def listen():
    with sr.Microphone() as source:
        # Adjust microphone for ambient noise
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1  # Adjust the pause threshold according to your environment
        audio = r.listen(source, phrase_time_limit=5, timeout=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        print("Sorry, an error occurred while recognizing your speech.")
        return ""


def generate_response(query):
    try:
        response = openai.Completion.create(
            # engine="davinci-codex",
            model="text-davinci-003",
            prompt=query,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            echo=True
        )
        return response.choices[0].text.strip()
    except:
        return "Sorry, an error occurred while generating response."


def speak(response):
    engine.say(response)
    engine.runAndWait()


speak(openai.api_base)


# Main loop
while True:
    # Listen for user input
    query = listen()

    if query:
        # Generate response using ChatGPT
        response = generate_response(query)
        print("ChatGPT:", response)

        # Speak the response
        speak(response)

    # Add a small delay to prevent excessive API requests
    time.sleep(0.5)
