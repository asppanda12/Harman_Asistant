import bol as b
import datetime as d
import take as t
import webbrowser as wb
import wikipedia
import bol as b
import take as t
import pyttsx3
import speech_recognition as sp


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
    
  
# Use male voice 
# function is used to speak
engine.setProperty("rate",80)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecomand():
    t=sp.Recognizer()
    with sp.Microphone() as source:
        print('Sir Harman here i am listening to what you are saying')
        t.pause_threshold=1
        audio=t.listen(source,timeout=1,phrase_time_limit=10)
    
    try:
        speak('recognizing')
        query=t.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        
        print("sir sorry can u say that once again")
        return "None"
    return query

def open(query):
      if 'youtube' in query:
          wb.open('youtube.com')
      elif 'google' in query:
          wb.open('google.com')
      elif 'gyani' in query:
          speak('sir what you want from wiki pedia')
          query1=takecomand()
          res=wikipedia.summary(query)
          speak('DO')
          speak(res)
          print(res)
    

#it is use to wish some one WishMe
def WishMe():
       t=d.datetime.now()
       print(d.datetime.now())
       year=(t.strftime("%Y"))
       month=(t.strftime("%m"))
       day=(t.strftime("%d"))
       hour=(int)(t.strftime("%H"))
       min=(t.strftime("%M"))
       sec=(t.strftime("%S"))
       if(hour>=0 and hour<12):
                      speak("GOOD MORNING SIR ITS HARMAN AND DATE IS {}{}{} AND THE TIME IS {}{} HAVE A GREAT DAY AHEAD".format(day,month,year,hour,min))

        
       else:
                      speak("GOOD EVENING SIR ITS Harman AND DATE IS {}{}{} AND THE TIME IS {}{}{} HAVE A GREAT DAY AHEAD".format(day,month,year,hour,min,sec))



if __name__=="__main__":
    query=takecomand().lower()
    open(query)
    
     

   
    
    
     
    
    
