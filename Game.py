import random

valid_signs=["sun", "moon", "star"] #usable signs


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.level = 1
        self.health = 100
        self.armor_class = 10
        self.strength = 10 
        self.magic = 10
        self.luck = 5
        self.sign = sign
        self.inventory = []
        self.apply_sign_bonus()
        self.exp = 0
    def apply_sign_bonus(self):
        if self.sign == "sun":
            self.strength += 5
        elif self.sign == "moon":
            self.magic += 5
        elif self.sign == "star":
            self.luck += 5

class Scene:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices
    def enter(self):
        print("\nEnd of this path.")
        return None
    def


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
    if  player.strength > 10:
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
sign=input("Please enter your chosen sign ").lower()
while sign not in valid_signs: #This will determine the players stats once they choose their sign.
    print("Im sorry that is not a valid sign, please type a valid sign from the list. Sun, Moon, or Star ")
    sign=input("Please enter your chosen sign ")
print(f"Thank you, you have chosen {sign.capitalize()}")
input("\nContinue... ")

player = Player(name, sign)
scene = Scene(description, choices)


scene.description("You've awaken in a tavern. You dont remember how you got here but you've got a splitting headache."
                  )

if player.luck == 10:
    print("\nyou see a crack of light from the wall. Perhaps some sort of hidden door.")
while True:
    choice=input("\nWhat would you like to do? (Bartender, Woman, Exit) ").lower()
    if "lady" in choice or "woman" in choice:
        print("You walk over to the lady...")
        input("\nContinue...")
        break
    elif "bartender" in choice:
        print("The bartender looks at you and asks you what will you have?")
        break
    #create a bartender path
    elif "hidden door" in choice:
        print("You manage to walk over to the wall and get close to the door. You give it a push and the door opens.")
        hidden_path #teehee!
        break
    elif "exit" in choice:
        print("You turn towards the exit. However, you're blocked as a tall mysterious figure approaches the door from the outside.")
        input("\nContinue...")
        dark_knight_path()
        break
    else:
        print("Please choose a valid choice!")

