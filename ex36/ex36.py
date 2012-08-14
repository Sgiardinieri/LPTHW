from sys import exit

def atm():
    print "First, let's go to the ATM and see what kind of a shopper you truly are!"
    print "Are you a Splurger or a Budgeter?"
    print "How much money shall you be removing from the ATM?"

    next = raw_input("> ")
    try:
        how_much = int(next)
    except ValueError:
        dead("Seriously, this is shopping! Type a number.")

    if how_much < 500:
        print "EEEKKK!! Time to budget, let's hit the mall anyways!!!"
        shopping_mall()
        
    elif how_much > 500:
        print "That's my kind of shopping.. Off to the mall!!"
        shopping_mall()



def alligator_room():
    print "Ohhh No!! There is a alligator here."
    print "The alligator has a bunch of friends."
    print "How are you going to move the alligators? You can either taunt alligator or lure them with food."
    alligator_moved = False

    while True:
        next = raw_input("> ")

        if next == "lure them with food":
            dead("The alligator looks at you then chews your face off, the end.")
        elif next == "taunt alligator" and not alligator_moved:
            print "The alligator has moved from the door. You can now open the door."
            alligator_moved = True
        elif next == "taunt alligator" and alligator_moved:
            dead("The alligator gets mad and chews your leg off.")
        elif next == "open the door" and alligator_moved:
            starbucks()
        else:
            print "You're an idiot, the alligators are now angry and ripped you to shreds."
            exit(0)


def shopping_mall():
    print "Here you see all of the beautiful shops..."
    print "Full of diamonds, clothes, and shoes!"
    print "Which will you be shopping for today?"

    next = raw_input("> ")

    if "clothes" in next:
        start()
    elif "diamonds" in next:
        	exit("Ohh La La!!! You're a winner just for your impeccable taste!!")
    else:
       	print "Hi ho, hi ho, off to the shoe store you go..."
        alligator_room()    
            
def starbucks():
    print "Phew, With all of that shopping, you must be thirtsty! Let's go to Starbucks!!!"
    print "You can order Coffee, Tea, or Water"
    print "Which will you be drinking today?"

    next = raw_input("> ")

    if "Coffee" in next:
        	exit("Yeah!! Get that energy up! Great shopping today!!")
    elif "Tea" in next:
        	exit("What are you sick? Go home and try to be a real shopper another day!")
    elif "Water" in next:
        	exit("Who goes to Starbucks for water. Go home!!")
    else:
        	exit("Seriously, You're dehydrated and now you die!")


def dead(why):
    print why
    exit(0)

def start():
    print "Wonderful shopping, lets head to the dressing room to see what we like..."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        alligator_room()
    elif next == "right":
       starbucks()
    else:
       dead("You are too indecisive, you're dead because you can't even pick a door!!")


atm()