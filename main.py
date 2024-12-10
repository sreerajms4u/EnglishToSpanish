import pyttsx3
import googletrans
from deep_translator import GoogleTranslator
from NetHyTech_HindiTTS import Speak

from googletrans import Translator

text = "Estamos autorizados a recopilar información de identificación personal (PII) de usted por las leyes federales y estatales aplicables. Cualquier PII que recopilamos se usa para crear y administrar su cuenta y para comunicarnos con usted sobre su cuenta. La PII también se usa para ayudarlo a solicitar ayuda financiera y/o inscribirse en un plan de salud calificado (QHP) del Mercado. Proteger tu privacidad es muy importante para nosotros. Esta política de privacidad describe qué información recopilamos, por qué la recopilamos y qué hacemos con ella."
# Use any translator you like, in this example GoogleTranslator
#translated = GoogleTranslator(source='auto', target='ml').translate(text)  # output -> Weiter so, du bist großartig

#print(googletrans.LANGUAGES)
translator = Translator()
translated = translator.translate(text)#, src='de', dest='ml')


print(translated)


engine = pyttsx3.init()
#engine.say(translated)
#engine.runAndWait()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#engine.say("getting details of current speaking rate")
#engine.say(translated + str(rate))

#engine.runAndWait()


"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
#engine.save_to_file('Hello World', 'test.mp3')

Speak(translated)
#engine.runAndWait()

engine.stop()
