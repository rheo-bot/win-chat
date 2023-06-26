import speech_recognition as sr

def listen_microphone():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)  # Adjust microphone for ambient noise
        print("Listening...")

        while True:
            try:
                audio = r.listen(source)
                print("recongnizing...")
                text = r.recognize_google(audio)  # Perform speech recognition using Google Speech Recognition API
                print("You said:", text)
            except sr.UnknownValueError:
                print("Unable to recognize speech")
            except sr.RequestError:
                print("Request failed due to network issues")

# Usage example
listen_microphone()