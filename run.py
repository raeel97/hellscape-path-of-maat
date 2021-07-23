# python code goes here
import time
from datetime import datetime
from ascii import intro, game_over 
   
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
    game_over()
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
            exit()
            break
        else:
            print()
            print("I don't understand!")
            time.sleep(1)
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
    main_sphinx()
    
def main_sphinx():
    def sphinx():
        """
        Main sphinx function
        """
        print()
        print("""
        Allecto raises his eyebrows!!\n
        Whether this is because he is impressed or not, is not clear.
        With an imperceptible wave of his hand, he sends you hurtling
        through darkness…
        """)
        time.sleep(4)
        print()
        print("""
        You open your eyes and find yourself on the one side of a dimly
        lit rectangular room.
        """)
        time.sleep(3)
        print()
        print("""
        You survey the room and notice many broken vases and ornaments
        and lots of nondescript furniture that had seen better days.
        """)
        time.sleep(3)
        print()
        print("""
        There also seems to be a lot of pale yellow sand in the room.
        """)
        time.sleep(3)
        print()
        print("""
        You look at the walls and notice the markings on them resemble
        hieroglyphics.
        """)
        time.sleep(3)
        print()
        print("""
        With a start you realize you are in an egytian tomb.
        On the other side of the room, is a large stone door.
        """)
        time.sleep(3)
        print()
        sphinx_choice_one()

    def sphinx_choice_one():
        while True:
            print("What do you do?")
            sphinx_choice_one = input("""
            A - Look through the furniture for clues
            B - Rush forward and try and pry open the door.
            """)
            first_sphinx_answer = sphinx_choice_one.upper()
            if first_sphinx_answer == "A":
                sphinx_choice_one_one()
                break
            elif first_sphinx_answer == "B":
                sphinx_choice_one_two()
                break
            else:
                time.sleep(2)
                print()
                print("Select A or B!")
                print()

    def sphinx_choice_one_one():
        time.sleep(3)
        print("""
        You make your way to a large worn cabinet, as you open
        the cabinet door, you scream as hundreds of scarab beetles
        swarm up the wall like a black cloud.
        """)
        time.sleep(3)
        print("""
        You jump back in horror and decide to escape this horrible room!
        """)
        sphinx_choice_one_two()

    def sphinx_choice_one_two():
        time.sleep(3)
        print("""
        You rush towards the large stone door. Once there you frantically
        start searcing for a lever or a switch of some kind!
        """)
        time.sleep(3)
        print("""
        Suddenly a horrible smells fills the room and the hairs on your neck
        prickle up
        """)
        time.sleep(3)
        print("""
        You turn and find yourself face to face with the
        strangest creature you have ever laid eyes on.
        Their face is beautiful in a genderless androgynous
        way, with slitted dark eyes, high cheekbones and golden
        skin. Atop their head rests a large striped headdress
        that would have even the most ostentatious pharaoh
        jealous. From the neck down, you see a powerfully built
        leonine body resting gracefully on the floor. Each one of
        its paws is bigger than your head.
        """)
        time.sleep(10)
        print("""
        The creature stares at you impassivley, its sharp intelligent eyes
        giving away nothing, waiting for you to make a move. You notice a
        spear on the floor next to you.
        """)
        sphinx_choice_two()

    def sphinx_death():
        print("""
        The sphinx lunges forward and knocks you backward. She lands on your
        chest crushing your windpipe and ribs beneath her weight.
        """)
        time.sleep(5)
        print("""
        Choking on your blood you see her head splitting open horizonatally
        from the edges of her mouth to her ears, your realize that shes opening
        her mouth to reveal rows of razor sharp teeth.
        """)
        time.sleep(5)
        print("""
        As you scream, all you hear is the sound of your blood gurgling, wetly,
         in back of your throat. She strikes forward like a snake.
        """)
        time.sleep(5)
        print("""
        With dawning horror, you realize because you are already dead, there is
        no end to this.
        You pray to god to save you but you spend the rest of eternity being
        torn open and toyed with by the sphinx.
        """)
        time.sleep(10)
        restart_game()

    def sphinx_choice_two():
        time.sleep(3)
        while True:
            print("What do you do?")
            sphinx_choice_two = input("""
            A - Grab the spear and attack the sphinx.
            B - Try to communicate with the sphinx.
            """)
            final_choice = sphinx_choice_two.upper()
            if final_choice == "A":
                sphinx_choice_two_one()
            elif final_choice == "B":
                break
            else:
                time.sleep(2)
                print()
                print("Select A or B!")
                print()
    sphinx_choice_two_two()

    def sphinx_choice_two_one():
        print("""
        You quickly grab the spear before the sphinx has time to react.
        """)
        time.sleep(5)
        print("""
        With a warcry that reeks of fear, you rush forward, aiming for the
        heart!
        """)
        time.sleep(5)
        print("""
        The sphinx lazily swipes at your spear, knocking it out of your hand!
        """)
        time.sleep(5)
        sphinx_death()

    def sphinx_choice_two_two():
        print("""
        Shaking like a leaf, your voice cracks as you ask
        “Do you speak English?”
        """)
        time.sleep(5)
        print("""
        The sphinx responds in a heavily accented purr “I speak all mortal
        languages, dead or alive”
        """)
        time.sleep(5)
        print("""
        You nod, frozen in fear.
        """)
        time.sleep(5)
        print("""
        The sphinx continues “Answer my riddle correctly and you may move along
        the path of the goddess Maat”
        """)
        time.sleep(5)
        print("""
        You choke out “And if I get it wrong?”
        """)
        time.sleep(5)
        print("""
        The sphinx replies “It would be in your best interest to not get it
        wrong”
        """)
        sphinx_riddle()

    def sphinx_riddle():
        global riddle
        global riddle_answer
        riddle_answer = "your word"
        riddle = "You cannot keep me until you have given me. What am I?"
        time.sleep(5),
        s = []
        while True:
            global ask_riddle
            print(f"""    The sphinx asks: \n    “{riddle}”
            """)
            ask_riddle = input("""    A - Your Mind \n    B - Your Soul \n    C - Your Word\n
            """)
            final_riddle_answer = ask_riddle.upper()
            if final_riddle_answer == "C":
                sphinx_final()
                break
            elif final_riddle_answer != "C":
                s.append(ask_riddle)
                if len(s) < 2:
                    print("""
                    The sphinx is growing restless. Better get it right next time
                    """)
                    time.sleep(3)
                    continue
                else:
                    time.sleep(3)
                    print("""
                    The sphinx has grow tired of your stupidity.
                    """)
                    time.sleep(3)
                    sphinx_death()
                    brreak


    def sphinx_final():
        time.sleep(5)
        print("""
        The sphinx stares at you. In its eyes you can detect the smallest
        glimmer of pride.
        """)
        time.sleep(5)
        print("""
        The sphinx taps her paw against the ground. A loud rumble fills the
        room.
        """)
        time.sleep(5)
        print("""
        You turn and see the large stone door has slid opened.
        You look back at the sphinx.
        """)
        time.sleep(5)
        print("""
        The sphinx nods and wishes you well, the smallest hint of regret
        in its voice.
        It informs you, that you may continue your journey along the path of
        maat.
        """)
        time.sleep(5)
        print("""
        You slowly back away from the sphinx, until you reach the doorway
        then you turn and run as fast as you can.
        """)
        time.sleep(5)
        vampire()
    sphinx()
def vampire():
    print("""
    After wondering down a dark tunnel for what feels like an eternity, 
    you find yourself in a cold, creepy church
    """)
def run_game():
    intro()
    time.sleep(2)
    print()
    get_user_data()
    print()
    time.sleep(1)
    first_part()
run_game()
