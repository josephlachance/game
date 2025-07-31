import random


player_stats = {
    "health": 100,
    "armor class" : 10,
    "strength" : 10,
    "magic" : 10,
    "luck" : 5
}

def player_attack(attacker, defender):
    print(f"\n{name} swings an attack! at Enemy")
    roll = random.randint(1,20)
    if roll >= defender["armor class"]:
        print("Hit")
    else:
        print("Miss!")

def npc_speak(name, line):
    print("\n---" + name.upper() + "---")
    print("> " + line + "\n")
    input("Continue....\n")

def choice_yn(prompt):
    #Prompt means that 
    while True:
        answer = input(prompt + " Yes or No? ").lower()
        if answer in ["yes","y"]:
            return True
        elif answer in ["no","n"]:
            return False
        else:
            print("Please answer Yes or No")



#Function Definitions
def dark_knight_path():
    npc_speak("Dark Knight", "I am afraid I must ask something of you, brave one.")
    if  player_stats["strength"] > 10:
        npc_speak("Dark Knight", "You seem stronger than the rest.")
        if choice_yn("> Care to challenge me to a friendly game?"):
            print("You accept the challenge")
            print("\nThe Dark Knight laughs softly.")
            npc_speak("Dark Knight", "I challenge you to land one hit on me. If you do you may pass. However, if you do not. You must do me a...favor.")
        else:
            print("You decline")

    else:
        npc_speak("Dark Knight", "I must ask you to buy another drink before leaving. Its dangerous out there in Waede. ")   

def hidden_path():
    print(">inside you see some shit. You find a sword")


#GAME BEGINS
print("Hello, World!")
# I am just trying to figure shit out.
input("\nPress Enter please")
print("First thing is first... ")
name=input('What is your name? ')
print(f"Hello {name}. Your adventure will begin soon. But I have a few more questions for you.")
print("\nWhat is your sign. You may only choose from the following: Sun, Moon, Star")
valid_signs=["sun", "moon", "star"] #usable signs
sign=input("Please enter your chosen sign ").lower()
while sign not in valid_signs: #This will determine the players stats once they choose their sign.
    print("Im sorry that is not a valid sign, please type a valid sign from the list. Sun, Moon, or Star ")
    sign=input("Please enter your chosen sign ")
print(f"Thank you, you have chosen {sign}")
if sign == "moon":
    player_stats["luck"] += 5
elif sign == "sun":
    player_stats["strength"] += 5
elif sign == "star":
    player_stats["magic"] += 5
input("\nContinue... ")
print("You begin your journey in a tavern.")
print("\nYou look around and see a bartender cleaning some glasses.")
print("\nA woman is sitting alone ")
if player_stats["luck"] == 10:
    print("\nyou see a crack of light from the wall. Perhaps some sort of hidden door.")
choice=input("\nWhat would you like to do? ").lower()
if "lady" in choice:
    print("You walk over to the lady...")
elif "bartender" in choice:
    print("The bartender looks at you and asks you what will you have?")
    bartender_path #create a bartender path
elif "hidden door" in choice:
    print("You manage to walk over to the wall and get close to the door. You give it a push and the door opens.")
    hidden_path #teehee!
elif "exit" in choice:
    print("You turn towards the exit. However, you're blocked as a tall mysterious figure approaches the door from the outside.")
    input("\nContinue...")
    dark_knight_path()

