## CST 205 - Lab 11
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

def game():#---------------------------------------------------------------------------------------------------
  #by default, player starts in room 1
  roomIn = 1
  
  printNow(welcomeMsg(roomIn))
  printNow(roomDescription(roomIn))
  
  gameRunning = true
  while gameRunning:
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
      spMove(userCmd, roomIn)
    elif userCmd in controlCommands():
      otherCommand(userCmd, roomIn)
    elif userCmd == "exit":
      gameRunning = false
    else:
      printNow("I do not know that command.")

  printNow("\nYou are a quitter.\n")

def spMove(userCmd, roomIn):#-------------------------------------------------------------------------------------------------------
  if userCmd == "jump":
    jump(roomIn)
  if userCmd == "fall":
    fall()
  if userCmd == "dance":
    dance()
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

def otherCommand(str, roomIn):#---------------------------------------------------------------------------------------------------
  #define and perform the other actions
  if str == "help":
    printNow(welcomeMsg(roomIn))
  elif str == "look":
    printNow(roomDescription(roomIn))
  elif str == "commands":
    listCommands()

def movementCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['n', 's', 'e', 'w']
  return validCommands

def spMoveCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['jump', 'dance', 'fall', 'sleep', 'run', 'cry', 'scream', 'laugh']
  return validCommands
  
def controlCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['help', 'look', 'commands']
  return validCommands

def roomDescription(roomIn):#---------------------------------------------------------------------------------------------------
  #all room definintions/descriptions go here
  output = ""
  if roomIn == 1:
    output = "---------- MUDROOM ---------\n" + \
              "You are in the mudroom.\n" + \
              "This room is full of dirty clothes and shoes, nothing else to note.\n" + \
              "The living room is through the North door.\n" + \
              "The exit to the house is through the Southern door, but it is will not open."
  elif roomIn == 2:
    output = "-------- LIVING ROOM -------\n" + \
              "You are in the living room.\n" + \
              "This room contains normal furniture, a television and a fireplace.\n" + \
              "The bed room is through the North door.\n" + \
              "The mud room is through the South door.\n" + \
              "The kitchen is through the West door."
  elif roomIn == 3:
    output = "---------- KITCHEN ---------\n" + \
              "You are in the kitchen.\n" + \
              "This looks like it was straight out of the 60's.\n" + \
              "The dining room is through the North door.\n" + \
              "The living room is through the East door."
  elif roomIn == 4:
    output = "--------- BED ROOM ---------\n" + \
              "You are in the bed room.\n" + \
              "Contains a neatly made queen sized bed and a small desk.\n" + \
              "The living room is through the South door.\n" + \
              "The dining room is through the West door."
  elif roomIn == 5:
    output = "-------- DINING ROOM -------\n" + \
              "You are in the dining room.\n" + \
              "This must be where they ate food, there are four chairs surrounding an empty table.\n" + \
              "The bed room is through the East door.\n" + \
              "The kitchen is through the South door."
  return output
  
def welcomeMsg(roomIn):#---------------------------------------------------------------------------------------------------
  output = "----------------------------------------------\n" + \
           "--------Welcome to my game-------- \n"+ \
           "----------------------------------------------\n" + \
           "Please enter a direction to navigate thoughout the envrionment.\n"+ \
           "You are allowed to move by typing 'n' for North, 's' for South, 'e' for East, and 'w' for West.\n"+ \
           "To see a list of commands, type 'commands'.\n" + \
           "To get help or quit the game, type 'help' or 'exit'."
  return output

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
    
def listCommands():
  print "Move: ", movementCommands()
  print "Special: ", spMoveCommands()
  print "Menu Commands: ", controlCommands()


def jump(roomIn):
  if roomIn == 4:
    printNow("You climb onto the bed and start jumping on it as you once did as a kid.\n" + \
              "After you had your fill of jumping, you climb down and stand next to the bed.\n" + \
              "You feel great, a little exausted, and a little embarrased that you did such a thing.\n" + \
              "But you are glad that nobody was around to see you doing something so silly.")
  else:
    printNow("You jumped. Are you happy?")
    
def fall():
  printNow("You should probably get up")

def dance():
  printNow("Keep going, like nobody's watching\n" + \
            "Except me...")
  
def sleep(roomIn):
  if roomIn == 4:
    printNow("Enjoy your rest, in some weirdos bed. You might regret this.")
  elif roomIn == 3:
    printNow("You're in the kitchen, at least go in the bedroom")
  else:
    printNow("Probably not a good time to sleep. You're in a creepy house\n" + \
              "and trying to get out!")
              
def run():
  printNow("What are you 6? Grow up!")
  
def cry(roomIn):
  if (roomIn % 2 == 0):
    printNow("I'm so sorry this happened to you!")
  else:
    printNow("Grow up Peter Pan!")
    
def scream(roomIn):
  if (roomIn % 2 == 1):
    printNow("I hear you, but I don't care...")
  else:
    printNow("I'd love to help you, but I'm just a wall.")
    
def laugh(roomIn):
  if (roomIn % 2 == 1):
    printNow("You did it. Sort of. Good luck with the rest of this thing.")
  else:
    printNow("Kinda weird that you're laughing right now...")                                                  