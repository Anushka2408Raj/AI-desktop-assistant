import speech_recognition as sr
def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
       print("Adjusting for background noise... Please wait.")
       r.adjust_for_ambient_noise(source, duration=1)  # Reduces noise

       print("Listening... Speak now!")
       audio = r.listen(source, timeout=5)

    try:
       voice_data = r.recognize_google(audio)
       print(voice_data)
       return voice_data
       
    except sr.UnknownValueError:
       print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
       print("Request failed; check your internet connection. Error:", e)
    except sr.WaitTimeoutError:
       print("Listening timed out. Please speak clearly.")



speech_to_text()