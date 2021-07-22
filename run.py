# python code goes here
import time
from datetime import datetime

player_details = []
def intro():
    """
    Simple game intro that uses sleep function to slow down the print statements. The intro fucntion 
    also requests user name and date of birth!
    """

    print("█𓂀█☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥█𓂀█")
    time.sleep(0.1) 
    print("███                                                             ███")
    time.sleep(0.1) 
    print("█☥█              ███    ███ ███▀▀▀▀ ███     ███                 █☥█")
    time.sleep(0.1)    
    print("███              ███■■■■███ ███■■■■ ███     ███                 ███")
    time.sleep(0.1)     
    print("█☥█              ███    ███ ███▄▄▄▄ ███▄▄▄▄ ███▄▄▄▄             █☥█")
    time.sleep(0.1) 
    print("███                                                             ███")
    time.sleep(0.1) 
    print("█☥█          ███▀▀▀▀ ███▀▀▀▀ ███▀▀▀▀███ ███▀▀▀▀█ ███▀▀▀▀        █☥█")
    time.sleep(0.1) 
    print("███          ▀▀▀▀███ ███     ███■■■■███ ███▄▄▄▄█ ███■■■■        ███")
    time.sleep(0.1) 
    print("█☥█          ▄▄▄▄███ ███▄▄▄▄ ███    ███ ███      ███▄▄▄▄        █☥█")
    time.sleep(0.1) 
    print("███                                                             ███")
    time.sleep(0.1) 
    print("█☥█          █▀█ █▀█ ▀█▀ █▄█   █▀█ █▀   █▀█▀█ █▀█ █▀█ ▀█▀       █☥█")
    time.sleep(0.1) 
    print("███          █▀▀ █▀█  █  █▀█   █▄█ █▀   █ █ █ █▀█ █▀█  █        ███")
    time.sleep(0.1) 
    print("█☥█                                                             █☥█")
    time.sleep(0.1) 
    print("███                                                             ███")
    time.sleep(0.1) 
    print("█☥█            ▄▀                                  ▀▄           █☥█")
    time.sleep(0.1)  
    print("███           █             █          █             █          ███")
    time.sleep(0.1)  
    print("█☥█          ██             ██        ██             ██         █☥█")
    time.sleep(0.1) 
    print("███           ██          ▄██████████████▄          ██          ███")
    time.sleep(0.1)  
    print("█☥█            ███▄▄▄▄▄▄██▀ ████████████ ▀██▄▄▄▄▄▄███           █☥█")
    time.sleep(0.1) 
    print("███             ▀█████████▄     ████     ▄█████████▀            ███")
    time.sleep(0.1) 
    print("█☥█                   █████████▄▄██▄▄█████████                  █☥█")
    time.sleep(0.1) 
    print("███                  ▀████████████████████████▀                 ███")
    time.sleep(0.1) 
    print("█☥█                    ▀████████████████████▀                   █☥█")
    time.sleep(0.1) 
    print("███                      ▀██ █ █ █ █ █ █ █▀                     ███")
    time.sleep(0.1) 
    print("█☥█                        ▀██ █ █ █ █ █▀                       █☥█")
    time.sleep(0.1) 
    print("███                          ▀██ █ █ █▀                         ███")
    time.sleep(0.1) 
    print("█☥█                            ▀██ ██▀                          █☥█")
    time.sleep(0.1) 
    print("███                              ▀█▀                            ███")
    time.sleep(0.1) 
    print("█☥█                                                             █☥█")
    time.sleep(0.1) 
    print("█𓂀█☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥████☥█𓂀█")                                   
    
def get_name():  
    name = input("What's your name?:")
    time.sleep(1)
    print(f"Welcome to Hellscape: Path of Maat, {name}!")
    player_details.append(name)

def get_dob():
    """
    Gets date of birth and checks if date of birth is in the correct format. 
    """
    print("Answer in the following format:DDMMYYYY")
    time.sleep(1)
    print()
    while True:
        dob = input("Whats your date of birth?")
        if len(dob) == 8 and dob.isnumeric() == True:
            return dob
            break
        else: 
            print()
            time.sleep(1)
            print("Incorrect format")
            print()
            time.sleep(1)
            print("Please provide your date of birth in the following format: \nDDMMYYYY")
            time.sleep(1)
            print()
            continue
    
def zodiac():
    list = []
    dob = get_dob()
    day = dob[0:2]
    month = dob[2:4]
    list.append(int(day))
    list.append(int(month))
    sun = ""
    year = dob[4:]
    if int(month) == 3 and int(day) <= 20:
        sun = "Pisces"
        print(sun)
    elif int(month) == 3 and int(day) > 20:
        sun = "Aries"
    elif int(month) == 4 and int(day) < 20:
        sun = "Aries"
    elif int(month) == 4 and int(day) >= 20:
        sun = "Taurus"
    elif int(month) == 5 and int(day) <= 20:
        sun = "Taurus"
    elif int(month) == 5 and int(day) > 20:
        sun = "Gemini"
    elif int(month) == 6 and int(day) <= 21:
        sun = "Gemini"
    elif int(month) == 6 and int(day) >= 21:
        sun = "Cancer"
    elif int(month) == 7 and int(day) <= 22:
        sun = "Cancer"
    elif int(month) == 7 and int(day) >= 21:
        sun = "Leo"
    elif int(month) == 8 and int(day) <= 20:
        sun = "Leo"
    elif int(month) == 8 and int(day) >= 21:
        sun = "Virgo"
    elif int(month) == 9 and int(day) <= 22:
        sun = "Virgo"
    elif int(month) == 9 and int(day) >= 23:
        sun = "Libra"
    elif int(month) == 10 and int(day) <= 23:
        sun = "Libra"
    elif int(month) == 10 and int(day) >= 23:
        sun = "Scorpio"
    elif int(month) == 11 and int(day) <= 23:
        sun = "Scorpio"
    elif int(month) == 11 and int(day) >= 23:
        sun = "Sagittarius"
    elif int(month) == 12 and int(day) <= 21:
        sun = "Sagittarius"
    elif int(month) == 12 and int(day) >= 22:
        sun = "Capricorn"
    elif int(month) == 1 and int(day) <= 19:
        list.append("Capricorn")
    elif int(month) == 1 and int(day) >= 20:
        sun = "Aquarius"
    elif int(month) == 2 and int(day) <= 18:
        sun = "Aquarius"
    print(list)
    
    
    
        

def get_user_data():
    player_details = {}
    #get_name()
    #print()
    #get_dob()
    zodiac()

#def run_game():
    #intro()
    #time.sleep(1)
    #print()
    #get_user_data()
get_user_data()