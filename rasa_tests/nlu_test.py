#!/usr/bin/python3

import subprocess
import os
import speech_recognition as sr
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output



# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak

import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
from rasa_nlu.model import Interpreter
from json import dumps

nlp_interpreter = Interpreter.load("./models/current/nlu")


while True :
    input("Press Enter to speak:  ")
    r = sr.Recognizer()
    with sr.Microphone() as source:     
        #print("Speak: ")
        audio = r.listen(source)        
        try:
            text = r.recognize_google(audio)    
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize your voice")
        
    #inpQuery = str(input(">>  "))
    response_nlp = nlp_interpreter.parse(text)
    print("\n")
    #print(response_nlp)
    
    if response_nlp["intent"]["name"]=="greet":
        a="Hello, How can I help you?"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")

    elif response_nlp["intent"]["name"]=="thankyou":
        a="My pleasure!"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)       
        print(a)
        print("\n")
        
    elif response_nlp["intent"]["name"]=="bye":
        a="Good bye."        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)       
        print(a)
        print("\n")        

    elif response_nlp["intent"]["name"]=="curse_words":
        a="Mind your language, How can you be so rude?"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")        

    elif response_nlp["intent"]["name"]=="love":
        a="This queen doesn’t need a king."        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")

    elif response_nlp["intent"]["name"]=="bored":
        a="How sad?, I will start a game for you."        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a
        print(a)
        execute_unix(c)
        cmd = "ninvaders"
        returned_value = subprocess.check_output(cmd)
        
        print("\n")

    elif response_nlp["intent"]["name"]=="my_name":
        a="I'm Alida"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")
        
    elif response_nlp["intent"]["name"]=="admire":
        a="Siri"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")
        
    elif response_nlp["intent"]["name"]=="my_dob":
        a="I was born on 14 December 2019 and by the way I'm week in math, to say what is my present age."        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        print("\n")
        
    elif response_nlp["intent"]["name"]=="open_settings":
        a="Please wait, Opening Settings"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        cmd = "gnome-control-center"
        returned_value = subprocess.check_output(cmd)
        #print(returned_output.decode("utf-8"))
        print("\n")

    elif response_nlp["intent"]["name"]=="open_filemanager":
        a="Opening File manager"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        cmd = "nautilus"
        returned_value = subprocess.check_output(cmd)
        
        print("\n")        
        
    elif response_nlp["intent"]["name"]=="date_time":
        cmd = "date"
        returned_value = os.system(cmd)
        print(returned_value)
        print("\n")

    elif response_nlp["intent"]["name"]=="dictionary":
        a="Opening Dictionary"        
        c = 'espeak -ven+f5 -k1 -s170 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print(a)
        word = input('Enter word: ')
        def getMeaning(w):
            w = w.lower()
            if w in data:
                return data[w]
            elif len(get_close_matches(w,data.keys())) > 0:
                close_match = get_close_matches(w,data.keys())[0]
                print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
                choice = input()
                choice = choice.lower()
                if choice == 'y':
                    return data[close_match]
                elif choice == 'n':  
                    return "The word doesn't exist. Please double check it."
                else:
                    return "Sorry, We didn't understand your entry."
            else:
                return "The word doesn't exist. Please double check it."
        meaning = getMeaning(word)
        if type(meaning) == list:
            for item in meaning:
                print(item)
        else:
            print(meaning)
        print("\n")        

    elif response_nlp["intent"]["name"]=="person_name":
        page_py = wiki_wiki.page(response_nlp["entities"][0]["value"])
        
        print("\n %s" % page_py.summary.split(". ")[:2])
        print("\n")        

