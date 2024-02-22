import time
import random
import pyttsx3

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

a=pyttsx3.init()

def display_intro():
    print(Colors.YELLOW + "Welcome to the Haunted Mansion Adventure!" + Colors.END)
    a.say("Welcome to the Haunted Mansion Adventure!")
    a.runAndWait()
    print("You find yourself standing in front of a mysterious mansion...")
    print("Legend has it that a valuable treasure is hidden inside, but beware of the dangers lurking within!")
    print( "Are you brave enough to enter")

def choose_path():
    path = "" 
    while path != "1" and path != "2":
        print(Colors.RED + "Which path will you choose? (1 or 2)" + Colors.END)
        a.say("Which path will you choose? (1 or 2)")
        a.runAndWait()
        path = input("> ")
    return path

def check_path(chosen_path):
    print(Colors.GREEN + "You cautiously proceed down the path..." + Colors.END)
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(Colors.GREEN + "You hear a strange noise behind you!" + Colors.END)
    time.sleep(2)
    print(Colors.GREEN + "You turn around but there's nothing there." + Colors.END)
    time.sleep(2)
    print(Colors.GREEN + "You continue on your path..." + Colors.END)
    time.sleep(2)
    correct_path = random.randint(1, 2)
    if chosen_path == str(correct_path):
        print(Colors.YELLOW + "Congratulations! You've chosen the right path." + Colors.END)
        a.say("Congratulations! You've chosen the right path.")
        a.runAndWait()
        print(Colors.YELLOW + "You arrive safely in the mansion's foyer." + Colors.END)
    else:
        print(Colors.BLUE + "Uh-oh! You've chosen the wrong path..." + Colors.END)
        print(Colors.BLUE + "Suddenly, the ground gives way beneath you!" + Colors.END)
        time.sleep(2)
        print(Colors.BLUE + "You fall into a dark pit and your adventure comes to a tragic end." + Colors.END)
        print(Colors.BLUE + "Game Over." + Colors.END)
        a.say("Game Over.")
        a.runAndWait()

def explore_foyer():
    print(Colors.GREEN + "You are now in the mansion's foyer." + Colors.END)
    print(Colors.GREEN + "You see two doors in front of you." + Colors.END)
    print(Colors.GREEN + "One door is marked 'Library' and the other is marked 'Dining Room'." + Colors.END)
    time.sleep(2)
    print(Colors.RED + "Which door will you choose? (Type 'library' or 'dining room')" + Colors.END)
    a.say("Which door will you choose? (Type 'library' or 'dining room')")
    a.runAndWait()
    door_choice = input("> ").lower()
    if door_choice == "library":
        explore_library()
    elif door_choice == "dining room":
        explore_dining_room()
    else:
        print("Invalid choice. Please try again.")
        explore_foyer()

def explore_library():
    print(Colors.RED + "You enter the library and see rows of dusty books." + Colors.END)
    print(Colors.RED + "In the dim light, you notice a glimmering object on one of the shelves." + Colors.END)
    time.sleep(2)
    print(Colors.YELLOW +"It's the treasure!" + Colors.END)
    time.sleep(2)
    print(Colors.GREEN + "Congratulations! You've found the hidden treasure." + Colors.END)
    a.say("Congratulations! You've found the hidden treasure.")
    a.runAndWait()
    print(Colors.GREEN + "You win!" + Colors.END)
    a.say("You win!")
    a.runAndWait()

def explore_dining_room():
    print(Colors.YELLOW + "You enter the dining room and see a long table set for a feast." + Colors.END)
    print(Colors.YELLOW + "You notice a key on the table." + Colors.END)
    time.sleep(2)
    print(Colors.YELLOW + "You pick up the key and wonder what it unlocks..." + Colors.END)
    time.sleep(2)
    print(Colors.BLUE + "As you turn around, you hear a loud noise behind you!" + Colors.END)
    time.sleep(2)
    print(Colors.BLUE + "You see a ghostly apparition hovering in front of you!" + Colors.END)
    time.sleep(2)
    print(Colors.GREEN + "You use the key to unlock the nearby door and escape the room." + Colors.END)
    print(Colors.GREEN + "You're safe for now..." + Colors.END)
    a.say("You're safe for now...")
    a.runAndWait()

def play_game():
    display_intro()
    chosen_path = choose_path()
    check_path(chosen_path)
    explore_foyer()

play_game()
