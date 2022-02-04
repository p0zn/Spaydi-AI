import speech_recognition as sr
import pyttsx3
import random

recognizer=sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga")
engine.say("Merhaba lordum")
engine.say("Spaydi emirlerinizi dinliyor. Size nasıl yardımcı olabilirim.")
engine.runAndWait()  

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source,duration=0.1) 
            print("Spaydi Dinliyor : ")
            voice= recognizer.listen(source)
            command = recognizer.recognize_google(voice, language="tr-TR,en-ENG")
            command = command.lower()
            print(command)

            spidey_names = ("spidey","speedy","spaydi","spaydır","spaydo","spidi","spider")
            for name in spidey_names:
                if name in command:
                    engine.say("Emredin Lordum")
                    engine.runAndWait()
                    break
            if 'nasılsın' in command:
                list1 = ["iyiyim","keyfim yok","mutsuzum","neşeliyim","halsizim","canım sıkılıyor","oyun oynamak istiyorum"]
                engine.say(random.choice(list1)  + "lordum")
                engine.runAndWait() 
            if 'mutsuzsun' in command:
                engine.say("Lordum inanın neden mutsuz olduğumu bilmiyorum")
                engine.runAndWait()
            
           
    except:
        engine.say("Maalesef dediğinizi anlamadım lordum. Henüz öğrenme aşamasındayım. Sizden çok özür dilerim.")
        engine.runAndWait()

  
    