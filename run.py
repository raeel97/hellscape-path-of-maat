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
    time.sleep(2)
    print()
    print(f"Welcome to Hellscape: Path of Maat, {name}!")
    return name

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
            time.sleep(2)
            print("Incorrect format")
            print()
            time.sleep(2)
            print("Please provide your date of birth in the following format: \nDDMMYYYY")
            time.sleep(2)
            print()
            continue
    
def zodiac():
    list = []
    dob = get_dob()
    day = dob[0:2]
    month = dob[2:4]
    year = dob[4:]
    if int(month) == 3 and int(day) <= 20:
        list.append("Pisces")
    elif int(month) == 3 and int(day) > 20:
        list.append("Aries")
    elif int(month) == 4 and int(day) < 20:
        list.append("Aries")
    elif int(month) == 4 and int(day) >= 20:
        list.append("Taurus")
    elif int(month) == 5 and int(day) <= 20:
        list.append("Taurus")
    elif int(month) == 5 and int(day) > 20:
        list.append("Gemini")
    elif int(month) == 6 and int(day) <= 21:
        list.append("Gemini")
    elif int(month) == 6 and int(day) >= 21:
        list.append("Cancer")
    elif int(month) == 7 and int(day) <= 22:
        list.append("Cancer")
    elif int(month) == 7 and int(day) >= 21:
        list.append("Leo")
    elif int(month) == 8 and int(day) <= 20:
        list.append("Leo")
    elif int(month) == 8 and int(day) >= 21:
        list.append("Virgo")
    elif int(month) == 9 and int(day) <= 22:
        list.append("Virgo")
    elif int(month) == 9 and int(day) >= 23:
        list.append("Libra")
    elif int(month) == 10 and int(day) <= 23:
        list.append("Libra")
    elif int(month) == 10 and int(day) >= 23:
        list.append("Scorpio")
    elif int(month) == 11 and int(day) <= 23:
        list.append("Scorpio")
    elif int(month) == 11 and int(day) >= 23:
        list.append("Sagittarius")
    elif int(month) == 12 and int(day) <= 21:
        list.append("Sagittarius")
    elif int(month) == 12 and int(day) >= 22:
        list.append("Capricorn")
    elif int(month) == 1 and int(day) <= 19:
        list.append("Capricorn")
    elif int(month) == 1 and int(day) >= 20:
        list.append("Aquarius")
    elif int(month) == 2 and int(day) <= 18:
        list.append("Aquarius")
    elif int(month) == 2 and int(day) >= 19:
        list.append("Pisces")
    return list      

def first_story():
    print()
    print("You wake to find yourself in a desolate wasteland.")
    time.sleep(1)
    print()
    print("The sky above you is a sooty crimson, but strangely enough the heat comes from the earth, you cannot locate the source of evil light that fills the world around you.")
    time.sleep(1)
    print()
    print("The harsh winds that tear at your face smell of sulfur and decaying flesh, the sounds of inumerable agonized screams fill your head")

def get_user_data():
    get_name()
    print()
    time.sleep(2)
    zodiac()

def run_game():
    intro()
    time.sleep(2)
    print()
    get_user_data()
    first_story()
run_game()