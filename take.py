import bol as b
import speech_recognition as sp
def takecomand():
    t=sp.Recognizer()
    with sp.Microphone() as source:
        print('Sir Harman here i am listening to what you are saying')
        t.pause_threshold=1
        audio=t.listen(source,timeout=1,phrase_time_limit=10)
    try:
        b.speak('recognizing')
        query=t.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        
        print("sir sorry can u say that once again")
        return "None"
    return query