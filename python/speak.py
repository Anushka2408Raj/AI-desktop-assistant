from gtts import gTTS
import os
import playsound
import uuid

def speak(text, lang='hi'):
    try:
        # Generate a unique filename for each voice output
        filename = f"temp_{uuid.uuid4()}.mp3"

        # Convert text to speech
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)

        # Play the generated speech
        playsound.playsound(filename)

        # Remove the temporary file after playing
        os.remove(filename)

    except Exception as e:
        print("❌ Error in speaking:", e)
