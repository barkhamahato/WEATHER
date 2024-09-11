#pip install pyttsx3
import webbrowser
import pyttsx3

#--------speech setup----------------------------------------

#------------------------------------------------------------

def talk(audio):
    engine = pyttsx3.init()

    voice= engine.getProperty('voices') #getting details of current voice

    engine.setProperty('voice', voice[1].id)
    engine.setProperty('rate',150)
    engine.say(audio) 

    engine.runAndWait() 
#----------------------------------------------------------------

# Function to Generate Report
def forecast(C):
    text_val = 'Here is the weather forecast upto 3 days of '+ str(C) +' city'  
    
    talk(text_val) 
    webbrowser.open('https://wttr.in/{}'.format(C),new=0, autoraise=True)
    
