import text_to_speech
import speech_to_text
import datetime
import speak
import webbrowser
import weather
import os


user_data=speech_to_text.speech_to_text()

def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is Luca")  
      return "my name is Luca"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey beautiful, How i can  help you !")  
        return "Hey beautiful, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days mam") 
            return "I am doing great these days mam"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure to stay with you sugarplum")
           return "its my pleasure to stay with you sugarplum"      

    elif "good morning" in data_btn:
           speak.speak("Good morning gorgeous, i think you might need some help")
           return "Good morning gorgeous, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 
    
    elif 'remote control car' in data_btn:
         speak.speak("maarenge do thappad, chup chap jaake padhai karo. padhai likhai karna nahi hai aur baith k sirf phone me gaadi gaadi gaadi....ganda bachcha")
         return "maarenge do thappad, chup chap jaake padhai karo. padhai likhai karna nahi hai aur baith k sirf phone me gaadi gaadi gaadi....ganda bachcha"
    
    else :
        speak.speak( "i'm not able to understand!")
        return "i'm not able to understand!"       