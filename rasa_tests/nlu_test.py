#!/usr/bin/python3

import subprocess

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
    inpQuery = str(input(">>  "))
    response_nlp = nlp_interpreter.parse(inpQuery)
    print("\n")
    #print(dumps(response_nlp,indent =4))
    
    if response_nlp["intent"]["name"]=="greet":
        a="Hello, How can I help you?"        
        c = 'espeak -ven+f5 -k1 -s200 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("Hello, How can I help you?")
        print("\n")

    elif response_nlp["intent"]["name"]=="thankyou":
        print("My pleasure!")
        print("\n")
        
    elif response_nlp["intent"]["name"]=="bye":
        print("Good bye.")
        print("\n")        

    elif response_nlp["intent"]["name"]=="curse_words":
        print("Mind your language, How can you be so rude?")
        print("\n")        

    elif response_nlp["intent"]["name"]=="love":
        print("This queen doesn’t need a king.")
        print("\n")

    elif response_nlp["intent"]["name"]=="bored":
        print("How sad?, why can't we become friends?")
        print("\n")

    elif response_nlp["intent"]["name"]=="my_name":
        print("I'm Alida")
        print("\n")
        
    elif response_nlp["intent"]["name"]=="admire":
        print("Siri")
        print("\n")
        
    elif response_nlp["intent"]["name"]=="my_dob":
        print("I was born on 14 December 2019 and by the way I'm week in math, to say what is my present age.")
        print("\n")

    elif response_nlp["intent"]["name"]=="person_name":
        page_py = wiki_wiki.page(inpQuery)
        print("\n %s" % page_py.summary.split(". ")[:2])
        print("\n")        

