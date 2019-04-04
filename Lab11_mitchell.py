## CST 205 - Lab 11
## Team #9 S.C.E.S.
## Team Members:
## Austin Ah Loo
## Mikie Reed
## Mitchell Saunders
## Nicholas Saunders
## Ramon Lucindo

#global variable to indicate which room player is in
roomIn = 1
gameRunning = True

def game():#---------------------------------------------------------------------------------------------------
  global roomIn #statement required in order to modify roomIn
  roomIn = 1 #needs to be reset at the start of each game
  
  #print welcome message and current room
  printNow(welcomeMsg())
  printNow(roomDescription())
  
 
  while gameRunning: #loops through the main part of the game until the global gameRunning flag gets changed to false
    userCmd = requestString("What do you want to do next?\nType 'help' for commands.")
    if len(userCmd) > 0:
      userCmd = userCmd.lower()
    

    
    if userCmd in movementCommands(): #check to make sure that the command given was valid for each control type
      if not move(userCmd): #the move command will atually do the moving, but will return a true or false if it was successful
        printNow("You cannot move that direction.\n")
      else:
        printNow(roomDescription())  #if the move was successful, print new room details
    elif userCmd in spMoveCommands():
      spMove(userCmd)
    elif userCmd in controlCommands():
      otherCommand(userCmd)
    else:
      printNow("I do not know that command.\n")

  printNow("\nYou have left the game.\n")

def spMove(str):
  if str == 'jump' and roomIn == 4:
    printNow("You climb onto the bed and start jumping on it as you once did as a kid.\n" + \
              "After you had your fill of jumping, you climb down and stand next to the bed.\n" + \
              "You feel great, a little exausted, and a little embarrased that you did such a thing\n" + \
              "But you are glad that nobody was around to see you doing something so silly.\n\n")
  elif str == 'jump':
    printNow("You jump. Are you happy?\n")

def otherCommand(str):#---------------------------------------------------------------------------------------------------
  #define and perform the other actions
  global gameRunning
  if str == "help":
    printNow(welcomeMsg())
  elif str == "exit":
    gameRunning = False
  elif str == "look":
    printNow(roomDescription())
  elif str == 'commands':
    printNow(movementCommands() + spMoveCommands() + controlCommands())

def movementCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['n', 's', 'e', 'w']
  return validCommands

def spMoveCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['jump']
  return validCommands
  
def controlCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['help', 'exit', 'look', 'commands']
  return validCommands

def roomDescription():#---------------------------------------------------------------------------------------------------
  #all room definintions/descriptions go here
  output = ""
  if roomIn == 1:
    output = "\n\n---------- MUDROOM ---------\n" + \
              "You are in the mudroom.\n" + \
              "The living room is through the North door.\n" + \
              "The exit to the house is through the Southern door, but it is will not open.\n"
  elif roomIn == 2:
    output = "\n\n-------- LIVING ROOM -------\n" + \
              "You are in the living room.\n" + \
              "The bed room is through the North door.\n" + \
              "The mud room is through the South door.\n" + \
              "The kitchen is through the West door.\n"
  elif roomIn == 3:
    output = "\n\n---------- KITCHEN ---------\n" + \
              "You are in the kitchen.\n" + \
              "The dining room is through the North door.\n" + \
              "The living room is through the East door.\n"
  elif roomIn == 4:
    output = "\n\n--------- BED ROOM ---------\n" + \
              "You are in the bed room.\n" + \
              "The living room is through the South door.\n" + \
              "The dining room is through the West door.\n"
  elif roomIn == 5:
    output = "\n\n-------- DINING ROOM -------\n" + \
              "You are in the dining room.\n" + \
              "The bed room is through the East door.\n" + \
              "The kitchen is through the South door.\n"
  return output
  
def welcomeMsg():#---------------------------------------------------------------------------------------------------
  output = "\n\n----------------------------------------------\n" + \
            "--------Welcome to my game-------- \n"+ \
            "----------------------------------------------\n" + \
            "Please enter a direction to navigate thoughout the envrionment.\n"+ \
            "You are allowed to move by typing 'n' for North, 's' for South, 'e' for East, and 'w' for West.\n"+ \
            "To see a list of commands, type 'commands'.\n" + \
            "To get help or quit the game, type 'help' or 'exit'.\n"
  return output

def move(str):#---------------------------------------------------------------------------------------------------
  #This function will change the room number that the player is currently in
  #by taking the user input as a direction, and figuring out if the direction
  #entered is a valid direction, and then making a change to the global
  #variable roomIn if that move was valid.
  #
  #             Map of home
  #                  N
  #                E + W
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
  
  global roomIn
  originalRoomIn = roomIn
  if roomIn == 1:
    if str == "n":
      roomIn = 2
    
  elif roomIn == 2:
    if str == "n":
      roomIn = 4
    elif str == "s":
      roomIn = 1
    elif str == "w":
      roomIn = 3
    
  elif roomIn == 3:
    if str == "n":
      roomIn = 5
    elif str == "e":
      roomIn = 2
  
  elif roomIn == 4:
    if str == "s":
      roomIn = 2
    elif str == "w":
      roomIn = 5
    
  elif roomIn == 5:
    if str == "e":
      roomIn = 4
    elif str == "s":
      roomIn = 3
  
  #if the room changed, then return true, otherwise the move command was not valid
  if roomIn != originalRoomIn:
    return True
  else:
    return False
