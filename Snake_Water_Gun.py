#TO MAKE "SNAKE WATER GUN"
#IT IS A GAME
import random
print("Enter via SNAKE OR WATER OR GUN")
count = 0
win = 0
draw = 0

p1 =["SNAKE","WATER","GUN"]
print("0-snake")
print("0-water")
print("0-gun")
while count<5:
    print("*****TURN-", str(count + 1), "*******")
    cp =random.randint(0,2)

    u=int(input("Please enter valid no."))
    while u>2 or u<0:
        print("Your input is invalid")
        u=int(input("Please insert again"))
    print("your choice:",[u])
    print("computer's choice:",[cp])
    if(u==cp):
        print("Draw")
        draw+=1
    else:
        if u==0:
            if cp==1:
                print("You win the game")
                win +=1
            elif cp==2:
                print("You lost the game")
        elif u==1:
            if cp == 0:
                print("You lost the game")
            elif cp == 2:
                print("You win the game")
                win += 1

        elif u==2:
            if cp == 0:
                print("You win the game")
                win += 1
            elif cp == 1:
                print("You lost the game")

    count +=1
    print("***********RESULT***********")
print("You win:",str(win))
print("Computer Win:",str(5-win-draw))
print("No. of draw:",str(draw))







