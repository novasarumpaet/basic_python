print("========================")
print("Here is my car game guys")
print("========================")
print("Start - Stop - Help - Quit")

print("\n")
ch = ""
started = False

while True:
    ch = input("> ").lower()
    if ch == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("car started...")
    elif ch == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped...")
    elif ch == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to exit this game
        """)
    elif ch == "quit":
        print("Thanks for playing this game")
        break
    else:
        print("Sorry, your input is not detected")