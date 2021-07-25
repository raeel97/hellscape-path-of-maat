import time
from datetime import datetime
from ascii import intro, game_over, end_game
import random


def get_name():
    """
    Requests the users name to be used throughout the story
    """
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
    lo = "Please provide your date of birth in the following format:\nDDMMYYYY"
    time.sleep(1)
    print()
    global dob
    while True:
        dob = input("Whats your date of birth?\n")
        if len(dob) == 8 and dob.isnumeric() is True:
            if int(dob[0:2]) <= 31 and int(dob[2:4]) <= 12:
                if int(dob[4:]) > 1910 and int(dob[4:]) < 2008:
                    return dob
                else:
                    print()
                    time.sleep(2)
                    print("Incorrect year")
                    print()
                    time.sleep(2)
                    print(lo)
                    time.sleep(2)
                    print()
                    continue
            else:
                print()
                time.sleep(2)
                print("Incorrect day/month format")
                print()
                time.sleep(2)
                print(lo)
                time.sleep(2)
                print()
                continue
        else:
            print()
            time.sleep(2)
            print("Incorrect format")
            print()
            time.sleep(2)
            print(lo)
            time.sleep(2)
            print()
            continue


def zodiac():
    """
    Takes users date of birth as a string, slices where needed and converts
    day, month and year into integers. Uses date of birth to get users
    astrological zodiac sign to be used later in the app.
    """
    global age
    global zodiac_list
    global current_year
    dob = get_dob()
    zodiac_list = []
    now = datetime.now()
    now_string = str(now)
    current_year = int(now_string[0:4])
    day = dob[0:2]
    month = dob[2:4]
    year = dob[4:]
    age = current_year - int(year)
    if int(month) == 3 and int(day) <= 20:
        zodiac_list.append("Pisces")
    elif int(month) == 3 and int(day) > 20:
        zodiac_list.append("Aries")
    elif int(month) == 4 and int(day) < 20:
        zodiac_list.append("Aries")
    elif int(month) == 4 and int(day) >= 20:
        zodiac_list.append("Taurus")
    elif int(month) == 5 and int(day) <= 20:
        zodiac_list.append("Taurus")
    elif int(month) == 5 and int(day) > 20:
        zodiac_list.append("Gemini")
    elif int(month) == 6 and int(day) <= 21:
        zodiac_list.append("Gemini")
    elif int(month) == 6 and int(day) >= 21:
        zodiac_list.append("Cancer")
    elif int(month) == 7 and int(day) <= 22:
        zodiac_list.append("Cancer")
    elif int(month) == 7 and int(day) >= 21:
        zodiac_list.append("Leo")
    elif int(month) == 8 and int(day) <= 20:
        zodiac_list.append("Leo")
    elif int(month) == 8 and int(day) >= 21:
        zodiac_list.append("Virgo")
    elif int(month) == 9 and int(day) <= 22:
        zodiac_list.append("Virgo")
    elif int(month) == 9 and int(day) >= 23:
        list.append("Libra")
    elif int(month) == 10 and int(day) <= 23:
        zodiac_list.append("Libra")
    elif int(month) == 10 and int(day) >= 23:
        zodiac_list.append("Scorpio")
    elif int(month) == 11 and int(day) <= 23:
        list.append("Scorpio")
    elif int(month) == 11 and int(day) >= 23:
        list.append("Sagittarius")
    elif int(month) == 12 and int(day) <= 21:
        zodiac_list.append("Sagittarius")
    elif int(month) == 12 and int(day) >= 22:
        zodiac_list.append("Capricorn")
    elif int(month) == 1 and int(day) <= 19:
        zodiac_list.append("Capricorn")
    elif int(month) == 1 and int(day) >= 20:
        zodiac_list.append("Aquarius")
    elif int(month) == 2 and int(day) <= 18:
        zodiac_list.append("Aquarius")
    elif int(month) == 2 and int(day) >= 19:
        zodiac_list.append("Pisces")
    return list


def zodiac_monster():
    """
    Once the fifth choice has taken place and the relevant function has
    run, this function runs. It holds the functions for each end boss demon
    thats computed from the users astrology sign. The final run function
    runs at the end of this function.
    """
    global demon_name

    def capricorn():
        """
        Assigns the user the Capricornus demon
        """
        global demon_name
        demon_name = "Capricornus"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        Its head resembles a horse sized goat with a fish tail for back legs.
        Its fiery eyes gaze at you in hostility!
        """)
        time.sleep(6)

    def aquarius():
        """
        Assigns the user the Aquaria demon
        """
        global demon_name
        demon_name = "Aquaria"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        Its a large golem made from pale white stone, fashioned into the form
        of a man carrying a large vase filled with foul smelling water!
        Its empty eyes stares at you in solemn hostility!
        """)
        time.sleep(6)

    def pisces():
        """
        Assigns the user the Piscea demon
        """
        global demon_name
        demon_name = "Piscea"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A large piscean humanoid figure stands before you, with balelful solid
        black eyes. Its skin is covered in dark grey scales, spikes potrude
        from its joints, its exaggerated mouth is filled with pike like teeth
        and a fin mowhawk protrudes from its bald head.
        """)
        time.sleep(10)

    def aries():
        """
        Assigns the user the Aries demon
        """
        global demon_name
        demon_name = "Aries"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A large man with the head of a ram stands before you, its fiery
        eyes staring at you hatefully as it pounds the ground with its hooves!
        """)
        time.sleep(8)

    def taurus():
        """
        Assigns the user the Taurai demon
        """
        global demon_name
        demon_name = "Taurai"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A large man with the head of a bull stands before you, its fiery
        eyes staring at you hatefully as it pounds the ground with its hooves!
        Its gleaming curved horns, holding the promise of violence.
        """)
        time.sleep(8)

    def gemini():
        """
        Assigns the user the Geminitron demon
        """
        global demon_name
        demon_name = "Geminitron"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A hairless two headed harpy stands before you. Each head stares at you
        hatefully. Its leathery wings flap in anger, its taloned feet scracth
        the ground
        """)
        time.sleep(8)

    def cancer():
        """
        Assigns the user the Canceria demon
        """
        global demon_name
        demon_name = "Canceria"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        An orange humanoid figure stands before you, its lower body resembles a
        crab and each one of its arms ends in a powerful pincer that look as
        if it could crush rocks. It stares at with hard eyes!
        """)
        time.sleep(8)

    def leo():
        """
        Assigns the user the Leonidus demon
        """
        global demon_name
        demon_name = "Leonidus"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        An infernal lion stands before you! Whereas the sphinx you faced before
        was calm and indifferent, this beast stares at you with unbrindled
        aggresion.
        Its wild mane burns with hell fire and its glowing coal-like eyes stare
        at you with hate as its bares its black fangs at you.
        """)
        time.sleep(9)

    def virgo():
        """
        Assigns the user the Virgoth demon
        """
        global demon_name
        demon_name = "Virgoth"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        It resembles a beautiful young girl that looks barely older than 13.
        Its eyes however are solid red and its long hair trails down to
        its knees in dark waves. Its skin is the color of a corpse. It smiles
        revealing sharklike teeth.
        """)
        time.sleep(10)

    def libra():
        """
        Assigns the user the Librenna demon
        """
        global demon_name
        demon_name = "Librenna"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A golden one eyed, armless being stands before you. Its torso has been
        impaled horizontally by a large golden pole. Each end sticks out where
        its arms would normally join its shoulders. Its mouth is missing lips
        revealing a mouthful of iron pins for teeth.
        From each end of the poles hangs a large flat bowl. It stares at you
        in anger, as if you were the one who subjected it to this cruel fate.
        """)
        time.sleep(1)

    def scorpio():
        """
        Assigns the user the Scorperia demon
        """
        global demon_name
        demon_name = "Scorperia"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A burgundy humanoid figure stands before you, its lower body resembles
        a scorpion and each one of its arms ends in a powerful pincer that look
        as if it could crush rocks. It stares at you with beetle like eyes!
        """)
        time.sleep(10)

    def sagittarius():
        """
        Assigns the user the Saggitar demon
        """
        global demon_name
        demon_name = "Saggitar"
        print("""
        Before you stands your own personal demon, terror fills your soul.
        A horrifying centaur stands before you. The human part of its body
        resembles a powerfully built bald man with a long white beard. It
        carries a crude bow and on his back lies a quiver of barbed arrows.
        Its eyes have been torn out, the black empty sockets still manage to
        stare you down in a predatory manner.
        """)
        time.sleep(10)
    if zodiac_list[-1] == "Capricorn":
        capricorn()
    elif zodiac_list[-1] == "Aquarius":
        aquarius()
    elif zodiac_list[-1] == "Pisces":
        pisces()
    elif zodiac_list[-1] == "Aries":
        aries()
    elif zodiac_list[-1] == "Taurus":
        taurus()
    elif zodiac_list[-1] == "Gemini":
        gemini()
    elif zodiac_list[-1] == "Cancer":
        cancer()
    elif zodiac_list[-1] == "Leo":
        leo()
    elif zodiac_list[-1] == "Virgo":
        virgo()
    elif zodiac_list[-1] == "Libra":
        libra()
    elif zodiac_list[-1] == "Scorpio":
        scorpio()
    elif zodiac_list[-1] == "Sagittarius":
        sagittarius()
    final_run()


def restart_game():
    """
    Prints the ascii art for game over and asks the user if they want to
    try again. If the user opts to try again, the main run_game function
    is run, if they opt for no, they're thanked for playing and the game
    ends
    """
    game_over()
    print()
    while True:
        print("Answer Y or N")
        restart_choice = input("Would you like to try again? Y/N\n")
        restart = restart_choice.upper()
        if restart == "Y":
            a = ["3", "2", "1"]
            print("The game will begin in 3 seconds...")
            for i in a:
                time.sleep(0.5)
                print(i)
                time.sleep(0.75)
                continue
            run_game()
        elif restart == "N":
            print("""
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
    """
    Main user data function which first gets the users name, then gets the
    users age and the users zodiac sign. The user is then thanked and
    told to have fun.
    """
    get_name()
    print()
    time.sleep(2)
    zodiac()
    print()
    print(f"Thank you {name}, have fun!\n")
    time.sleep(2)


def first_part():
    """
    First part of story line takes place. And then first choice happens.
    Once user selects the choice, the appropriate function takes place and
    more storyline takes place. If they dont lose, they loop back to this
    function and the sphinx function is called.
    """
    print("""
    You wake to find yourself in a desolate wasteland.
    """)
    time.sleep(4)
    print("""
    The sky above you is an angry sooty crimson, casting a red haze everywhere
    that meets the eye, your skin prickles at the intense heat of the world
    around you but strangely enough the unbearable heat comes not from the sky
    but from the ground beneath you.
    Startled, you realize there is no sun in the sky, however you cannot
    locate the source of evil light that illuminates everything around you...
    """)
    time.sleep(15)
    print("""
    The harsh winds that tear at your face smell of sulfur and decaying flesh,
    they carry with them the sounds of inumerable agonized screams.
    """)
    time.sleep(7)
    print("""
    The sound of large wings flapping in the distance sends a
    frightful shiver down your spine. A heavy thud echos behind you.
    You turn and find yourself face to face with Nicholas Cage.
    In shock, you take in his nicely tailored three piece suit, cold black
    eyes, sharp white horns and two large batlike wings. Speechless, all you
    can do is stare at demonic Nicholas Cage in shock.
    """)
    time.sleep(15)
    print(f"""
    “Welcome to Erebus, {name}. In case it escaped your notice, I’m happy to
    inform you that you are dead” he says, his mouth curling up in cruel
    amusement.
    He continues “I am Allecto, Lord of Implacable Anger, and my job is to
    punish you for the sins you committed in the {age} years you roamed the
    mortal plane.
    Your offenses are numerous, chief among them, the lies you spoke,
    the crocs you wore when you thought no one was looking,
    the animals that suffered for your nourishment, yes the vegans were right,
    and worst of all that candy bar you stole in third grade…. ”
    """)
    time.sleep(20)
    print("""
    A bubble of panic forms in your chest, this is it, the moment every human
    being fears deep, deep down. The reckoning of all your mistakes.
    You think of your loved ones, you’ll never see them again.
    You have so many regrets.....
    """)
    time.sleep(7)
    print("""
    Allecto interrupts your panicked thoughts “Usually my job is to escort you
    to the dungeons of Erebus, located in Tartarus, however, I am presented
    with a dilemma. Most mortals that end up here have sufficiently blackened
    their souls to the point where redemption is impossible, your soul however
    as mediocre as the mortal thats attached to it, can be redeemed.”
    """)
    time.sleep(15)
    print("""
    The bubble of panic in your chest is quickly replaced by a bubble of hope!
    """)
    time.sleep(5)
    print(f"""
    “You have a choice before you {name}, you can either spend an eternity
    wandering the endless fields of despair, a punishment created for the meek
    and unremarkable, or you can choose the Path of the goddess Maat and stand
    a chance of redeeming yourself-”
    """)
    time.sleep(10)
    print("""
    Emboldened by the prospect of a positive outcome and unable to help
    yourself, you interrupt and ask “What would the Path of Maat entail?
    And also, why do you look like Nicholas Cage?”
    """)
    time.sleep(8)
    print("""
    “SILENCE, MORTAL! I did not give you leave to speak!” Allecto roars!
    The ground rumbles beneath you rumbles at his displeasure,
    red lightning crackles in the distance.
    """)
    time.sleep(7)
    print("""
    Straightening a hair that has fallen out of place, Allecto calmly
    continues “Firstly, I don't look like Nicholas Cage, your pathetic
    mortal brain cannot comprehend my true form so it tries to make sense of
    what it is seeing and it conjures the closest thing it can imagine!
    Interesting choice...
    Second and most importantly, the Path of Maat is not an easy path.
    You will be challenged and tested! If you fail any of the challenges,
    you will subjected to realities of endless suffering that
    you cannot even begin to imagine”
    """)
    time.sleep(20)
    print("""
    Impatient, he snaps “The time for talking has come to an end!
    You must now choose!”
    """)
    time.sleep(3)
    print("""
    “Will you walk the Path of Maat or do you choose the fields of despair?”
    """)
    time.sleep(3)
    while True:
        print("Answer A for the Path of Maat or B for the Fields of Despair")
        first_choice = input("I choose:\n")
        first_choice_upper = first_choice.upper()
        if first_choice_upper == "B":
            print("""
            Allecto smiles maliciously at your choice. “You mortals are so
            weak” he laughs, he then snaps his fingers and everything
            goes black....
            """)
            time.sleep(6)
            print("""
            You wake to find yourself in a endless grass field.\n
            Everywhere you look, you are greeted by silent emptiness.
            """)
            time.sleep(4)
            print("""
            You scream but you cannot hear the sound of your own voice!!
            """)
            time.sleep(4)
            print("""
            You aimlessly wander, looking for something, anything!!
            But you find nothing but despair!!
            """)
            time.sleep(4)
            restart_game()
            break
        elif first_choice_upper == "A":
            break
        else:
            print()
            print("Allecto doesn't understand you choice, do not anger him!")
            time.sleep(3)
            print()
            continue
    main_sphinx()


def last_part():
    """
    Final part of story line takes place. And then the fifth and sixth
    choices take place. The fifth choice leads to the same outcome. The sixth
    choice will either lead to the win function or the restart function.
    """
    time.sleep(3)
    print("""
    Emerging from the darkness, you find yourself in a large garden.
    The foilage is lush and vibrant, an odd contrast with the crimson storm
    raging in the distance. The garden is contained by thick hedges standing
    15 feet high in a box formation.
    """)
    time.sleep(10)
    print("""
    In the centre of the garden, between two large willow trees is a stone
    circle and within it is a sacrifical altar, stained a dark color that you
    swear is dried blood!
    """)
    time.sleep(7)
    print("""
    But none of these things hold your attention for long.
    Your eyes are drawn to the other side of the garden, beyond the stone
    circle and willow trees.
    """)
    time.sleep(7)
    print("""
    On either side of the garden, parallel to each other, lies a stone archway
    and a spiral staircase.
    """)
    time.sleep(4)
    print("""
    The staircase looks as if its been carved from the purest white marble in
    existence. Its so white that it almost glows in the twilight of the
    perpetual storm that rages above in the sky. It looks as if it goes
    upwards forever, dissappearing into the thick blood red clouds above the
    garden. The staircase fills you with hope!
    Its clearly a way out of Erebus!
    """)
    time.sleep(10)
    print("""
    The archway on the other hand fills you with intense fear. Within it a
    vortex of swirling fire burns, so much so it that hurts if you stare at it
    for too long. The ancient stone its hewed from, pulsates with darkness.
    """)
    time.sleep(8)
    print("A choice lies before you")
    while True:
        print("Do you:")
        final_first_choice = input("""
        A - Make a dash for freedom
        B - Meekly make your way to the circle \n""")
        final_first = final_first_choice.upper()
        if final_first == "B":
            final_first_one()
            break
        elif final_first == "A":
            final_first_two()
            break
        else:
            time.sleep(2)
            print()
            print("I don't understand your choice?")
            print()
            continue


def final_first_one():
    """
    If the second option of the 5th choice is taken, this function will run
    and then the zodiac monster function will run.
    """
    time.sleep(3)
    print("""
    You are bruised and broken. Any courage you had, is long gone.
    """)
    time.sleep(4)
    print("""
    You make your way to the altar and wait for whatever comes next!
    """)
    time.sleep(4)
    print("""
    Wish a flash of infernal light, a monstrous being appears before you.
    """)
    zodiac_monster()


def final_first_two():
    """
    If the first option of the 5th choice is taken, this function will run
    and then the zodiac monster function will run.
    """
    print("""
    Naturally you make a run for the staircase, your bruised and battered
    body slowing you down.
    """)
    time.sleep(6)
    print("""
    But just as you're about to reach the staircase, a powerful blow from out
    of nowhere knocks you backwards.
    """)
    time.sleep(6)
    print("""
    Disorientated, you yelp as something grabs you by the scruff of your
    neck and starts dragging you towards the stone circle.
    """)
    time.sleep(6)
    print("""
    Paralyzed with fear, your courage depleted.
    You allow yourself to be dragged towards whatever fate awaits you.
    """)
    time.sleep(6)
    print("""
    Whatever has a hold of you, deposits you before the altar and then
    makes its way to the head of the stone circle.
    """)
    time.sleep(6)
    print("""
    It turns to face you!
    """)
    zodiac_monster()


def final_run():
    """
    After the zodiac monster function is done running, this function will run.
    This function runs the anagram function and then the anagram checker
    function
    """
    time.sleep(4)
    print(f"""
        It declares "I am the demon {demon_name}, tremble before me mortal"
        """)
    time.sleep(5)
    print(f"""
        You stare at the demon {demon_name} in fear and ask "What do you want
        from me?"
        """)
    time.sleep(5)
    print(f"""
        {demon_name} shouts "You have come to the final trial of the Path of
        Maat, now you will answer a puzzle created by Maat herself. If you get
        this puzzle right, you will be allowed to ascend the staircase of
        and find redemeption, if you get it wrong, you will be tossed through
        the hellgate where your soul will endure the worst of all hell
        torments."
        """)
    time.sleep(14)
    print(f"""
        {demon_name} bows its head. Before you on the altar, glowing letters
        appear.
        """)
    time.sleep(5)
    print("""
        You realize its an anagram.
        """)
    anagram()
    time.sleep(5)
    anagram_checker()


def final_monster_lose():
    """
    This function holds all the zodiac monster description functions that run
    if the user gets the sixth choice wrong. The function checks to see which
    zodiac sign the users has and then it runs the final lose function
    """
    def capricorn_lose():
        print(f"""
        {demon_name} front goat legs and fish tail help it to reach you faster
        than you could have imagined.
        {demon_name} grabs you with its clawed hand. Its goat eyes bulging in
        mad excitement! It lifts you into the air and slams you against the
        ground several times to knock the fight out of you.

        You pass out
        """)
        time.sleep(13)

    def aquarius_lose():
        print(f"""
        {demon_name} moves suprisingly fast for a being made of rock!
        {demon_name} grabs you with one of its crude hands.
        Its golem eyes burning with mad excitement! It hits with you the vase
        knocking the air out of you. Some of the water in the vase sloshes
        onto your arm, with a sizzling sound the skin on your arm starts
        to melt off.

        You pass out.
        """)
        time.sleep(13)

    def pisces_lose():
        print(f"""
        {demon_name} moves suprisingly fast for an aquatic being!
        {demon_name} grabs you with its webbed hands. Its large shark eyes
        burning with mad excitement! It slashes you with its claws several
        times before bashing your head against the ground.

        You pass out.
        """)
        time.sleep(13)

    def aries_lose():
        print(f"""
        {demon_name}'s cloven hooves carry it forward with immense speed!
        {demon_name} grabs you with its clawed hands. Its ram eyes
        burning with mad excitement! It slams its horns into your body
        knocking you to the floor.
        Giving you barely any reprieve, it slams its hoof into your head.

        You pass out.
        """)
        time.sleep(13)

    def taurus_lose():
        print(f"""
        {demon_name} charges you with a bellow!
        {demon_name} grabs you with its clawed hands. Its bull eyes
        burning with mad excitement! It gores you with its horns and slams you
        into the ground.

        You pass out.
        """)
        time.sleep(13)

    def gemini_lose():
        print(f"""
        {demon_name} flaps its way towards you in the blink of an eye!
        {demon_name} slashes at you with its talons. Its hawk eyes
        burning with mad excitement! It grabs you with its talons, carries you
        10 feet into the air and forcibly throws you to the earth!

        You pass out.
        """)
        time.sleep(13)

    def cancer_lose():
        print(f"""
        {demon_name} scuttles towards you at an impressive speed for its size!
        {demon_name} backhands you with one of its pincers. Its small black
        eyes burning with mad excitement! It grabs your head with its pincers,
        and squeezes.

        You pass out.
        """)
        time.sleep(13)

    def leo_lose():
        print(f"""
        {demon_name} leaps towards you with an earth shattering roar!
        {demon_name} swipes as you with its clawed paws repeatedly, tearing
        your body to ribbons of bloody flesh. Its fiery eyes burning with mad
        excitement! It slams its body into you knocking you to the ground.

        You pass out.
        """)
        time.sleep(13)

    def virgo_lose():
        print(f"""
        {demon_name} scuttles towards you on all fours, its pale form moving
        fast!
        {demon_name} leaps on top of you, slashing with its clawed hands.
        Surpised by its strength you fall to your knees, screaming in pain as
        it rips your scalp off. It grabs your head and slams it into the
        ground

        You pass out.
        """)
        time.sleep(13)

    def libra_lose():
        print(f"""
        {demon_name} leaps towards you before you can react!
        {demon_name} it impales you on one end of the spike and then proceeds
        to repeatedly throw you against the ground!

        You pass out.
        """)
        time.sleep(13)

    def scorpio_lose():
        print(f"""
        {demon_name} scuttles towards you at an impressive speed!
        {demon_name} backhands you with one of its pincers. Its small black
        eyes burning with mad excitement! It grabs your head with its pincers,
        and squeezes.

        You pass out.
        """)
        time.sleep(13)

    def sagittarius_lose():
        print(f"""
        {demon_name} shoots a spiked arrow into your knee before galloping
        towards you in a blur!
        {demon_name} kicks you in the head with its back leg.

        You pass out.
        """)
        time.sleep(13)
    time.sleep(4)
    if zodiac_list[-1] == "Capricorn":
        capricorn_lose()
    elif zodiac_list[-1] == "Aquarius":
        aquarius_lose()
    elif zodiac_list[-1] == "Pisces":
        pisces_lose()
    elif zodiac_list[-1] == "Aries":
        aries_lose()
    elif zodiac_list[-1] == "Taurus":
        taurus_lose()
    elif zodiac_list[-1] == "Gemini":
        gemini_lose()
    elif zodiac_list[-1] == "Cancer":
        cancer_lose()
    elif zodiac_list[-1] == "Leo":
        leo_lose()
    elif zodiac_list[-1] == "Virgo":
        virgo_lose()
    elif zodiac_list[-1] == "Libra":
        libra_lose()
    elif zodiac_list[-1] == "Scorpio":
        scorpio_lose()
    elif zodiac_list[-1] == "Sagittarius":
        sagittarius_lose()
    final_lose()


def final_lose():
    """
    This function is the final lose function. After it has run, it calls
    the restart function.
    """
    time.sleep(5)
    print(f"""
        You awaken to find {demon_name} has dragged your battered body
        to the archway. You gaze in horror at the swirly fiery vortex
        contained within the archway. Its a portal that opens up above
        a lake of fire. Within the lake of fire, you see millions of
        screaming people writhining in agony, pleading for relief that
        will never come.
        """)
    time.sleep(10)
    print(f"""
        You gaze up at {demon_name} "Please" you beg "Have mercy on my soul"
        """)
    time.sleep(5)
    print(f"""
        {demon_name} looks down at you with zero remorse.
        """)
    time.sleep(5)
    print(f"""
        You have barely a moment to catch your breath to continue
        your begging before {demon_name} hurls you through the archway.
        """)
    time.sleep(6)
    print("""
        Your body passes through the archway and gets dragged down
        by the sudden change in gravity.
        """)
    time.sleep(6)
    print("""
        You fall 50 feet, your flesh crisping the closer you get towards
        the liquid fire of the Tartarean lake.
        """)
    time.sleep(6)
    print("""
        Your body slams into the lake, crushing every bone in your body.
        But in horror you feel the flames piece your bones back together.
        """)
    time.sleep(6)
    print("""
        The fire is excruciating. A never ending cycle of being burnt and
        healed begins. Each breath you take to scream scorches and shrivels
        your lungs. The mass of desperate bodies around you start to pull
        you down in desperate attempt to climb above the flames.
        """)
    time.sleep(12)
    print(f"""
        The last thing you see before being pulled under is the ugly face of
        {demon_name} staring down at you.

        Thus ends the story of {name}'s journey along the Path of Maat!
        """)
    time.sleep(6)
    restart_game()


def win_game():
    """
    If the user gets the sixth choice right, this function runs. The endgame
    function is called at the end. And then the user has the option to play
    again.
    """
    print(f"""
    {demon_name} stares at you in shock!
    """)
    time.sleep(5)
    print("""
    You have done it!
    """)
    time.sleep(5)
    print(f"""
    {demon_name} bows its head and says "You have solved the sacred anagram of
    Maat, redemption is yours"
    """)
    time.sleep(5)
    print(f"""
    {demon_name} dissappears in a flash of fire. In its place stands the
    goddess Maat in all her glory.
    """)
    time.sleep(5)
    print(f"""
    The goddess Maat stands 8 feet tall, garbed in a snowy white kaftan that
    falls to her feet. Her heavily kholed eyes burn with divine light.
    She smiles at you "Dear {name}, you have been through so much! Your trials
    and tribulations have cleansed your soul of its sins.
    You are no longer a hellbound spirit"
    """)
    time.sleep(13)
    print("""
    The goddess Maat continues "By my word I restore you and I give you leave
    to ascend the staircase and find redemption"
    """)
    time.sleep(6)
    print("""
    The goddess vanishes in a flash of white light, but not before you find
    yourself healed. The traumas you have experienced lift themselves from
    your mind and you feel light as feather, no longer weighed down by
    darkness. Your body is strong, healthy and unmarked again.
    """)
    time.sleep(13)
    print("""
    You make your way to the staircase and you start to climb it.
    """)
    time.sleep(6)
    print("""
    With each step you take on the staircase, the memories of hell are erased
    from your mind. Before long you find yourself floating upwards in peaceful
    bliss, the Path of Maat and its trials, forgotten.
    """)
    time.sleep(6)
    end_game()
    print()
    while True:
        print("Answer Y or N")
        restart_choice = input("Would you like to play again? Y/N\n")
        restart = restart_choice.upper()
        if restart == "Y":
            a = ["3", "2", "1"]
            print("The game will begin in 3 seconds...")
            for i in a:
                time.sleep(0.5)
                print(i)
                time.sleep(0.75)
                continue
            run_game()
        elif restart == "N":
            print("""
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


def anagram_checker():
    """
    This function shows the user the sixth choice and it loops to check if the
    anagram answer is correct.
    """
    answer_list = []
    while True:
        print(f"The anagram before you is: {ana_gram}")
        print()
        anagram_var = input("Solve the anagram\n")
        anagram_answer = anagram_var.lower()
        if len(answer_list) < 2:
            if anagram_answer == anagram_correct:
                win_game()
                break
            elif anagram_answer != anagram_correct:
                answer_list.append(anagram_answer)
                print()
                time.sleep(2)
                print(f"""
                {demon_name}: "That is incorrect, pathetic mortal!" """)
                print()
        else:
            final_monster_lose()
            break


def anagram():
    """
    This function holds the three random anagrams and their answers in a
    dictionairy and then gets a random anagram and its answer and makes them
    into global variables.
    """
    global ana_gram
    global anagram_correct
    anagram_dict = {
        "noitemperi": "redemption",
        "ablutionso": "absolution",
        "toxineraone": "exoneration"
    }
    ana_gram = random.choice(list(anagram_dict.keys()))
    anagram_correct = anagram_dict.get(ana_gram,)


def main_sphinx():
    """
    Main function that holds all the sphinx functions. Calls the sphinx
    function.
    """
    def sphinx():
        """
        Carries on from the first part function and leads the first choice
        function
        """
        print()
        print("""
        Allecto raises his eyebrows!!\n
        Whether this is because he is impressed or not, is not clear. With an
        dismissive wave of his hand, he sends you hurtling through darkness…
        """)
        time.sleep(5)
        print()
        print("""
        You open your eyes and find yourself on the one side of a dimly lit
        rectangular room.
        """)
        time.sleep(5)
        print()
        print("""
        You survey the room and notice many broken vases, ornaments and lots
        of nondescript furniture that has seen better days.
        """)
        time.sleep(5)
        print()
        print("""
        Looking down you observe that there also seems to be a lot of pale
        yellow sand in the room.
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
        """
        Presents the user with the first choice. Depending on the users choice
        either the sphinx choice one one function is run or the sphinx choice
        one two function is run. It also checks to make sure the users input
        is the right format answer.
        """
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
                print("I don't understand")
                print("Select A or B!")
                print()

    def sphinx_choice_one_one():
        """
        Additional dialogue that takes place after the sphinx_choice_one
        function and ends with the sphinx choice one two function.
        """
        time.sleep(3)
        print("""
        You make your way to a large aged cabinet, as you open the cabinet
        door, you scream as hundreds of large scarab beetles the size of
        tarantulas, swarm up the wall behind it like a black cloud.
        """)
        time.sleep(5)
        print("""
        You jump back in horror and decide to escape this horrible room!
        """)
        sphinx_choice_one_two()

    def sphinx_choice_one_two():
        """
        Additional dialogue that takes place after the sphinx_choice_one
        function and leads to the sphinx choice two function.
        """
        time.sleep(5)
        print("""
        You rush towards the large stone door. Once there you frantically
        start searcing for a lever or a switch of some kind!
        """)
        time.sleep(5)
        print("""
        Suddenly a horrible smells fills the room and the hairs on your neck
        prickle up
        """)
        time.sleep(5)
        print("""
        You turn and find yourself face to face with the strangest creature
        you have ever laid eyes on, a sphinx!
        Its androgynous face is beautiful, with proud heavily kholed
        blue eyes, high cheekbones and golden skin.
        Atop its head rests a large striped headdress that would have made
        even the wealthiest Pharaoh jealous, in its centre, above the sphinxes
        brow rests the living head of a king cobra attached to the headdress.
        From the neck down, you see a powerfully built leonine body resting
        gracefully on the floor. Each one of its paws bigger than your head.
        """)
        time.sleep(13)
        print("""
        The creature stares at you impassivley, its sharp intelligent eyes
        giving away nothing, waiting for you to make a move. You notice a
        spear on the floor next to you.
        """)
        sphinx_choice_two()

    def sphinx_death():
        """
        If the user gets the riddle wrong enough times, this function is
        called and then the restart game function is called.
        """
        print("""
        The king cobra head spits venom into your eyes, making you scream.
        """)
        time.sleep(7)
        print("""
        The sphinx lunges forward and knocks you backward. She lands on your
        chest crushing your windpipe and ribs beneath her weight.
        """)
        time.sleep(7)
        print("""
        Choking on your blood you see her head splitting open horizonatally
        from the edges of her mouth to her ears, your realize that shes
        opening her horrifyingly wide mouth to reveal rows of
        razor sharp teeth.
        """)
        time.sleep(7)
        print("""
        As you scream, all you hear is the sound of your blood gurgling,
        wetly, in back of your throat. She strikes forward and
        starts devouring you.
        """)
        time.sleep(7)
        print("""
        With dawning horror, you realize because you are already dead,
        there is no end to this as your body knits itself back together
        as quickly as its damaged.
        You pray to be saved but instead you spend the rest of eternity being
        torn open and toyed with by the sphinx.
        """)
        time.sleep(12)
        restart_game()

    def sphinx_choice_two():
        """
        Presents the user with the 3rd choice and runs either sphinx one two
        one function or the sphinx one two two function. Also displays an
        error message if the wrong input takes place.
        """
        time.sleep(5)
        while True:
            print("What do you do?")
            sphinx_choice_two = input("""
            A - Grab the spear and attack the sphinx.
            B - Try to communicate with the sphinx.
            """)
            final_choice = sphinx_choice_two.upper()
            if final_choice == "A":
                sphinx_choice_two_one()
                break
            elif final_choice == "B":
                sphinx_choice_two_two()
                break
            else:
                time.sleep(2)
                print()
                print("I don't understand")
                print("Select A or B!")
                print()
                continue

    def sphinx_choice_two_one():
        """
        The function thats called if the user selects A and it ends with the
        sphinx death function.
        """
        print("""
        You quickly grab the spear before the sphinx has time to react.
        """)
        time.sleep(5)
        print("""
        With a war cry that reeks of fear, you rush forward, aiming for the
        heart!
        """)
        time.sleep(5)
        print("""
        The sphinx lazily swipes at your spear, knocking it out of your hand!
        """)
        time.sleep(5)
        sphinx_death()

    def sphinx_choice_two_two():
        """
        The function thats called if the user selects B and it ends with the
        sphinx riddle function.
        """
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
        You nod, frozen in fear. You ask “What now?”
        """)
        time.sleep(5)
        print("""
        The sphinx continues “Answer my riddle correctly and you may move
        along the path of the goddess Maat”
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
        """
        The function that presents the user with choice 3 which is a riddle
        with three possible answers of which only one is correct. Each time
        the user answers incorrectly, the answerr is appended to an empty list
        Once the list has 3 values the sphinx death function takes place.
        If the user gets the answer correct before there are three values
        in the list, the sphinx final function is called and the loop is
        broken.
        """
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
                    The sphinx is growing restless.
                    Better get it right next time
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
                    break

    def sphinx_final():
        """
        The function contains dialogue then finishes.
        """
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
        It informs you, that you may continue your journey along the Path of
        Maat.
        """)
        time.sleep(5)
        print("""
        You slowly back away from the sphinx, until you reach the doorway
        then you turn and run as fast as you can.
        """)
        time.sleep(5)
    sphinx()


def vampire():
    """
    Level two function that is not called. When I have enough time I will
    expand on the story and introduce more levels
    """
    print("""
    After wondering down a dark tunnel for what feels like an eternity,
    you find yourself in a cold, creepy church
    """)


def run_game():
    """
    Main function that contains all the essential functions for the game and
    runs them in a specific order.
    """
    intro()
    time.sleep(2)
    print()
    get_user_data()
    print()
    time.sleep(1)
    first_part()
    last_part()


#run_game()
end_game()
