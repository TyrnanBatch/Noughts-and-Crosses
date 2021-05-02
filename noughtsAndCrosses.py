print("--- Noughts and Crosses ---")
print(" ")
print("the commands to place your pieces are as follow:")
print(" ")
print(" " + "Top Left   " + " | " + "Top Middle   " + " | " + "Top Right   " + " ")
print("------------------------------------------")
print(" " + "Middle Left" + " | " + "Middle Middle" + " | " + "Middle Left " + " ")
print("------------------------------------------")
print(" " + "Bottom Left" + " | " + "Bottom Middle" + " | " + "Bottom Right" + " ")
print(" ")
print(" ")
print(" ")

check = 2

topLeft = " "
topMiddle = " "
topRight = " "
middleLeft = " "
middleMiddle = " "
middleRight = " "
bottomLeft = " "
bottomMiddle = " "
bottomRight = " "

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

firstGo = input("Player one's first go: ")

if firstGo == "Top Left":
    topLeft = "X"
if firstGo == "Top Middle":
    topMiddle = "X"
if firstGo == "Top Right":
    topRight = "X"
if firstGo == "Middle Left":
    middleLeft = "X"
if firstGo == "Middle Middle":
    middleMiddle = "X"
if firstGo == "Middle Right":
    middleRight = "X"
if firstGo == "Bottom Left":
    bottomLeft = "X"
if firstGo == "Bottom Middle":
    bottomMiddle = "X"
if firstGo == "Bottom Right":
    bottomRight = "X"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

secondGo = input("Player two's first go: ")

if secondGo == "Top Left":
    topLeft = "O"
if secondGo == "Top Middle":
    topMiddle = "O"
if secondGo == "Top Right":
    topRight = "O"
if secondGo == "Middle Left":
    middleLeft = "O"
if secondGo == "Middle Middle":
    middleMiddle = "O"
if secondGo == "Middle Right":
    middleRight = "O"
if secondGo == "Bottom Left":
    bottomLeft = "O"
if secondGo == "Bottom Middle":
    bottomMiddle = "O"
if secondGo == "Bottom Right":
    bottomRight = "O"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

thirdGo = input("Player one's second go: ")

if thirdGo == "Top Left":
    topLeft = "X"
if thirdGo == "Top Middle":
    topMiddle = "X"
if thirdGo == "Top Right":
    topRight = "X"
if thirdGo == "Middle Left":
    middleLeft = "X"
if thirdGo == "Middle Middle":
    middleMiddle = "X"
if thirdGo == "Middle Right":
    middleRight = "X"
if thirdGo == "Bottom Left":
    bottomLeft = "X"
if thirdGo == "Bottom Middle":
    bottomMiddle = "X"
if thirdGo == "Bottom Right":
    bottomRight = "X"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

fourthGo = input("PLayer two's second go: ")

if fourthGo == "Top Left":
    topLeft = "O"
if fourthGo == "Top Middle":
    topMiddle = "O"
if fourthGo == "Top Right":
    topRight = "O"
if fourthGo == "Middle Left":
    middleLeft = "O"
if fourthGo == "Middle Middle":
    middleMiddle = "O"
if fourthGo == "Middle Right":
    middleRight = "O"
if fourthGo == "Bottom Left":
    bottomLeft = "O"
if fourthGo == "Bottom Middle":
    bottomMiddle = "O"
if fourthGo == "Bottom Right":
    bottomRight = "O"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

fifthGo = input("Player one's third go: ")

if fifthGo == "Top Left":
    topLeft = "X"
if fifthGo == "Top Middle":
    topMiddle = "X"
if fifthGo == "Top Right":
    topRight = "X"
if fifthGo == "Middle Left":
    middleLeft = "X"
if fifthGo == "Middle Middle":
    middleMiddle = "X"
if fifthGo == "Middle Right":
    middleRight = "X"
if fifthGo == "Bottom Left":
    bottomLeft = "X"
if fifthGo == "Bottom Middle":
    bottomMiddle = "X"
if fifthGo == "Bottom Right":
    bottomRight = "X"

if topLeft and topMiddle and topRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleLeft and bottomLeft == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topMiddle and middleMiddle and bottomMiddle == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topRight and middleRight and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if middleLeft and middleMiddle and middleRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if bottomLeft and bottomMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

sixthGo = input("Player two's third go: ")

if sixthGo == "Top Left":
    topLeft = "O"
if sixthGo == "Top Middle":
    topMiddle = "O"
if sixthGo == "Top Right":
    topRight = "O"
if sixthGo == "Middle Left":
    middleLeft = "O"
if sixthGo == "Middle Middle":
    middleMiddle = "O"
if sixthGo == "Middle Right":
    middleRight = "o"
if sixthGo == "Bottom Left":
    bottomLeft = "O"
if sixthGo == "Bottom Middle":
    bottomMiddle = "O"
if sixthGo == "Bottom Right":
    bottomRight = "O"

if topLeft and topMiddle and topRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleMiddle and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleLeft and bottomLeft == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topMiddle and middleMiddle and bottomMiddle == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topRight and middleRight and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if middleLeft and middleMiddle and middleRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if bottomLeft and bottomMiddle and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

seventhGo = input("Player one's forth go: ")

if seventhGo == "Top Left":
    topLeft = "X"
if seventhGo == "Top Middle":
    topMiddle = "X"
if seventhGo == "Top Right":
    topRight = "X"
if seventhGo == "Middle Left":
    middleLeft = "X"
if seventhGo == "Middle Middle":
    middleMiddle = "X"
if seventhGo == "Middle Right":
    middleRight = "X"
if seventhGo == "Bottom Left":
    bottomLeft = "X"
if seventhGo == "Bottom Middle":
    bottomMiddle = "X"
if seventhGo == "Bottom Right":
    bottomRight = "X"

if topLeft and topMiddle and topRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleLeft and bottomleft == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topMiddle and middleMiddle and bottomMiddle == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topRight and middleRight and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if middleLeft and middleMiddle and middleRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if bottomLeft and bottomMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

eighthGo = input("Player two's forth go: ")

if eighthGo == "Top Left":
    topLeft = "O"
if eighthGo == "Top Middle":
    topMiddle = "O"
if sixthGo == "Top Right":
    topRight = "O"
if eighthGo == "Middle Left":
    middleLeft = "O"
if eighthGo == "Middle Middle":
    middleMiddle = "O"
if eighthGo == "Middle Right":
    middleRight = "O"
if eighthGo == "Bottom Left":
    bottomLeft = "O"
if eighthGo == "Bottom Middle":
    bottomMiddle = "O"
if eighthGo == "Bottom Right":
    bottomRight = "O"

if topLeft and topMiddle and topRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleMiddle and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleLeft and bottomLeft == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topMiddle and middleMiddle and bottomMiddle == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if topRight and middleRight and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if middleLeft and middleMiddle and middleRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

if bottomLeft and bottomMiddle and bottomRight == "O":
    print(" ")
    print(" ")
    print("--- Player Two Wins! ---")
    print(" ")
    print(" ")
    quit()

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

ninethGo = input("Player one's fifth go: ")

if ninethGo == "Top Left":
    topLeft = "X"
if ninethGo == "Top Middle":
    topMiddle = "X"
if ninethGo == "Top Right":
    topRight = "X"
if ninethGo == "Middle Left":
    middleLeft = "X"
if ninethGo == "Middle Middle":
    middleMiddle = "X"
if ninethGo == "Middle Right":
    middleRight = "X"
if ninethGo == "Bottom Left":
    bottomLeft = "X"
if ninethGo == "Bottom Middle":
    bottomMiddle = "X"
if ninethGo == "Bottom Right":
    bottomRight = "X"

if topLeft and topMiddle and topRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topLeft and middleLeft and bottomLeft == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topMiddle and middleMiddle and bottomMiddle == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if topRight and middleRight and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if middleLeft and middleMiddle and middleRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

if bottomLeft and bottomMiddle and bottomRight == "X":
    print(" ")
    print(" ")
    print("--- Player One Wins! ---")
    print(" ")
    print(" ")
    quit()

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")
