"""Text Game

Author: Aiden Cague
Version: 1.0.1
"""

#Color Resources
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

name = ""
life_span = 30
gems = 0
introList = [0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0]
itemList = [1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,]
invList = ['( )', '( )', '( )', '( )',
           '( )', '( )', '( )', '( )',
           '( )', '( )']

#Game Tools
def isValid(action, case):
    if action.upper() == case.upper() or action.lower() == case.lower():
        return True
    else:
        return False

def actionInput():
    playerInput = input()
    return playerInput

def life():
        print('\nDays Till Death:', life_span)

#Inventory Management
def inv(): 
        print('\n~ Inventory ~\n-', invList[0],'\n-', invList[1],'\n-',
              invList[2],'\n-', invList[3],'\n-', invList[4],'\n-',
              invList[5],'\n-', invList[6],'\n-', invList[7],'\n-',
              invList[8],'\n-', invList[9])

def freeInvSlot():
    freeSpace = False
    for slot in invList:
        if slot == '( )':
            freeSpace = True
            return invList.index('( )')
    if freeSpace == False:
        return False

def money(): 
    print('\nGems:', gems)

#Play Game

#Menu
def menu():
    global name
    global life_span
    global gems
    print('||||| || || |||||     ||||| || ||  |||  ||||| ||||  |||||  |||  || ||')
    print('  |   || || ||        |     || || || || || || || ||   |   || || ||| |')
    print('  |   ||||| |||||     | ||| || || ||||| ||||  || ||   |   ||||| |||||')
    print('  |   || || ||        |  || || || || || || || || ||   |   || || | |||')
    print('  |   || || |||||     ||||| ||||| || || || || ||||  ||||| || || || ||')
    print('\n-PLAY\n-CREDITS\n-CONTROLS\n-QUIT\n')
    end = 0
    while end == 0:
        actionResult = actionInput()
        if isValid(actionResult, 'play'):
            print('\n~ What is your name? ~\n')
            name = actionInput()
            print('\n~ Welcome ' + color.RED + color.BOLD + name + color.END + ' ~\n')
            shed()
            break
        elif isValid(actionResult, 'credits'):
            credits()
        elif isValid(actionResult, 'controls'):
            controls()
        elif isValid(actionResult, 'quit'):
            exit()
        else:
            print("\n- Invalid Input -\n")
    
def credits():
    credits = 0
    while credits == 0:
        print('\nCreated by Aiden Cague, degree in CS at James Madison University\n\nType "Back" to return to menu.')
        actionResult = actionInput()
        if isValid(actionResult, 'back') or isValid(actionResult, 'exit') or isValid(actionResult, 'menu'):
            menu()
        else:
            print("\n- Invalid Input -\n")

def controls():
    controls = 0
    while controls == 0:
        print('\nType an action in any style, ' \
              'so long as it is a valid word. ' \
              'Typical keywords include "Back", "Exit", "Menu", "Inventory", ' \
              '"Life", "Gems", "Money", "Take", "Look", and "Use".\n\nType "Back" to return to menu.')
        actionResult = actionInput()
        if isValid(actionResult, 'back') or isValid(actionResult, 'exit') or isValid(actionResult, 'menu'):
            menu()
        else:
            print("\n- Invalid Input -\n")

#Graveyard
def graveyard():
    global name
    global gems
    global life_span
    start = 0
    while start == 0:
        if introList[1] == 0:
            print("\n~~~~~\nYou now stand in an empty graveyard.")
            print("\nTombs cover every inch of the open hillscape, bathed in an eery moonlight.")
            introList[1]= 1
        while introList[1] == 1:
            actionResult = actionInput()
            if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                inv()
            elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                money()
            elif isValid(actionResult, 'life'):
                life()
            elif isValid(actionResult, 'look'):
                print("\n~~~~~\nA lone", color.BOLD + 'tree' + color.END, "stands pale and barren against the black sky. "
                      "In the distance you see a crooked gate where the sea of tombstones end, adorned on either side by",
                      color.BOLD + 'gargoyles.' + color.END, "Past the gate, "
                      "a forked stone path leads beyond the horizon. From the", color.BOLD + 'left path' + color.END,
                      ", you can make out a shadowy forest. From the", color.BOLD + 'right path' + color.END,
                      ", you can see dim lights almost completely swallowed by the oppressive night. "
                      "The", color.BOLD + 'shed' + color.END, "lies behind you.")
            elif isValid(actionResult, 'tree'):
                print("\n~~~~~\nThe gnarled tree gets worse the longer you stare at it.")
                while itemList[2] == 1:
                    tree_search = input('\nShould you search further?\n')
                    if isValid(tree_search, 'yes') or isValid(tree_search, 'search'):
                        print("\n~~~~~\nNoticing a hole in the wooden flesh, you reach inside and find a",
                              color.BOLD + 'locket.' + color.END,
                              "Inside is a faded picture of a young woman with hollow eyes.")
                        if freeInvSlot() is not False:
                            invList[freeInvSlot()] = 'Old Locket'
                            itemList[2] = 0
                        elif freeInvSlot() is False:
                            print("\n~~~~~\nYour backpack is full.")
                            print("\n~~~~~\nYou return to the courtyard.")
                            break
                    elif isValid(tree_search, 'no') or isValid(tree_search, 'back') or isValid(tree_search, 'exit'):
                        print("\n~~~~~\nYou return to the courtyard.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
                while itemList[2] == 0:
                    tree_search = input('\nShould you search further?\n')
                    if isValid(tree_search, 'yes') or isValid(tree_search, 'search'):
                        print("\n~~~~~\nAn old dead tree. You turn back to the courtyard.")
                        break
                    elif isValid(tree_search, 'no') or isValid(tree_search, 'back') or isValid(tree_search, 'exit'):
                        print("\n~~~~~\nYou return to the courtyard.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
            elif isValid(actionResult, 'gargoyle'):
                print("\n~~~~~\nYou approach the stone figures, their eyes gleaming", color.GREEN + color.BOLD + 'green.' + color.END)
                while itemList[3] == 1:
                    garg_inspect = input()
                    if isValid(garg_inspect, 'inspect') or isValid(garg_inspect, 'search') or isValid(garg_inspect, 'look') or isValid(garg_inspect, 'take'):
                        print("\n~~~~~\nThe gargoyles\' eyes seem to be made from glimmering jewels. You crudely pry them from their sockets.\n\nMoney + 50")
                        gems += 50
                        itemList[3] = 0
                        break
                    elif isValid(garg_inspect, 'back') or isValid(garg_inspect, 'exit'):
                        print("\n~~~~~\nYou turn back to the courtyard.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
                while itemList[3] == 0:
                    garg_inspect = input()
                    if isValid(garg_inspect, 'inspect') or isValid(garg_inspect, 'search') or isValid(garg_inspect, 'take'):
                        print("\n~~~~~\nTheir eyes are empty. You return to the courtyard.")
                        break
                    elif isValid(garg_inspect, 'back') or isValid(garg_inspect, 'exit'):
                        print("\n~~~~~\nYou turn back to the courtyard.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
            elif isValid(actionResult, 'shed') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                print("\n~~~~~\nYou turn around and head back into the dilapitated shed.")
                shed()
                life_span -= 1
                break
            elif isValid(actionResult, 'left path'):
                if introList[2] == 0:
                    print("\n~~~~~\nYour conscious tells you to choose the", color.BOLD + 'right path,' + color.END,
                          "but your hungering curiosity yearns for the dark forest.")
                    introList[2] = 1
                    life_span -= 1
                    forest()
                elif introList[2] == 1:
                    print("\n~~~~~\nYou head into the maw of the dark forest.")
                    life_span -= 1
                    forest()
            elif isValid(actionResult, 'right path'):
                if introList[3] == 0:
                    print("\n~~~~~\nGuided by the hopeful lights in the distance, you make your way down the "
                          "right path in the hopes of finding the answers you seek.")
                    print("\n~~~~~\nThe gently swaying lanterns are the only warmth to be found within "
                          "the village. You walk down the cracked stone street, passing unlit windows. "
                          "From inside one, you see a pale young girl staring through you until she "
                          "catches your gaze and ducks out of sight. ")
                    print("\nAfter searching the boarded windows, you finally spot an old man with a scared look "
                          "beckoning you from behind the cover of his shoddy wooden door. "
                          "With no other choice, you quickly follow him into his home. He doesn't say a word as he "
                          "pours some sort of liquid "
                          "into a mug, but his eyes are no longer filled with fear. He hobbles over to you with the "
                          "mug and sets it on the table in front of you.")
                    print('"It is you, the cursed', color.RED + color.BOLD + name + color.END, '. You were not meant to survive."')
                    print('\nHe lays an old book on the table and flips to a page depicting a man with the head and hooves of a goat.')
                    print('"You''ll find', color.BOLD + 'Him' + color.END, 'deep within that condemned forest. '
                          'Take one of his horns and bring it to me. I will use it to craft the holy antidote to your ailment. '
                          'The poison will take your life', color.BOLD + 'within' + color.END, life_span,
                          color.BOLD + 'days.' + color.END, 'God save you."')
                    print("You leave the old man's house and return to the village.")
                    introList[3] = 1
                    life_span -= 1
                    village()
                if introList[3] == 1:
                    print("\n~~~~~\nYou head into the village.")
                    life_span -= 1
                    village()
            else:
                print("\n- Invalid Input -\n")

#Forest
def forest():
    global name
    global life_span
    global gems
    start = 0
    while start == 0:
        if introList[4] == 0:
            print("\n~~~~~\nYou continue to walk deeper into the lair of thorns and branches.")
            introList[4] = 1
        while introList[4] == 1:
            while itemList[6] == 1:
                cancel = 0
                path_choice1 = 1
                path_choice2 = 0
                path_choice3 = 0
                if cancel == 1:
                    break
                while path_choice1 == 1:
                    if cancel == 1:
                        break
                    print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END,
                          'or', color.BOLD + 'right' + color.END)
                    actionResult = actionInput()
                    if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                        inv()
                    elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                        money()
                    elif isValid(actionResult, 'life'):
                        life()
                    elif isValid(actionResult, 'graveyard') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                        print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                        life_span -= 1
                        graveyard()
                    elif isValid(actionResult, 'left'):
                        print("\n~~~~~\nThe path forward becomes clearer.")
                        path_choice1 = 0
                        path_choice2 = 1
                        break
                    elif isValid(actionResult, 'middle') or isValid(actionResult, 'right'):
                        print("\nYou lose yourself in the forest...")
                        path_choice1 = 1
                        path_choice2 = 0
                        path_choice3 = 0
                        break
                    elif isValid(actionResult, 'search') or isValid(actionResult, 'look'):
                        print("\n~~~~~\nA", color.GREEN + color.BOLD + 'green glint' + color.END, "in the leaves catches your eye.")
                        gems += 25
                    else:
                        print("\n- Invalid Input -\n")
                while path_choice2 == 1:
                    print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END,
                          'or', color.BOLD + 'right' + color.END)
                    actionResult = actionInput()
                    if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                        inv()
                    elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                        money()
                    elif isValid(actionResult, 'life'):
                        life()
                    elif isValid(actionResult, 'graveyard') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                        print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                        life_span -= 1
                        graveyard()
                    elif isValid(actionResult, 'right'):
                        print("\n~~~~~\nThe path forward becomes clearer.")
                        path_choice2 = 0
                        path_choice3 = 1
                        break
                    elif isValid(actionResult, 'left') or isValid(actionResult, 'middle'):
                        print("\nYou lose yourself in the forest...")
                        path_choice1 = 1
                        path_choice2 = 0
                        path_choice3 = 0
                        break
                    else:
                        print("\n- Invalid Input -\n")
                while path_choice3 == 1:
                    if cancel == 1:
                        break
                    print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END,
                          'or', color.BOLD + 'right' + color.END)
                    actionResult = actionInput()
                    if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                        inv()
                    elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                        money()
                    elif isValid(actionResult, 'life'):
                        life()
                    elif isValid(actionResult, 'graveyard') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                        print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                        life_span -= 1
                        graveyard()
                    elif isValid(actionResult, 'middle'):
                        print("\n~~~~~\nThe path forward reveals a sprawling castle. Its spires pierce the moonlight.")
                        print("A", color.BOLD + 'bridge' + color.END, 'separates you and the fortress, '
                              'blocked by what appears to be a knight in haunting black armor. '
                              'Bodies lie in heaps beside the bridge, and you spot a sword sticking out of '
                              'one of them. When you grab the hilt, the blade snaps, but the hilt '
                              'remains gleaming.')
                        if freeInvSlot() is not False:
                            invList[freeInvSlot()] = 'Sword Hilt'
                            itemList[6] = 0
                            break
                        elif freeInvSlot() is False:
                            print("\n~~~~~\nYour backpack is full.")
                            print("\n~~~~~\nYou return to the graveyard.")
                            graveyard()
                    elif isValid(actionResult, 'left') or isValid(actionResult, 'right'):
                        print("\nYou lose yourself in the forest...")
                        path_choice1 = 1
                        path_choice2 = 0
                        path_choice3 = 0
                        break
                    else:
                        print("\n- Invalid Input -\n")
            while itemList[6] == 0:
                if introList[8] == 0:
                    print("\n~~~~~\nYou break through the forest finding a beaten path. You can see the",
                          color.BOLD + 'bridge' + color.END, "to the castle looming through the trees.")
                    path_choice1 = 0
                    path_choice2 = 0
                    path_choice3 = 0
                    introList[8] = 1
                while introList[8] == 1:
                    actionResult = actionInput()
                    if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                        inv()
                    elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                        money()
                    elif isValid(actionResult, 'life'):
                        life()
                    elif isValid(actionResult, 'graveyard') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                        print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                        life_span -= 1
                        graveyard()
                    elif isValid(actionResult, 'look'):
                        print("\n~~~~~\nThe dark forest knows its tricks are beaten. The", color.BOLD + "castle" + color.END,
                              "reveals itself beyond the", color.BOLD + "bridge" + color.END,
                              "through the thick branches.")
                    else:
                        print("\n- Invalid Input -\n")

#Village
def village():
    global name
    global life_span
    global gems
    start = 0
    while start == 0:
        if introList[5] == 0:
            print("\n~~~~~\nYou enter the forgotten village.")
            introList[5] = 1
        while introList[5] == 1:
            actionResult = actionInput()
            if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                inv()
            elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                money()
            elif isValid(actionResult, 'life'):
                life()
            elif isValid(actionResult, 'look'):
                print('\n~~~~~\nYou stand in what you assume to be the town square. The cracked stone streets are bordered by short '
                      'cobbled shacks, their wood structures rotting. In the center of the square is an old', color.BOLD + 'well.' + color.END,
                      'There are three storefronts closest to it, and despite their faded signs you can read; "',
                      color.BOLD + 'GEAR, FOOD,' + color.END, 'and', color.BOLD + 'MYSTICS'+ color.END)
            elif isValid(actionResult, 'look'):
                print("\n~~~~~\nYou approach the moss covered well, the only thing in this town with vegetation. "
                      "Something glows underneath the algae of the water.")
                while itemList[7] == 1:
                    well_inspect = input()
                    if isValid(well_inspect, 'search') or isValid(well_inspect, 'look') or isValid(well_inspect, 'take'):
                        print("\n~~~~~\nYou reach into the murk and find a "
                              "large gold coin depicting a goddess.")
                        if freeInvSlot() is not False:
                            invList[freeInvSlot()] = 'Gold Coin'
                            itemList[7] = 0
                        elif freeInvSlot() is False:
                            print("\n~~~~~\nYour backpack is full.")
                            print("\n~~~~~\nYou return to the square.")
                            break
                    if isValid(well_inspect, 'back') or isValid(well_inspect, 'exit') or isValid(well_inspect, 'village'):
                        print("\n~~~~~\nYou return to the square.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
                while itemList[7] == 0:
                    well_inspect = input()
                    if isValid(well_inspect, 'search') or isValid(well_inspect, 'look') or isValid(well_inspect, 'take'):
                        print("\n~~~~~\nJust an old well. You return to the village.")
                        break
                    if isValid(well_inspect, 'back') or isValid(well_inspect, 'exit') or isValid(well_inspect, 'village'):
                        print("\n~~~~~\nYou return to the square.")
                        break
                    else:
                        print("\n- Invalid Input -\n")
            elif isValid(well_inspect, 'back') or isValid(well_inspect, 'exit') or isValid(well_inspect, 'village'):
                print("\n~~~~~\nYou take the beaten path back to the graveyard, never looking back.")
                life_span -= 1
                graveyard()
            elif isValid(actionResult, 'look'):
            
            elif isValid(actionResult, 'look'):
                
            else:
                print("\n- Invalid Input -\n")

#Shed
def shed():
    global name
    global life_span
    global gems
    start = 0
    while start == 0:
        if introList[6] == 0:
            print(f"\n~~~~~\nYou awoke in a dark and unfamiliar place. "
                  "\nThe torn bedsheets you lie in are stained with a deep sickly red "
                  "and the smell suggests it's been there for a while.")
            print("To your left is an old wooden", color.BOLD + 'bedstand,' + color.END,
                  "to your right, a rusted", color.BOLD + 'axe.' +color.END) 
            print("A broken", color.BOLD + 'door' + color.END,
                  "across the room creaks on its hinges and begins to open at the howls of the wind.")
            introList[6] = 1
        while introList[6] == 1:
            actionResult = actionInput()
            if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                inv()
            elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                money()
            elif isValid(actionResult, 'life'):
                life()
            elif isValid(actionResult, 'look'):
                print("\n~~~~~\nThe room you've awoken in seems to be a barren log shed. "
                      "The walls are barely a comfort against the cold or the howling wind. "
                      "You notice a", color.BOLD + 'bedstand, a door, an axe,' + color.END,
                      'and a loose', color.BOLD + 'floorboard.' + color.END)
            elif isValid(actionResult, 'bedstand') and itemList[5] == 1:
                print("\n~~~~~\nYou approach the bedstand and notice a", color.BOLD + 'letter' + color.END,
                      "written in red ink on the table. You search the drawers and find nothing but dust.")
            elif isValid(actionResult, 'bedstand') and itemList[5] == 0:
                print("\n~~~~~\nThe blood letter sits on the bedstand.")
            elif isValid(actionResult, 'axe') and itemList[4] == 1:
                print("\n~~~~~\nYou pick up the axe and dust off what you can of the rust, "
                      "placing it into your backpack. It looks like it might fall apart after one good swing.")
                if freeInvSlot() is not False:
                      invList[freeInvSlot()] = 'Rusty Axe'
                      itemList[4] = 0
                elif freeInvSlot() is False:
                      print("\n~~~~~\nYour backpack is full.")
                      print("\n~~~~~\nYou return to the room.")
                      break
            elif isValid(actionResult, 'axe') and itemList[4] == 0:
                print("\n~~~~~\nThere is nothing left.")
            elif isValid(actionResult, 'floorboard'):
                print("\n~~~~~\nSomething creaks under your feet, and you notice a loose floorboard. "
                      "Peeling it up with your fingers, you find nothing but rats.")
            elif isValid(actionResult, 'door'):
                print("\n~~~~~\nMoving quickly towards the door, you open it and step through its broken frame.")
                life_span -= 1
                graveyard()
            elif isValid(actionResult, 'letter'):
                print("\n~~~~~\nYou pick up the letter and read its sickly contents that glow red despite the darkness.")
                print(color.RED + "\nMy dearest", name + ",\n\tThere is a poison running through your veins. "
                      "You have a month's time to cure yourself, or you shall meet Death. The answer lies in the",
                      color.BOLD + 'Keep.' + color.END)
                print(f"\nYou put down the letter, panic rising within your chest.")
                itemList[5] = 0
            else:
                print("\n- Invalid Input -\n")

def castle():
    global name
    global life_span
    global gems
    start = 0
    while start == 0:
        if introList[7] == 0:
            print("\n~~~~~\nThe ", color.BOLD + 'castle' + color.END, "invokes a deep dread in the bowels of your mind. "
                  "You doubted the knight of the bridge was the last challenge you would have to face. "
                  "The grand doors ahead of you were midnight black, with only two silver handles bolted to its surface.")
            introList[7] = 1
        while introList[7] == 1:
            actionResult = actionInput()
            if isValid(actionResult, 'inventory') or isValid(actionResult, 'backpack'):
                inv()
            elif isValid(actionResult, 'gems') or isValid(actionResult, 'money'):
                money()
            elif isValid(actionResult, 'life'):
                life()
            elif isValid(actionResult, 'graveyard') or isValid(actionResult, 'back') or isValid(actionResult, 'exit'):
                print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                life_span -= 1
                graveyard()
            else:
                print("\n- Invalid Input -\n")

menu()
