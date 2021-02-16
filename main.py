print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure located on an island.")
print("You found an old treasure map in your parents house in their garden while tending to it")
print("The letter the comes with the treasure map writes'I'm glad you found my map,\nnow go get the treasure for me and you will get half.\nI will tell you the full story after you come back with the treasure.\nNow go' You look at the treasure map and decide to go.")

choice1 = input("Where do you go first, Store or Dock? ").lower()

if choice1 == "store":
  print("You get the equipment you need from the store")
elif choice1 == "dock":
  print("You go to the docks without a plan, you end up doing something else and forget about the treasure.\nGame Over")
else:
  print("First warning, please follow the rules. Game Over")

if choice1 == "store":
  choice2 = input("After you get the equipment, you go to the docks and decide to get a boat, Rent or Steal? ")
  choice2.lower()

  if choice2 == "rent":
    print("You Rent the boat and get on your way")
  elif choice2 == "steal":
    print("You try to steal the boat and get caught.\nGame Over")
  else:
    print("No second warning, this is your final warning. Follow the rules")

  if choice2 == "rent":
    choice3 = input("Which direction do you go, West or East? ")
    choice3.lower()

    if choice3 == "east":
      print("After an hour, you see the island")
    elif choice3 == "west":
      print("After 6 hours, you realise you had the map upside down. You decide to give up and go back home.\nGame Over")
    else:
      print("You decide to be a fool and let the wind to you and you get lost never to be seen again because you went crazy after a week on the ocean and got eaten. You fool, follow the rules")

    if choice3 == "east":
      choice4 = input("What do you do next, Dock or Turn? ")
      choice4.lower()

      if choice4 == "dock":
        print("You dock on the island but you hit something and the boat gets a hole in the bottom,\nyou can't leave the island, you are trap.\nGame Over")
      elif choice4 == "turn":
        print("You turn and avoid the bad docking spot. You dock on a good one which is close to the treasure spot.")
      else:
        print("You boat breaks but you are ok until the run onto some wild animals and well you know the rest... just follow the rules, fool")

        if choice4 == "turn":
          choice5 = input("After digging for 2 hours and getting the treasure, what do you do next, NumberOne or MyFamily? ")
          choice5.lower()

          if choice5 == "myfamily":
            print("You take back the treasure to your parents and they give you half.\nThey tell you why they coundn't get it but you were on your phone the whole time pretending to listen to them.\nAt least you get half.\nGood End")
          elif choice5 == "numberone":
            print("You decide to take the treasure for yourself and go to live on another country and life's good.\nSeriously? they are your parents.\nYou need to rethink your choice next time.\nBad End")
          else:
            print("God strikes you with lighting.\nYeah, my game my rules. Now restart and follow the rules you fool.")