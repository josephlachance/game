import random
import time

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
    def __init__(self, description, choices, look_description):
        self.description = description
        self.choices = choices
        self.look_description = look_description


    def enter(self):
        print(self.description)
        while True:
            action = input("\nWhat do you want to do?")
            if "look" in action:
                print(self.look_description)
            elif "inventory" in action:
                print (Player.inventory)
                break
            else:
                print("Nah mang")



def enter():
    input("Press Enter to continue... ")

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

def intro():
    print("Welcome to the game. Joseph LaChance made this game. ")
    input("Press Enter to continue...")
    print("Lets get started.")
    name = input("What is your name? ")
    print(f"Welcome {name} You must now think long and hard about the next question.")
    sign = input("What is your sign? The of the Sun, That of the Moon, Or that of the Star?").lower()
    while sign not in valid_signs:
        print("That is not a valid sign. Please choose from Sun, Moon, or Star")
        sign = input("What is your sign? ").lower()
    print(f"You have chosen {sign}! ")
    
    enter()
    print(f"\nNow. {name}. Your journey begins at dawn. Get some rest")
    enter()


tavern = Scene(
        description="You are in a warm bustling tavern",
        choices=[],
        look_description="""
        There a number of patrons enjoying their drinks and talking amongst them.
        A woman is sitting alone however, covered in a dark hood that resembles a clan
        that you've heard of, but not entirely sure.
        
        The bartender is looking at you now as check the surroundings. What would like to do?
        """
    )

#GAME BEGINS
intro()
tavern.enter()