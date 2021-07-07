print("--- Noughts and Crosses ---")
print(" ")
print("the commands to place your pieces are as follow:")
print(" ")
print(" " + "top left   " + " | " + "top middle   " + " | " + "top right   " + " ")
print("------------------------------------------")
print(" " + "middle left" + " | " + "middle middle" + " | " + "middle right " + " ")
print("------------------------------------------")
print(" " + "bottom left" + " | " + "bottom middle" + " | " + "bottom right" + " ")
print(" ")
print(" ")
print(" ")

check = 2
check2 = 0

topLeft = " "
topMiddle = " "
topRight = " "
middleLeft = " "
middleMiddle = " "
middleRight = " "
bottomLeft = " "
bottomMiddle = " "
bottomRight = " "

def playerOne():
    if topLeft == "X" and topMiddle == "X" and topRight == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topLeft == "X" and middleMiddle == "X" == "X" and bottomRight == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topLeft == "X" and middleLeft == "X" and bottomLeft == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topMiddle == "X" and middleMiddle == "X" and bottomMiddle == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topRight == "X" and middleRight == "X" and bottomRight == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if middleLeft == "X" and middleMiddle == "X" and middleRight == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

    if bottomLeft == "X" and bottomMiddle == "X" and bottomRight == "X":
        print(" ")
        print(" ")
        print("--- Player One Wins! ---")
        print(" ")
        print(" ")
        quit()

def playerTwo():
    if topLeft == "O" and topMiddle == "O" and topRight == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topLeft == "O" and middleMiddle == "O" and bottomRight == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topLeft == "O" and middleLeft == "O" and bottomLeft == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topMiddle == "O" and middleMiddle == "O" and bottomMiddle == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if topRight == "O" and middleRight == "O" and bottomRight == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if middleLeft == "O" and middleMiddle == "O" and middleRight == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

    if bottomLeft == "O" and bottomMiddle == "O" and bottomRight == "O":
        print(" ")
        print(" ")
        print("--- Player Two Wins! ---")
        print(" ")
        print(" ")
        quit()

def bourd():
    print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
    print("-----------")
    print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
    print("-----------")
    print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

bourd()

while check2 < 1:
    check2 = 0
    firstGo = input("Player one's first go: ")
    firstGo = firstGo.lower()

    if firstGo == "top left":
        topLeft = "X"
        check2 = check + 1
    if firstGo == "top middle":
        topMiddle = "X"
        check2 = check + 1
    if firstGo == "top right":
        topRight = "X"
    if firstGo == "middle left":
        middleLeft = "X"
        check2 = check + 1
    if firstGo == "middle middle":
        middleMiddle = "X"
        check2 = check + 1
    if firstGo == "middle right":
        middleRight = "X"
        check2 = check + 1
    if firstGo == "bottom left":
        bottomLeft = "X"
        check2 = check + 1
    if firstGo == "bottom middle":
        bottomMiddle = "X"
        check2 = check + 1
    if firstGo == "bottom right":
        bottomRight = "X"
        check2 = check + 1

bourd()

while check2 < 1:
    check2 = 0
    secondGo = input("Player two's first go: ")
    secondGo = secondGo.lower()

    if secondGo == "top left":
        topLeft = "O"
    if secondGo == "top middle":
        topMiddle = "O"
    if secondGo == "top right":
        topRight = "O"
    if secondGo == "middle left":
        middleLeft = "O"
    if secondGo == "middle middle":
        middleMiddle = "O"
    if secondGo == "middle right":
        middleRight = "O"
    if secondGo == "bottom left":
        bottomLeft = "O"
    if secondGo == "bottom middle":
        bottomMiddle = "O"
    if secondGo == "bottom right":
        bottomRight = "O"

bourd()

while check2 < 1:
    check2 = 0
    thirdGo = input("Player one's second go: ")
    thirdGo = thirdGo.lower()

    if thirdGo == "top left":
        topLeft = "X"
    if thirdGo == "top middle":
        topMiddle = "X"
    if thirdGo == "top right":
        topRight = "X"
    if thirdGo == "middle left":
        middleLeft = "X"
    if thirdGo == "middle middle":
        middleMiddle = "X"
    if thirdGo == "middle right":
        middleRight = "X"
    if thirdGo == "bottom left":
        bottomLeft = "X"
    if thirdGo == "bottom middle":
        bottomMiddle = "X"
    if thirdGo == "bottom right":
        bottomRight = "X"

bourd()

while check2 < 1:
    check2 = 0
    fourthGo = input("PLayer two's second go: ")
    fourthGo = fourthGo.lower()

    if fourthGo == "top left":
        topLeft = "O"
    if fourthGo == "top middle":
        topMiddle = "O"
    if fourthGo == "top right":
        topRight = "O"
    if fourthGo == "middle left":
        middleLeft = "O"
    if fourthGo == "middle middle":
        middleMiddle = "O"
    if fourthGo == "middle right":
        middleRight = "O"
    if fourthGo == "bottom left":
        bottomLeft = "O"
    if fourthGo == "bottom middle":
        bottomMiddle = "O"
    if fourthGo == "bottom right":
        bottomRight = "O"

bourd()

while check2 < 1:
    check2 = 0
    fifthGo = input("Player one's third go: ")
    fifthGo = fifthGo.lower()

    if fifthGo == "top left":
        topLeft = "X"
    if fifthGo == "top middle":
        topMiddle = "X"
    if fifthGo == "top right":
        topRight = "X"
    if fifthGo == "middle left":
        middleLeft = "X"
    if fifthGo == "middle middle":
        middleMiddle = "X"
    if fifthGo == "middle right":
        middleRight = "X"
    if fifthGo == "bottom left":
        bottomLeft = "X"
    if fifthGo == "bottom middle":
        bottomMiddle = "X"
    if fifthGo == "bottom right":
        bottomRight = "X"

playerOne()

bourd()

while check2 < 1:
    check2 = 0
    sixthGo = input("Player two's third go: ")
    sixthGo = sixthGo.lower()

    if sixthGo == "top left":
        topLeft = "O"
    if sixthGo == "top middle":
        topMiddle = "O"
    if sixthGo == "top right":
        topRight = "O"
    if sixthGo == "middle left":
        middleLeft = "O"
    if sixthGo == "middle middle":
        middleMiddle = "O"
    if sixthGo == "middle right":
        middleRight = "O"
    if sixthGo == "bottom left":
        bottomLeft = "O"
    if sixthGo == "bottom middle":
        bottomMiddle = "O"
    if sixthGo == "bottom right":
        bottomRight = "O"

playerTwo()

bourd()

while check2 < 1:
    check2 = 0
    seventhGo = input("Player one's forth go: ")
    seventhGo = seventhGo()

    if seventhGo == "top left":
        topLeft = "X"
    if seventhGo == "top middle":
        topMiddle = "X"
    if seventhGo == "top right":
        topRight = "X"
    if seventhGo == "middle left":
        middleLeft = "X"
    if seventhGo == "middle middle":
        middleMiddle = "X"
    if seventhGo == "middle right":
        middleRight = "X"
    if seventhGo == "bottom left":
        bottomLeft = "X"
    if seventhGo == "bottom middle":
        bottomMiddle = "X"
    if seventhGo == "bottom right":
        bottomRight = "X"

playerOne()

bourd()

while check2 < 1:
    check2 = 0
    eighthGo = input("Player two's forth go: ")
    eighthGo = eighthGo.lower()

    if eighthGo == "top left":
        topLeft = "O"
    if eighthGo == "top middle":
        topMiddle = "O"
    if sixthGo == "top right":
        topRight = "O"
    if eighthGo == "middle left":
        middleLeft = "O"
    if eighthGo == "middle middle":
        middleMiddle = "O"
    if eighthGo == "middle right":
        middleRight = "O"
    if eighthGo == "bottom left":
        bottomLeft = "O"
    if eighthGo == "bottom middle":
        bottomMiddle = "O"
    if eighthGo == "bottom right":
        bottomRight = "O"

playerTwo()

bourd()

while check2 < 1:
    check2 = 0
    ninethGo = input("Player one's fifth go: ")
    ninethGo = ninethGo.lower()

    if ninethGo == "top left":
        topLeft = "X"
    if ninethGo == "top middle":
        topMiddle = "X"
    if ninethGo == "top right":
        topRight = "X"
    if ninethGo == "middle left":
        middleLeft = "X"
    if ninethGo == "middle middle":
        middleMiddle = "X"
    if ninethGo == "middle right":
        middleRight = "X"
    if ninethGo == "bottom left":
        bottomLeft = "X"
    if ninethGo == "bottom middle":
        bottomMiddle = "X"
    if ninethGo == "bottom right":
        bottomRight = "X"

playerOne()

bourd()
