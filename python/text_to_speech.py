import pyttsx3
def text_to_speech(text):
    text="geeks for geeks"
    engine=pyttsx3.init()
    rate= engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()
