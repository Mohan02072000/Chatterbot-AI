import webbrowser
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer



def executer(s):
    
    w=word_tokenize(s)

    if("Search" in w):

        print("this is google search sector")
        browser(w)


    if("Execution" in w):
        print("this is execution sector")

def browser(w):
    s=""
    x=len(w)
    for i in range(3,x):
        s=s+"+"+w[i]
    print(s)



s=input()

executer(s)