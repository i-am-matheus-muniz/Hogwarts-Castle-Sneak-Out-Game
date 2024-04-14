import random

def stage_one():
    print("\nStage One: Select an magic object to help you.")
    print("Choose one of the following magical objects:")
    print("1. Marauders Map")
    print("2. Howler")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        print("You've chosen the Marauders Map that will help you getting through the castle!")
        return True
    else:
        print("The Howler starts to scream about how could you not get the MARAUDERS MAP instead of the Howler. You've been discovered by Filch. Game Over.")
        return False

def stage_two():
    print("\nStage Two: Pick a way at Hogwarts to sneak out from the castle.")
    print("Choose one of the following ways:")
    print("1. Main Hall")
    print("2. Gardens")
    choice = input("Enter the number of your choice: ")
    if choice == '2':
        print("Nice! Sneaking out through the Gardens seems to be the right choice.")
        return True
    else:
        print("As you made your way through the Main Hall, Filch was there petting Mrs Norris. You've been discovered by Filch. Game Over.")
        return False

def stage_three():
    print("\nStage Three: After finding a potential enemy, pick an option that will permit you to continue.")
    print("You've encountered a Prefect patrolling the corridors.")
    print("Choose one of the following options:")
    print("1. Use the Invisibility Cloak to hide and sneak past quietly.")
    print("2. Try to distract the Prefect with a charm.")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        print("Using the Invisibility Cloak to hide was the right choice. You passed through him without being discovered!")
        return True
    else:
        print("The Prefect tells it's not time for a student to be out of the bed. He calls Filch. Game Over.")
        return False

def stage_four():
    print("\nStage Four: The player found Peeves! He will need to choose a spell to get out of this situation.")
    print("Choose one of the following spells:")
    print("1. Lumos")
    print("2. Petrificus Totalus")
    choice = input("Enter the number of your choice: ")
    if choice == '2':
        print("Well done! Petrificus Totalus immobilized Peeves, allowing you to escape.")
        return True
    else:
        print("Peeves alerted Filch! You've been caught. Game Over.")
        return False

def main():
    print("Welcome to the Hogwarts Castle Sneak Out Game!")
    print("This is a 4 stages choice game, where based on your choices it will detemine if you can sneak out at night from the Hogwarts castle.")
    print("But if Filch catches you... You will be in SERIOUS trouble.")
    if not stage_one():
        return
    if not stage_two():
        return
    if not stage_three():
        return
    if not stage_four():
        return
    
    print("\nCongratulations! You managed to sneak out from the Hogwwarts castle safely!")

if __name__ == "__main__":
    main()
