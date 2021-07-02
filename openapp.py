import webbrowser as wb
import wikipedia
import bol as b
import take as t
def open(query):
      if 'youtube' in query:
          wb.open('youtube.com')
      elif 'google' in query:
          wb.open('google.com')
      elif 'gyani' in query:
          b.speak('sir what you want from wiki pedia')
          query1=t.takecomand()
          res=wikipedia.summary(query)
          b.speak('DO')
          b.speak(res)
          b.print(res)
    

          



