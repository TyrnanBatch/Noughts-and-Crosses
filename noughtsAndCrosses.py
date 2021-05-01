import time

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
    topLeft = "x"
if firstGo == "Top Middle":
    topMiddle = "x"
if firstGo == "Top Right":
    topRight = "x"
if firstGo == "Middle Left":
    middleLeft = "x"
if firstGo == "Middle Middle":
    middleMiddle = "x"
if firstGo == "Middle Right":
    middleRight = "x"
if firstGo == "Bottom Left":
    bottomLeft = "x"
if firstGo == "Bottom Middle":
    bottomMiddle = "x"
if firstGo == "Bottom Right":
    bottomRight = "x"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

secondGo = input("Player two's first go: ")

if secondGo == "Top Left":
    topLeft = "o"
if secondGo == "Top Middle":
    topMiddle = "o"
if secondGo == "Top Right":
    topRight = "o"
if secondGo == "Middle Left":
    middleLeft = "o"
if secondGo == "Middle Middle":
    middleMiddle = "o"
if secondGo == "Middle Right":
    middleRight = "o"
if secondGo == "Bottom Left":
    bottomLeft = "o"
if secondGo == "Bottom Middle":
    bottomMiddle = "o"
if secondGo == "Bottom Right":
    bottomRight = "o"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

thirdGo = input("Player one's second go: ")

if thirdGo == "Top Left":
    topLeft = "x"
if thirdGo == "Top Middle":
    topMiddle = "x"
if thirdGo == "Top Right":
    topRight = "x"
if thirdGo == "Middle Left":
    middleLeft = "x"
if thirdGo == "Middle Middle":
    middleMiddle = "x"
if thirdGo == "Middle Right":
    middleRight = "x"
if thirdGo == "Bottom Left":
    bottomLeft = "x"
if thirdGo == "Bottom Middle":
    bottomMiddle = "x"
if thirdGo == "Bottom Right":
    bottomRight = "x"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

fourthGo = input("PLayer two's second go: ")

if fourthGo == "Top Left":
    topLeft = "o"
if fourthGo == "Top Middle":
    topMiddle = "o"
if fourthGo == "Top Right":
    topRight = "o"
if fourthGo == "Middle Left":
    middleLeft = "o"
if fourthGo == "Middle Middle":
    middleMiddle = "o"
if fourthGo == "Middle Right":
    middleRight = "o"
if fourthGo == "Bottom Left":
    bottomLeft = "o"
if fourthGo == "Bottom Middle":
    bottomMiddle = "o"
if fourthGo == "Bottom Right":
    bottomRight = "o"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

fifthGo = input("Player one's third go: ")

if fifthGo == "Top Left":
    topLeft = "x"
if fifthGo == "Top Middle":
    topMiddle = "x"
if fifthGo == "Top Right":
    topRight = "x"
if fifthGo == "Middle Left":
    middleLeft = "x"
if fifthGo == "Middle Middle":
    middleMiddle = "x"
if fifthGo == "Middle Right":
    middleRight = "x"
if fifthGo == "Bottom Left":
    bottomLeft = "x"
if fifthGo == "Bottom Middle":
    bottomMiddle = "x"
if fifthGo == "Bottom Right":
    bottomRight = "x"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

sixthGo = input("Player two's third go: ")

if sixthGo == "Top Left":
    topLeft = "o"
if sixthGo == "Top Middle":
    topMiddle = "o"
if sixthGo == "Top Right":
    topRight = "o"
if sixthGo == "Middle Left":
    middleLeft = "o"
if sixthGo == "Middle Middle":
    middleMiddle = "o"
if sixthGo == "Middle Right":
    middleRight = "o"
if sixthGo == "Bottom Left":
    bottomLeft = "o"
if sixthGo == "Bottom Middle":
    bottomMiddle = "o"
if sixthGo == "Bottom Right":
    bottomRight = "o"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

seventhGo = input("Player one's forth go: ")

if seventhGo == "Top Left":
    topLeft = "x"
if seventhGo == "Top Middle":
    topMiddle = "x"
if seventhGo == "Top Right":
    topRight = "x"
if seventhGo == "Middle Left":
    middleLeft = "x"
if seventhGo == "Middle Middle":
    middleMiddle = "x"
if seventhGo == "Middle Right":
    middleRight = "x"
if seventhGo == "Bottom Left":
    bottomLeft = "x"
if seventhGo == "Bottom Middle":
    bottomMiddle = "x"
if seventhGo == "Bottom Right":
    bottomRight = "x"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

eighthGo = input("Player two's forth go: ")

if eighthGo == "Top Left":
    topLeft = "o"
if eighthGo == "Top Middle":
    topMiddle = "o"
if sixthGo == "Top Right":
    topRight = "o"
if eighthGo == "Middle Left":
    middleLeft = "o"
if eighthGo == "Middle Middle":
    middleMiddle = "o"
if eighthGo == "Middle Right":
    middleRight = "o"
if eighthGo == "Bottom Left":
    bottomLeft = "o"
if eighthGo == "Bottom Middle":
    bottomMiddle = "o"
if eighthGo == "Bottom Right":
    bottomRight = "o"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")

ninethGo = input("Player one's fifth go: ")

if ninethGo == "Top Left":
    topLeft = "x"
if ninethGo == "Top Middle":
    topMiddle = "x"
if ninethGo == "Top Right":
    topRight = "x"
if ninethGo == "Middle Left":
    middleLeft = "x"
if ninethGo == "Middle Middle":
    middleMiddle = "x"
if ninethGo == "Middle Right":
    middleRight = "x"
if ninethGo == "Bottom Left":
    bottomLeft = "x"
if ninethGo == "Bottom Middle":
    bottomMiddle = "x"
if ninethGo == "Bottom Right":
    bottomRight = "x"

print(" " + str(topLeft) +" | " + str(topMiddle) +" | " + str(topRight) +" ")
print("-----------")
print(" " + str(middleLeft) +" | " + str(middleMiddle) +" | " + str(middleRight) +" ")
print("-----------")
print(" " + str(bottomLeft) +" | " + str(bottomMiddle) +" | " + str(bottomRight) +" ")