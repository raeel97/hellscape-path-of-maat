# python code goes here
import time
from datetime import datetime
player_details = []


def intro():
    """
    Simple game intro that uses sleep function to slow down the print\n 
    statements. The intro function also requests user name and date of birth!
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

def game_over():
    print(" 💀 💀 💀 💀 💀 💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀")
    time.sleep(0.1) 
    print("💀                                                         💀")
    time.sleep(0.1)  
    print("💀  ██▀▀▀▀▀▀▀▀██ ██▀▀▀▀▀▀▀██ ██▀▀▀▀██▀▀▀▀██ ██▀▀▀▀▀▀▀▀▀▀█  💀")
    time.sleep(0.1) 
    print("💀  ██           ██       ██ ██    ██    ██ ██             💀")
    time.sleep(0.1) 
    print("💀  ██           ██▄▄▄▄▄▄▄██ ██    ██    ██ ██▄▄▄▄▄▄▄██    💀")
    time.sleep(0.1) 
    print("💀  ██  ██▀▀▀▀██ ██       ██ ██    ██    ██ ██▀▀▀▀▀▀▀██    💀")
    time.sleep(0.1) 
    print("💀  ██        ██ ██       ██ ██          ██ ██             💀")
    time.sleep(0.1) 
    print("💀  ██▄▄▄▄▄▄▄▄██ ██▄     ▄██ ██▄        ▄██ ██▄▄▄▄▄▄▄▄▄▄█  💀")
    time.sleep(0.1) 
    print("💀                                                         💀")
    time.sleep(0.1) 
    print("💀  ██▀▀▀▀▀▀▀▀██ █▀▀▀   ▀▀▀█ ██▀▀▀▀▀▀▀▀▀▀█ ██▀▀▀▀▀▀▀▀▀▀██  💀")
    time.sleep(0.1)  
    print("💀  ██        ██ █         █ ██            ██          ██  💀")
    time.sleep(0.1) 
    print("💀  ██        ██ ▀█       █▀ ██▄▄▄▄▄▄▄▄█   ██          ██  💀")
    time.sleep(0.1) 
    print("💀  ██        ██  ▀█     █▀  ██▀▀▀▀▀▀▀▀█   ██▀▀▀▀██▀▀▀▀▀▀  💀")
    time.sleep(0.1) 
    print("💀  ██        ██   ▀█   █▀   ██            ██     ▀█       💀")
    time.sleep(0.1) 
    print("💀  ██▄▄▄▄▄▄▄▄██    ▀█▄█▀    ██▄▄▄▄▄▄▄▄▄▄█ ██      ▀█▄▄▄█  💀")
    time.sleep(0.1)  
    print("💀                                                         💀")
    time.sleep(0.1) 
    print(" 💀  💀  💀  💀  💀  💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀")
 
def get_name(): 
    while True:
        global name 
        player_name = input("What's your name?:\n")
        name = player_name.capitalize() 
        print()
        if name == "":
            print("Please enter a name to continue")
            continue
        else: 
            time.sleep(2)
            print(f"Welcome to Hellscape: Path of Maat, {name}!")
            break
        print()

def get_dob():
    """
    Gets date of birth and checks if date of birth is in the correct format. 
    """
    print("Answer in the following format:DDMMYYYY")
    time.sleep(1)
    print()
    while True:
        dob = input("Whats your date of birth?\n")
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
    global age
    dob = get_dob()
    list = []
    now = datetime.now()
    now_string = str(now)
    current_year = int(now_string[0:4])
    day = dob[0:2]
    month = dob[2:4]
    year = dob[4:]
    age = current_year - int(year)
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

def restart_game():
    print()
    while True:
        print("Answer Y or N")
        restart_choice = input("Would you like to try again? Y/N\n")
        restart = restart_choice.upper()
        if restart == "Y":
            a = [ "3", "2", "1"]
            print("The game will begin in 3 seconds...")
            for i in a:
                time.sleep(0.5)
                print(i)
                time.sleep(0.75)
                continue
            run_game()
        elif restart == "N":
            print(
            """
            Thank you so much for playing!
            """)
            game_over()
            break
        else:
            print("I don't understand!")
            continue
            



def first_part():
    print("""
    You wake to find yourself in a desolate wasteland.
    """)
    time.sleep(1.5)
    print("""
    The sky above you is an angry sooty crimson, 
    casting a red haze everywhere that meets the 
    eye, but strangely enough the unbearable heat
    that feels like its slowly roasting you alive 
    comes not from the sky but from the ground beneath 
    you, you cannot locate the source of evil light         
    that fills the world around you.. Startled, you 
    realize there is no sun in the sky.
    """)
    time.sleep(8)
    print(
    """
    The harsh winds that tear at your face smell of 
    sulfur and decaying flesh, they carry the sounds 
    of inumerable agonized screams
    """)
    time.sleep(5)
    print(
    """
    The sound of large leathery wings flapping in the 
    distance sends a frightful shiver down your spine. 
    A large thud sounds behind you. You turn and find 
    yourself face to face with none other than 
    Nicholas Cage himself. Wearing a nicely tailored 
    three piece suit, he surveys you with cool indifference, 
    his glittering malevolent eyes the only that gives 
    away his true nature. That and the two large batlike 
    wings that are folding themselves away. 
    """)
    time.sleep(8)
    print(
    f"""
    “Welcome to Erebus, {name}. In case it escaped your 
    notice, I’m happy to inform you that you are dead” 
    he says, his mouth curling up in amusement. He continued 
    “I am Allecto, and my job is to punish you for the sins 
    you committed in the {age} years you roamed the mortal 
    plane. Your offenses are numerous, chief among them, 
    the lies you spoke, those crocs you wore once
    when you thought no one was looking, the animals that 
    suffered for your nourishment, that candy bar you stole 
    in third grade…. ”
    """)
    time.sleep(8)
    print(
    """
    A bubble of panic forms in your chest, this is it, the 
    moment every human being fears deep deep down. The reckoning 
    of all your mistakes. You think of your loved ones, you’ll 
    never see them again. You have so many regrets..... 
    """)
    time.sleep(5)
    print(
    """
    Allecto interrupts your panicked thoughts “Usually my job 
    is to escort you to the dungeons of Erebus, located in Tartarus, 
    however, I am presented with a dilemma. Most mortals that end 
    up here have sufficiently blackened their souls to the point 
    where redemption is impossible, your soul however, as mediocre 
    as the mortal thats attached to it, is salvageable.”
    """)
    time.sleep(5)
    print(
    """
    The bubble of panic in your chest is quickly replaced by a bubble of hope!
    """)
    time.sleep(3)
    print(
    f"""
    “You have a choice before you {name}, you can either spend an 
    eternity wandering the endless fields of despair, a punishment 
    created for the meek and unremarkable, or you can choose the path 
    of the goddess Maát and stand a chance of redeeming yourself-”
    """)
    time.sleep(6)
    print(
    """
    Emboldened by the prospect of a positive outcome, you interrupt 
    and ask “What would the path of Maat entail? And also, why do you 
    look like Nicholas Cage?”
    """)
    time.sleep(3)
    print(
    """
    “SILENCE, MORTAL! I did not give you leave to speak!” Allecto snaps! 
    The ground rumbles beneath his displeasure, red lightning crackles 
    in the distance.
    """)
    time.sleep(5)
    print(
    """
    Straightening a hair that had fallen out of place, Allecto calmly 
    continues “Firstly, I don't look like Nicholas Cage, he looks like me!
    Second and most importantly, the path of Maat is not an easy path. 
    You will be challenged and tested! If you fail any of the challenges, 
    you will subjected to realities of unbridled suffering that 
    you cannot even begin to imagine”
    """)
    time.sleep(8)
    print(
    """
    “The time for talking has come to an end! You must now choose!”
    """)
    time.sleep(3)
    print(
    """
    “Will you walk the path of Maat or do you choose the fields of despair?”
    """)
    time.sleep(3)
    
    while True:
        print("Answer A for the Path of Maat or B for the Fields of Despair")
        first_choice = input("I choose:\n")
        first_choice_upper = first_choice.upper()
        if first_choice_upper == "B":
            print(
            """
            Allecto smiles maliciously at your choice. “You mortals 
            are so weak” he laughs, he then snaps his fingers and 
            everything goes black....
            """)
            time.sleep(6)
            print("""
            You wake to find yourself in a endless grass field.\n
            Everywhere you look, you are greeted by silent emptiness.
            """)
            time.sleep(3)
            print("""
            You scream but you cannot hear the sound of your own voice!!
            """)
            time.sleep(3)
            print("""
            You aimlessly wander, looking for something, anything!!
            But you find nothing but despair!!
            """)
            time.sleep(3)
            restart_game()
            break
        elif first_choice_upper == "A": 
            break
        else:
            print()
            print("Allecto doesn't understand you choice, do not anger him!")
            time.sleep(6)
            print()
            continue

def get_user_data():
    get_name()
    print()
    time.sleep(2)
    zodiac()
    print()
    print(f"Thank you {name}, have fun!\n")
    time.sleep(2)


def run_game():
    intro()
    time.sleep(2)
    print()
    get_user_data()
    print()
    time.sleep(1)
    first_part()
run_game()

