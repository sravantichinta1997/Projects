import aiml
from screens2 import *
import os
import re
import webbrowser
import requests
from bs4 import BeautifulSoup
import re

k=aiml.Kernel()
BRAIN_FILE="brain.dump"
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="start1.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


def temp1(url1):
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, 'html.parser')
    k=soup.find_all('td')
    l=k[12]
    k=str(l)
    m=k[4:9]
    return m
    

    
kaya=" "
name=" "
        


def granny6(user_input):
    
    ss=user_input.split(" ")
    ss2=ss.count('to')
    ss3=ss.count('from')
    if(ss2>1):
        ss4=ss.index('to')
        del ss[ss4]
    elif(ss3>1):
        ss5=ss.index('from')
        del ss[ss5]
    else:
        pass
    
    try:
        user1=ss.index('from')+1
        user2=ss.index('to')+1
        user11=ss[user1]
        user22=ss[user2]
        auto(user11,user22)
        return "The map is displayed on your chrome browser"
    except ValueError:
        return " Life is a journey ...bon voyage"
        
            
    
def granny2(user_input):
    samm=user_input.split(" ")
    try:
        samm1=samm.index('of')+1
        name67=samm[samm1]
    
        
    except ValueError: 
        samm2=samm.index('in')+1
        name67=samm[samm2]
    url345="https://www.timeanddate.com/weather/india/"+name67
    print(url345)
    page = requests.get(url345)
    soup = BeautifulSoup(page.content, 'html.parser')
    k=soup.find_all('td')
   
    try:
        l=k[12]
        k=str(l)
        m=k[4:9]
        return m
    except IndexError:
        return "Please type your city name"
    
        
    

def dean(user_input):
    global kaya
    global name
    match2=re.search("temperature *",user_input,re.IGNORECASE)
    xmas=['route','way','path','go','direction','path']
    for w in xmas:
        match6=re.search(w,user_input,re.IGNORECASE)
        if match6:
            break
        
    
    
    if(kaya=="Please type your city name"):
        name1="city name is "+ user_input
        name=user_input
        x=k.respond(name1)
        kaya=x
        return x,name1
    elif(kaya=="Can you please tell me the country name"):
        name2="the country name is  " +user_input
        name4=user_input+"/"
        x=k.respond(name2)
        url1="https://www.timeanddate.com/weather/"+name4+name
        sat1=temp1(url1)
        y=x+sat1
        kaya=y
        return y,name2
    elif(match2):
        fan2=granny2(user_input)
        x=fan2
        kaya=x
        return x,user_input
    elif(match6):
        fan6=granny6(user_input)
        x=fan6
        kaya=x
        return x,user_input
    else:
        x=k.respond(user_input)
        kaya=x
        return x,user_input
    



        
        
      
