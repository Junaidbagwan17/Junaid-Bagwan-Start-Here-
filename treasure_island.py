print("Welcome to the treasure island !")
print("mission is to find a treasure on island")

road= input("your at crossroad where do you want to go 'left or 'right'\n").lower()

if road == "left":
    lake = input("you come to a lake , type 'wait' , 'swim' .\n").lower()
    if lake == "wait":
        house = input("there is house with 3 doors 'blue' ,'yellow', 'red'\n").lower()
        if house == "yellow":
            print("congratulations, you found a treasuer,you win\n")
        elif house == "blue":
            print("you reaced at atlantic ,game over\n")
        elif house == "red":
            print("you go into rooom which is full of fire ,game over\n")
        else:
            print("you typed somehing wrong ,game over\n")
    else:
        print("you have got attacked by angry shark , game over\n")
else:
    print(" game over")
s
