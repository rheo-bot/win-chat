import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak("Oho! How was the meeting?")