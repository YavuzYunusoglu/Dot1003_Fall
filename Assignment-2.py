print("Welcome to the Simple Adventure Game!")

def right_choice():
    print("You find a treasure chest!")
    print("Open it and find some gold coins!")

def left_choice():
    print("There is a wild cat licking his paws. Better to be avoid.")

def idle_choice():
    print("You can't start an adventure by waiting.")
    print("You're boring...")

def start_adventure():
    choice = input("Please make a choice -> idle, left, right: ")
    if(str.lower(choice) == "left"):
        left_choice()
    elif(str.lower(choice) == "right"):
        right_choice()
    elif(str.lower(choice) == "idle"):
        idle_choice()
    else:
        print("invalid Input")
        start_adventure()

start_adventure()
