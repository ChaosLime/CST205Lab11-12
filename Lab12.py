## CST 205 - Lab 12
## Team #9 S.C.E.S.
## Team Members:
## Austin Ah Loo
## Mikie Reed
## Mitchell Saunders
## Nicholas Saunders
## Ramon Lucindo

#             Map of home
#                  N
#                W + E
#                  S
#  |--------------------------------|
#  |               |                |
#  |Dining Room #5 _   Bed Room #4  |
#  |               |                |
#  |------- |------|-------- |------|
#  |               | Living Room #2 |
#  |  Kitchen # 3  _                |
#  |               |-------- |------|
#  |               |  Mud Room #1   |
#  |----------------------|  |------|
GAMERUNNING = True #global variable gives the ability to allow other functions
                   #to terminate game

# driver
def game():#---------------------------------------------------------------------------------------------------
  #by default, player starts in room 1
  global GAMERUNNING
  roomIn = 1

  printNow(welcomeMsg(roomIn))
  printNow(roomDescription(roomIn))

  # dictionary to store name / value pairs of required items user needs to obtain in order to finish game
  allItems = {'medallion':'This medallion has been carved in the shape of a lionhead.\n'+\
              "You notice a strange aura that makes you feel safe.",\
              'key':'This key is oddly-shaped like a spade of hearts.'}
  inventory = []
  #medallion is a ward that keeps monster from killing you
  #key is to open a hidden trap door into the room with a monster but also the place to exit

  while GAMERUNNING:
    userCmd = requestString("What do you want to do next?\nType 'Help' for commands.")
    printNow(userCmd)
    if len(userCmd) > 0:
      userCmd = userCmd.lower()
    else:
      #user entered nothing, ask again
      continue
    if userCmd in movementCommands(): #check to make sure that the command given was valid for each control type
      oldRoom = roomIn
      roomIn = move(userCmd, roomIn)
      if oldRoom != roomIn:
        printNow(roomDescription(roomIn))
      else:
        printNow("You cannot move that direction.")
    elif userCmd in spMoveCommands():
      spMove(userCmd, roomIn, inventory)
    elif userCmd in controlCommands():
      otherCommand(userCmd, roomIn, inventory, allItems)
    elif userCmd == "exit":
      GAMERUNNING = False
      printNow("\nYou are a quitter.\n")
    else:
      printNow("I do not know that command.")

# specific moves within specified room with current inventory of items on player
def spMove(userCmd, roomIn, inventory):#-------------------------------------------------------------------------------------------------------
  if userCmd == "jump":
    jump(roomIn, inventory)
  if userCmd == "fall":
    fall(roomIn, inventory)
  if userCmd == "dance":
    dance(roomIn, inventory)
  if userCmd == "sleep":
    sleep(roomIn)
  if userCmd == "run":
    run()
  if userCmd == "cry":
    cry(roomIn)
  if userCmd == "scream":
    scream(roomIn)
  if userCmd == "laugh":
    laugh(roomIn)

# other commands within specified room with current inventory of items on player
def otherCommand(str, roomIn, inventory, allItems):#---------------------------------------------------------------------------------------------------
  #define and perform the other actions
  if str == "help":
    printNow(welcomeMsg(roomIn))
  elif str == "look":
    printNow(roomDescription(roomIn))
  elif str == "commands":
    listCommands()
  elif str == "inventory":
    listInventory(inventory)
  elif str == "examine":
    examineItem(inventory, allItems)

# valid moves: north, south, east, and west
def movementCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['n', 's', 'e', 'w']
  return validCommands

# specific valid moves
def spMoveCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['jump', 'dance', 'fall', 'sleep', 'run', 'cry', 'scream', 'laugh']
  return validCommands

# specific valid other commands
def controlCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['help', 'look', 'commands', 'examine', 'inventory']
  return validCommands

# lists inventory of items on player
def listInventory(inventory):#---------------------------------------------------------------------------------------------------
  if len(inventory) > 0:
    for i in inventory:
      printNow(i)
  else:
    printNow("You have nothing on you.")
    
# add an item to inventory of items on player
def addToInventory(item, inventory):#---------------------------------------------------------------------------------------------------
  inventory.append(item)

# check if an item is in the inventory of items
def examineItem(inventory, allItems):#---------------------------------------------------------------------------------------------------
  if len(inventory) > 0:
    userCmd = requestString("What item do you want to examine?")
    if userCmd in inventory:
      printNow(allItems[userCmd])
    else:
      printNow("You do not have that item in inventory.")
  else:
    printNow("You do not have any items in inventory.")

# provides a description of each room
def roomDescription(roomIn):#---------------------------------------------------------------------------------------------------
  #all room definintions/descriptions go here
  output = ""
  if roomIn == 1:
    output = "---------- MUDROOM ---------\n" + \
              "You are in the mudroom.\n" + \
              "This room is full of dirty clothes and shoes, nothing else to note.\n" + \
              "The living room is through the North door.\n" + \
              "The exit to the house is through the Southern door, but it will not open."
  elif roomIn == 2:
    output = "-------- LIVING ROOM -------\n" + \
              "You are in the living room.\n" + \
              "This room contains common furniture, a television, and a fireplace.\n" + \
              "The wooden floor in this room makes it a perfect place to dance on.\n" + \
              "The bedroom is through the North door.\n" + \
              "The mudroom is through the South door.\n" + \
              "The kitchen is through the West door."
  elif roomIn == 3:
    output = "---------- KITCHEN ---------\n" + \
              "You are in the kitchen.\n" + \
              "This looks like it was straight out of the 60's.\n" + \
              "The dining room is through the North door.\n" + \
              "The living room is through the East door."
  elif roomIn == 4:
    output = "--------- BEDROOM ---------\n" + \
              "You are in the bedroom.\n" + \
              "It contains a small desk and a neatly made queen-sized bed, which looks tempting to jump on.\n" + \
              "The living room is through the South door.\n" + \
              "The dining room is through the West door."
  elif roomIn == 5:
    output = "-------- DINING ROOM -------\n" + \
              "You are in the dining room.\n" + \
              "This must be where they eat food. There are four chairs surrounding an empty table.\n" + \
              "The floor near the table appears to be slippery. Try not to fall.\n"+\
              "Or do...\n" + \
              "The bedroom is through the East door.\n" + \
              "The kitchen is through the South door."
  return output

# generates welcome message, description of movement commands and provides other commands 
def welcomeMsg(roomIn):#---------------------------------------------------------------------------------------------------
  output = "----------------------------------------------\n" + \
           "--------Welcome to my game-------- \n"+ \
           "----------------------------------------------\n" + \
           "Please enter a direction to navigate thoughout the envrionment.\n"+ \
           "You are allowed to move by typing 'n' for North, 's' for South, 'e' for East, and 'w' for West.\n"+ \
           "To see a list of commands, type 'commands'.\n" + \
           "To get help or quit the game, type 'help' or 'exit'."
  return output

# move player based on direction and specified room
def move(direction, roomIn):#---------------------------------------------------------------------------------------------------
  #This function will change the room number that the player is currently in
  #by taking the user input as a direction, and figuring out if the direction
  #entered is a valid direction, and then making a change to the global
  #variable roomIn if that move was valid.
  #
  #             Map of home
  #                  N
  #                W + E
  #                  S
  #  |--------------------------------|
  #  |               |                |
  #  |Dining Room #5 _   Bed Room #4  |
  #  |               |                |
  #  |------- |------|-------- |------|
  #  |               | Living Room #2 |
  #  |  Kitchen # 3  _                |
  #  |               |-------- |------|
  #  |               |  Mud Room #1   |
  #  |----------------------|  |------|

  if roomIn == 1:
    if direction == "n":
      roomIn = 2

  elif roomIn == 2:
    if direction == "n":
      roomIn = 4
    elif direction == "s":
      roomIn = 1
    elif direction == "w":
      roomIn = 3

  elif roomIn == 3:
    if direction == "n":
      roomIn = 5
    elif direction == "e":
      roomIn = 2

  elif roomIn == 4:
    if direction == "s":
      roomIn = 2
    elif direction == "w":
      roomIn = 5

  elif roomIn == 5:
    if direction == "e":
      roomIn = 4
    elif direction == "s":
      roomIn = 3

  return roomIn

# lists different types of commands or movements 
def listCommands():
  print "Move: ", movementCommands()
  print "Special: ", spMoveCommands()
  print "Menu Commands: ", controlCommands()

# jump in specified room with items on player
# the user will need to exectue the jump action at some point in order to trigger the jump() function that
# advances the gameplay
def jump(roomIn, inventory):
  if roomIn == 4:
    printNow("You climb onto the bed and start jumping on it as you once did as a kid.\n" + \
              "While you where jumping, you hear a metallic sounding object hit the ground.\n" + \
              "After you had your fill of jumping, you climb down and stand next to the bed.\n" + \
              "You feel great, a little exausted, and a little embarrased that you did such a thing.\n" + \
              "You look around for that weird noise, and find a key.")
    addToInventory('key', inventory)
  else:
    printNow("You jumped. Are you happy?")

# fall in specified room with items on player
# the user will need to exectue the fall action at some point in order to trigger the fall() function that
# advances the gameplay
def fall(roomIn, inventory):
  if roomIn == 5:
    printNow("When you fall, you notice a weird object underneath the table.\n"+\
            "You grab the item, and it appears to be a medallion.")
    addToInventory('medallion', inventory)
  else:
    printNow("You should probably get up.")

# dance in specified room with items on player
# the dance() function includes the logic to determine whether the user wins or loses the game
def dance(roomIn, inventory):
  if (roomIn == 2):
    userCmd = ""
    printNow("You dance wildly, so much so that you move the couch.\n" +\
              "You notice a hatch where the couch was.")
    if('key' in inventory):
      printNow("The key that you have appears to be a perfect fit, and the hatch opens.")
      while True:
        userCmd = requestString("Would you like to enter the hatch? y/n")
        if(len(userCmd) > 0):
          userCmd = userCmd.lower()
          if(userCmd == 'y' or userCmd == 'n'):
            break
      if(userCmd == 'y'):
        printNow("You enter the hatch.\n" +\
                 "It is dark and damp, with a sense of dread as you step inside. Suddenly, the hatch closes and locks behind you.")
        if('medallion' in inventory):
          printNow("To your surprise, the medallion you found earlier starts to glow with a warm, golden aura, and your initial dread immediately dissolves.\n"+\
                   "You then see a distant light in the dark room.\n"+\
                   "You approach the light, and it leads you outside where it is safe.")
          win(True)
        else:
          printNow("There is a horrible stench and the sound of heavy breathing\n"+\
                   "A loud screech is made and you feel your body being ripped to pieces")
          win(False)
      elif(userCmd == 'n'):
        printNow("You do not enter the hatch.")
    else:
      printNow("This hatch appears to have a strange looking keyhole.\n" +\
               "Perhaps it is around here somewhere.")
  else:
    printNow("Keep going, like nobody's watching\n" + \
            "Except me...")

# determine if player won
def win(didWin):
  global GAMERUNNING

  if(didWin):
    printNow("Congratulations! You win the game!")
  else:
    printNow("You were killed by a monster, sorry, you lose the game, try again.")

  GAMERUNNING = False

# sleep in specified room
def sleep(roomIn):
  if roomIn == 4:
    printNow("Enjoy your rest, in some stranger's bed. You might regret this.")
  elif roomIn == 3:
    printNow("You're in the kitchen, at least go in the bedroom.")
  else:
    printNow("It's probably not a good time to sleep. You're in a creepy house\n" + \
              "and trying to get out!")

# run regardless of room
def run():
  printNow("What are you 6? Grow up!")

# cry in specified room
def cry(roomIn):
  if (roomIn % 2 == 0):
    printNow("I'm so sorry this happened to you!")
  else:
    printNow("Grow up Peter Pan!")

# scream in specified room
def scream(roomIn):
  if (roomIn % 2 == 1):
    printNow("I hear you, but I don't care...")
  else:
    printNow("I'd love to help you, but I'm just a wall.")

# laugh in specified room
def laugh(roomIn):
  if (roomIn % 2 == 1):
    printNow("You did it. Sort of. Good luck with the rest of this thing.")
  else:
    printNow("Kinda weird that you're laughing right now...")
