
print("==============================")
print("       TREASURE HUNT")
print("==============================")

name = input("Enter your name: ")

print("\nWelcome,", name)
print("You are inside a mysterious cave.")
print("Your mission is to find the hidden treasure!")

print("\nYou see two paths.")
print("1. Go left")
print("2. Go right")

choice = input("Which path do you choose? ")

if choice == "1":
    print("\nYou found a sleeping dragon!")

    print("1. Fight the dragon")
    print("2. Run away")

    action = input("What will you do? ")

    if action == "1":
        print("\nThe dragon defeated you!")
        print("GAME OVER!")

    elif action == "2":
        print("\nYou escaped safely!")
        print("But you found no treasure.")

    else:
        print("\nInvalid choice!")

elif choice == "2":
    print("\nYou found a treasure chest!")

    print("1. Open the chest")
    print("2. Ignore the chest")

    action = input("What will you do? ")

    if action == "1":
        print("\nCONGRATULATIONS!")
        print("You found 1000 gold coins!")
        print("YOU WIN!")

    elif action == "2":
        print("\nYou walked away from the treasure.")
        print("GAME OVER!")

    else:
        print("\nInvalid choice!")

else:
    print("\nInvalid choice!")
    print("GAME OVER!")

print("\nThanks for playing!")
