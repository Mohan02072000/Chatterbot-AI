import pyttsx3 
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.trainers import ChatterBotCorpusTrainer


def audio_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Press enter to continue...")
        input()
        print("....////speak now\\\\....")
        a=r.listen(source)

        try:
            s=r.recognize_google(a)
            print(s)
            return s
        except Exception as e:
            print("Exception :",str(e))
            return "nothing"

    

def text_to_audio(msg,i):
    engine=pyttsx3.init()
    v=engine.getProperty('voices')
    engine.setProperty('voice',v[i].id)
    engine.setProperty('rate',180)
    engine.say(msg)
    engine.runAndWait()

def repeater(i):
    r=""
    while(r!="exit"):
        
        text_to_audio("Tell me something.",i)
        print("Listning...........")
        r=audio_to_text()
        text_to_audio("You Said? ",i)

        text_to_audio(r,i)


def init(i):
    r=""
    w=["garbag"]
    text_to_audio("Voice command now active",i)
    while(not(("exit" in w)or("quit" in w)or("stop" in w)or("disable" in w))):
        text_to_audio("Waiting for your command",i)
        print("waiting for your command")
        r=audio_to_text()
        w=word_tokenize(r)
        print(w)
        if(("execute" in w)or("Run" in w)or("start" in w)):
            text_to_audio("Would you like me to run an app?",i)
            print("app ready to run")
        elif(("search" in w)or("browse" in w)or("web" in w)):
            text_to_audio("Do you wanna open browser",i)
            print("web browser initiated.")
        else:
            if(not(("exit" in w)or("quit" in w)or("stop" in w)or("disable" in w))):
                text_to_audio("couldnt figure out what you said.",i)
    
    
    text_to_audio("voice command dissabled",i)   


def ai(i):
    text_to_audio("give me a name first",i)
    print("my name is:")
    n=input()
    print("Do you want to train me?\nInput [y/n]")
    text_to_audio("Have you made any changes in my source code like adding another conversation file or or have edited the existing ones? If so do consider training me ",i)
    t=input()
    bot=ChatBot(n)

    if(t=='y'):
        
        trainer=ChatterBotCorpusTrainer(bot)

        trainer.train("chatterbot.corpus.english")

    q=""
    a=""
    s=""
    while 1:
        
        
        print('You  >>')
        m=input()
        
        r=bot.get_response(m)
        r=str(r)
        w=word_tokenize(m)
        
        print (w)
        if((("My" in w)and("name" in w))or(("call" in w)and("me" in w))):
            
            r=r+" "+n
            print(n,'  >>',r)
            text_to_audio(r,i)
            continue
            

        if(("remember" in w)or("note" in w)or("learn" in w)):
            f=open("C:/Users/LENOVO/programs/Anaconda3/Lib/site-packages/chatterbot_corpus/data/english/custom.yml","a")
            s="\n- - "+q+"\n  - "+a
            f.write(s)
            f.close()
            trainer=ChatterBotCorpusTrainer(bot)
            trainer.train("chatterbot.corpus.english.custom")
        q=a
        a=m
        
        
        print(n,'  >>',r)
        text_to_audio(r,i)
        
        
        if "bye" in word_tokenize(m):
            break

    print("AI Disabled")




print("-----------------------------------------------------------")
print("||||||||||||||||||||||VOICE-COMMAND-PROMPT|||||||||||||||||")
print("-----------------------------------------------------------")
text_to_audio("Set your preferred voice. This can be set only once.",1)
print("Set Voice \n0.For male \n1.For Female")
i=input()
i=int(i)
r=""
text_to_audio("Input your choice. Press 1 for command mode. Press 2 to activate Artificial inteligence. Press 3 to shut me down.",i)
print("input choice \n1.for command mode\n2.activate AI\n3.Terminate program")
c=input()
c=int(c)
while(c!=3):
    if(c==1):
        init(i)
    elif(c==2):
        ai(i)

    elif(c==3):
        break
    else:
        print("wrong command")
        text_to_audio("wrong command punk",i)
    
    text_to_audio("Input your choice. Press 1 for command mode. Press 2 to activate Artificial inteligence. Press 3 to shut me down.",i)
    print("input choice \n1.for command mode\n2.activate AI\n3.Terminate program")

    c=input()
    c=int(c)

    


text_to_audio("Thank you for your time sir. Press enter to quit.",i)
print("Press enter to quit")
print("========================/THANK YOU\========================")
print("===========================================================")
input()



