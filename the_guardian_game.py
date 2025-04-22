'''Demo text-based game.

THE GUARDIAN

Author: Aiden Cague
v1.0.0
'''

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

# Intro Sequence
print('||||| || || |||||     ||||| || ||  |||  ||||| ||||  |||||  |||  || ||')
print('  |   || || ||        |     || || || || || || || ||   |   || || ||| |')
print('  |   ||||| |||||     | ||| || || ||||| ||||  || ||   |   ||||| |||||')
print('  |   || || ||        |  || || || || || || || || ||   |   || || | |||')
print('  |   || || |||||     ||||| ||||| || || || || ||||  ||||| || || || ||')

start_sequence = ['MENU']
for play1 in start_sequence:
    while play1 == 'MENU':
        menu = input('\n-PLAY\n-CREDITS\n-QUIT\n')
        if menu.lower() == 'play' or menu.upper() == 'PLAY':  
            play1 = ['START']
            start_sequence = ['START']
            break
        if menu.lower() == 'credits' or menu.upper() == 'CREDITS':
            print('\nCreated by Aiden Cague, degree in CS')
            continue
        if menu.lower() == 'quit' or menu.upper() == 'QUIT':
            exit()
        else:
            print("\n- Invalid Input -")
#Gameplay
for play1 in start_sequence:
    def life(life_span):
        print('Days Till Death:', life_span)
    def money(gems): #Currency Count
        print('Money:', gems)
    gems = 0
  
    def inv(a, b, c, d, e, f, g, h, i, j): #Inventory Management
        print('~ Inventory ~\n\n-',a,'\n-',b,'\n-',c,'\n-',d,'\n-',e,'\n-',f,'\n-',g,'\n-',h,'\n-',i,'\n-',j)
    a = '( )'
    b = '( )'
    c = '( )'
    d = '( )'
    e = '( )'
    f = '( )'
    g = '( )'
    h = '( )'
    i = '( )'
    j = '( )'
    life_span = 30
    cancel = 0
    intro = 0
    intro2 = 0
    intro3 = 0
    intro4 = 0
    intro5 = 0
    intro6 = 0
    intro7 = 0
    intro8 = 0
    intro9 = 0
    intro10 = 0
    castle_intro = 0
    letter = 1
    axe = 1
    locket = 1
    gem = 1
    token = 1
    castle = 0
    room = 'INTRO'
#Shed
    while play1 == 'START':
        while room == 'INTRO':
            if intro == 0:
                name = input('\n~ What is your name? ~\n') #Saved for later
                print(f"\n~~~~~\nYou awoke in a dark and unfamiliar place. "
                       "\nThe torn bedsheets you lie in are stained with a deep sickly red "
                       "and the smell suggests it's been there for a while.")
                print("To your left is an old wooden", color.BOLD + 'bedstand,' + color.END, "to your right a rusted", color.BOLD + 'axe.' +color.END) 
                print("A broken", color.BOLD + 'door' + color.END, "across the room creaks on its hinges and begins to open at the howls of the wind.") 
                intro = 1
                break
            while intro == 1:
                player_action = input()
                if 'bedstand' in player_action.upper() or 'bedstand' in player_action.lower() and letter == 1:
                    print("\n~~~~~\nYou approach the bedstand and notice a", color.BOLD + 'letter' + color.END, "written in red ink on the table. You search the drawers and find nothing but dust.")
                    continue
                if 'bedstand' in player_action.upper() or 'bedstand' in player_action.lower() and letter == 0:
                    print("\n~~~~~\nThe blood letter sits on the bedstand.")
                    continue
                elif 'axe' in player_action.upper() or 'axe' in player_action.lower() and axe == 1:
                    print("\n~~~~~\nYou pick up the axe and dust off what you can of the rust, placing it into your backpack. It looks like it might fall apart after one good swing.")
                    if a == '( )':
                        a = 'Rusty Axe'
                        axe = 0
                    elif b == '( )':
                        b = 'Rusty Axe'
                        axe = 0
                    elif c == '( )':
                        c = 'Rusty Axe'
                        axe = 0
                    elif d == '( )':
                        d = 'Rusty Axe'
                        axe = 0
                    elif e == '( )':
                        e = 'Rusty Axe'
                        axe = 0
                    elif f == '( )':
                        f = 'Rusty Axe'
                        axe = 0
                    elif g == '( )':
                        g = 'Rusty Axe'
                        axe = 0
                    elif h == '( )':
                        h = 'Rusty Axe'
                        axe = 0
                    elif i == '( )':
                        i = 'Rusty Axe'
                        axe = 0
                    elif j == '( )':
                        j = 'Rusty Axe'
                        axe = 0
                    else:
                        print("\n~~~~~\nYour backpack is full.")
                    continue
                elif 'axe' in player_action.upper() or 'axe' in player_action.lower() and axe == 0:
                    print("\n~~~~~\nThere is nothing left.")
                    continue
                elif 'floorboard' in player_action.upper() or 'floorboard' in player_action.lower():
                    print("\n~~~~~\nSomething creaks under your feet, and you notice a loose floorboard. Peeling it up with your fingers, you find nothing but rats.")
                    continue
                elif 'door' in player_action.upper() or 'door' in player_action.lower():
                    print("\n~~~~~\nMoving quickly towards the door, you open it and step through its broken frame.")
                    room = 'GRAVEYARD'
                    life_span = life_span - 1
                    break
                elif 'look' in player_action.upper() or 'look' in player_action.lower():
                    print("\n~~~~~\nThe room you've awoken in seems to be a barren log shed. The walls are barely a comfort against the cold or the howling wind. "
                          "You notice a", color.BOLD + 'bedstand, a door, an axe,' + color.END, 'and a loose', color.BOLD + 'floorboard.' + color.END)
                    continue
                elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'money' in player_action.upper() or 'money' in player_action.lower():
                        money(gems)
                        continue
                elif 'life' in player_action.upper() or 'life' in player_action.lower():
                    life(life_span)
                    continue
                elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                    life(life_span)
                    continue
                elif 'letter' in player_action.upper() or 'letter' in player_action.lower():
                    print("\n~~~~~\nYou pick up the letter and read its sickly contents that glow red despite the darkness.")
                    print(color.RED + "\nMy dearest",name,",\n\tThere is a poison running through your veins. You have a month's time to cure yourself, or you shall meet Death. The answer lies in the", color.BOLD + 'village.' + color.END)
                    print(f"\nYou put down the letter, panic rising within your chest.")
                    letter = 0
                    continue
                else:
                    print("\n- Invalid Input -\n")
#Graveyard              
        while room == 'GRAVEYARD':
            if intro2 == 0:
                print("\n~~~~~\nYou now stand in an empty graveyard.")
                print("\nTombs cover every inch of the open hillscape, bathed in an eery moonlight.")
                intro2 = 1
                break
            while intro2 == 1:
                if cancel == 1:
                    cancel = 0
                    break
                player_action = input()
                if 'look' in player_action.upper() or 'look' in player_action.lower():
                    print("\n~~~~~\nA lone", color.BOLD + 'tree' + color.END, "stands pale and barren against the black sky. "
                          "In the distance you see a crooked gate where the sea of tombstones end, adorned on either side by", color.BOLD + 'gargoyles.' + color.END, "Past the gate, "
                          "a forked stone path leads beyond the horizon. From the", color.BOLD + 'left path' + color.END, ", you can make out a shadowy forest. From the", color.BOLD + 'right path' + color.END, ", you can see dim lights almost completely swallowed by the oppressive night. "
                          "The", color.BOLD + 'shed' + color.END, "lies behind you.")
                    continue
                elif 'tree' in player_action.upper() or 'tree' in player_action.lower():
                    print("\n~~~~~\nThe gnarled tree gets worse the longer you stare at it.")
                    while locket == 1:
                        tree_search = input('\nShould you search further?\n')
                        if 'yes' in tree_search.upper() or 'yes' in tree_search.lower() or 'search' in tree_search.upper() or 'search' in tree_search.lower():
                            print("\n~~~~~\nNoticing a hole in the wooden flesh, you reach inside and find a", color.BOLD + 'locket.' + color.END, "Inside is a faded picture of a young woman with hollow eyes.")
                            if a == '( )':
                                a = 'Old Locket'
                                locket = 0
                                break
                            elif b == '( )':
                                b = 'Old Locket'
                                locket = 0
                                break
                            elif c == '( )':
                                c = 'Old Locket'
                                locket = 0
                                break
                            elif d == '( )':
                                d = 'Old Locket'
                                locket = 0
                                break
                            elif e == '( )':
                                e = 'Old Locket'
                                locket = 0
                                break
                            elif f == '( )':
                                f = 'Old Locket'
                                locket = 0
                                break
                            elif g == '( )':
                                g = 'Old Locket'
                                locket = 0
                                break
                            elif h == '( )':
                                h = 'Old Locket'
                                locket = 0
                                break
                            elif i == '( )':
                                i = 'Old Locket'
                                locket = 0
                                break
                            elif j == '( )':
                                j = 'Old Locket'
                                locket = 0
                                break
                            else:
                                print("\n~~~~~\nYour backpack is full.")
                                break
                        elif 'no' in tree_search.upper() or 'no' in tree_search.lower() or 'back' in tree_search.upper() or 'back' in tree_search.lower():
                            print("\n~~~~~\nYou return to the courtyard.")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    while locket == 0:
                        tree_search = input('\nShould you search further?\n')
                        if 'yes' in tree_search.upper() or 'yes' in tree_search.lower() or 'search' in tree_search.upper() or 'search' in tree_search.lower():
                            print("\n~~~~~\nAn old dead tree. You turn back to the courtyard.")
                            break
                        elif 'no' in tree_search.upper() or 'no' in tree_search.upper() or 'back' in tree_search.upper() or 'back' in tree_search.lower():
                            print("\n~~~~~\nYou return to the courtyard.")
                            break
                        elif 'backpack' in tree_search.upper() or 'backpack' in tree_search.upper():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in tree_search.upper() or 'inventory' in tree_search.upper():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'money' in tree_search.upper() or 'money' in tree_search.upper():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'no' in tree_search.upper() or 'no' in tree_search.lower() or 'back' in tree_search.upper() or 'back' in tree_search.lower():
                            print("\n~~~~~\nYou return to the courtyard.")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                elif 'gargoyle' in player_action.upper() or 'gargoyle' in player_action.lower():
                    print("\n~~~~~\nYou approach the stone figures, their eyes gleaming", color.GREEN + color.BOLD + 'green.' + color.END)
                    while gem == 1:
                        garg_inspect = input()
                        if 'search' in garg_inspect.upper() or 'search' in garg_inspect.lower() or 'inspect' in garg_inspect.upper() or 'inspect' in garg_inspect.lower() and gem == 1:
                            print("\n~~~~~\nThe gargoyles\' eyes seem to be made from glimmering jewels. You crudely pry them from their sockets.\n\nMoney + 50")
                            gems = gems + 50
                            gem = 0
                            break
                        elif 'backpack' in garg_inspect.upper() or 'backpack' in garg_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in garg_inspect.upper() or 'inventory' in garg_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'money' in garg_inspect.upper() or 'money' in garg_inspect.lower():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'back' in garg_inspect.upper() or 'back' in garg_inspect.lower():
                            print("\n~~~~~\nYou turn back to the courtyard.")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    while gem == 0:
                        garg_inspect = input()
                        if 'search' in garg_inspect.upper() or 'search' in garg_inspect.lower() or 'inspect' in garg_inspect.upper() or 'inspect' in garg_inspect.lower() and gem == 1:
                            print("\n~~~~~\nTheir eyes are empty. You return to the courtyard.")
                            break
                        elif 'backpack' in garg_inspect.upper() or 'backpack' in garg_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in garg_inspect.upper() or 'inventory' in garg_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'money' in garg_inspect.upper() or 'money' in garg_inspect.lower():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'back' in garg_inspect.upper() or 'back' in garg_inspect.lower():
                            print("\n~~~~~\nYou turn back to the courtyard.")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                elif 'shed' in player_action.upper() or 'shed' in player_action.lower() or 'back' in player_action.upper() or 'back' in player_action.lower():
                    print("\n~~~~~\nYou turn around and head back into the dilapitated shed.")
                    room = 'INTRO'
                    life_span = life_span - 1
                    break
                elif 'left path' in player_action.upper() or 'left path' in player_action.lower():
                    if intro3 == 0:
                        print("\n~~~~~\nYour conscious tells you to choose the", color.BOLD + 'right path,' + color.END, "but your hungering curiosity yearns for the dark forest.")
                        intro3 = 1
                        room = 'FOREST'
                        life_span = life_span - 1
                        break
                    elif intro3 == 1:
                        print("\n~~~~~\nYou head into the maw of the dark forest.")
                        room = 'FOREST'
                        life_span = life_span - 1
                        break
                elif 'right path' in player_action.upper() or 'right path' in player_action.lower():
                    if intro4 == 0: 
                        print("\n~~~~~\nGuided by the hopeful lights in the distance, you make your way down the right path in the hopes of finding the answers you seek.")
                        print("\n~~~~~\nThe gently swaying lanterns are the only warmth to be found within the village. You walk down the cracked stone street, passing unlit windows. From inside one, you see a pale young girl staring through you until she catches your gaze and ducks out of sight. ")
                        print("\nAfter searching the boarded windows, you finally spot an old man with a scared look beckoning you from behind the cover of his shoddy wooden door. "
                              "With no other choice, you quickly follow him into his home. He doesn't say a word as he pours some sort of liquid "
                              "into a mug, but his eyes are no longer filled with fear. He hobbles over to you with the mug and sets it on the table in front of you.")
                        print('"It is you, the cursed', color.RED + color.BOLD + name + color.END, '. You were not meant to survive."')
                        print('\nHe lays an old book on the table and flips to a page depicting a man with the head and hooves of a goat.')
                        print('"You''ll find', color.BOLD + 'Him' + color.END, 'deep within that condemned forest. Take one of his horns and bring it to me. I will use it to craft the holy antidote to your ailment. '
                              'The poison will take your life', color.BOLD + 'within' + color.END, life_span, color.BOLD + 'days.' + color.END, 'God save you."')
                        print("You leave the old man's house and return to the village.")
                        intro4 = 1
                        room = 'VILLAGE'
                        life_span = life_span - 1
                        break
                    if intro4 == 1:
                        print("\n~~~~~\nYou head into the village.")
                        room = 'VILLAGE'
                        life_span = life_span - 1
                        break
                elif 'life' in player_action.upper() or 'life' in player_action.lower():
                    life(life_span)
                    continue
                elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                    life(life_span)
                    continue
                elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'money' in player_action.upper() or 'money' in player_action.lower():
                    money(gems)
                    continue
                else:
                    print("\n- Invalid Input -\n")
#Forest
        while room == 'FOREST':
            if intro5 == 0:
                print("\n~~~~~\nYou continue to walk deeper into the lair of thorns and branches.")
                intro5 = 1
                break
            while intro5 == 1:
                if cancel == 1:
                    cancel = 0
                    break
                while castle == 0:
                    if cancel == 1:
                        break
                    path_choice1 = 1
                    path_choice2 = 0
                    path_choice3 = 0
                    while path_choice1 == 1:
                        print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END, 'or', color.BOLD + 'right' + color.END)
                        player_action = input()
                        if ('left' in player_action.upper() or 'left' in player_action.lower()) and path_choice1 == 1:
                            print("\n~~~~~\nThe path forward becomes clearer.")
                            path_choice1 = 0
                            path_choice2 = 1
                            break
                        if ('middle' in player_action.upper() or 'middle' in player_action.lower() or 'right' in player_action.upper() or 'right' in player_action.lower()):
                            print("\nYou lose yourself in the forest...")
                            path_choice1 = 1
                            path_choice2 = 0
                            path_choice3 = 0
                            break
                        if 'look' in player_action.upper() or 'look' in player_action.lower():
                            print("\n~~~~~\nYou are surrounded on all sides by a dense thick folliage.")
                            continue
                        if 'search' in player_action.upper() or 'look' in player_action.lower():
                            print("\n~~~~~\nA", color.GREEN + color.BOLD + 'green glint' + color.END, "in the leaves catches your eye.")
                            money = money + 25
                            continue
                        elif 'money' in player_action.upper() or 'money' in player_action.lower():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        if 'back' in player_action.upper() or 'back' in player_action.lower():
                            print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                            room = 'GRAVEYARD'
                            life_span = life_span - 1
                            cancel = 1
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    while path_choice2 == 1:
                        print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END, 'or', color.BOLD + 'right' + color.END)
                        player_action = input()
                        if ('right' in player_action.upper() or 'right' in player_action.lower()):
                            print("\n~~~~~\nThe path forward becomes clearer.")
                            path_choice2 = 0
                            path_choice3 = 1
                            break
                        if ('left' in player_action.upper() or 'left' in player_action.lower() or 'middle' in player_action.upper() or 'middle' in player_action.lower()) and path_choice2 == 1:
                            print("\nYou lose yourself in the forest...")
                            path_choice1 = 1
                            path_choice2 = 0
                            path_choice3 = 0
                            break
                        if 'look' in player_action.upper() or 'look' in player_action.lower():
                            print("\n~~~~~\nYou are surrounded on all sides by a dense thick folliage.")
                            continue
                        elif 'money' in player_action.upper() or 'money' in player_action.lower():
                            money(gems)
                            continue
                        elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        if 'back' in player_action.upper() or 'back' in player_action.lower():
                            print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                            room = 'GRAVEYARD'
                            life_span = life_span - 1
                            cancel = 1
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    while path_choice3 == 1:
                        print("\nThe path suddenly splits into three;", color.BOLD + 'left, middle' + color.END, 'or', color.BOLD + 'right' + color.END)
                        player_action = input()
                        if ('middle' in player_action.upper() or 'middle' in player_action.lower()) and path_choice3 == 1:
                            print("\n~~~~~\nThe path forward reveals a sprawling castle. Its spires pierce the moonlight.")
                            print("A", color.BOLD + 'bridge' + color.END, 'separates you and the fortress, blocked by what appears to be a knight in haunting black armor.')
                            castle = 1
                            break
                        if ('left' in player_action.upper() or 'left' in player_action.lower() or 'right' in player_action.upper() or 'right' in player_action.lower()) and path_choice3 == 1:
                            print("\nYou lose yourself in the forest...")
                            path_choice1 = 1
                            path_choice2 = 0
                            path_choice3 = 0
                            break
                        if 'look' in player_action.upper() or 'look' in player_action.lower():
                            print("\n~~~~~\nA tall tower looms somewhere up ahead.")
                            continue
                        elif 'money' in player_action.upper() or 'money' in player_action.lower():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        if 'back' in player_action.upper() or 'back' in player_action.lower():
                            print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                            room = 'GRAVEYARD'
                            life_span = life_span - 1
                            cancel = 1
                            break
                        else:
                            print("\n- Invalid Input -\n")
                while castle == 1:
                    if castle_intro == 0:
                        print("\n~~~~~\nThe forest reveals the beaten path and you can see the", color.BOLD + 'castle' + color.END, "through the trees.")
                        castle_intro = 1
                        break
                    if castle_intro == 1:
                        player_action = input()
                        if 'castle' in player_action.upper() or 'castle' in player_action.lower():
                            room = 'CASTLE'
                            life_span = life_span - 1
                            cancel = 1
                            break
                        if 'look' in player_action.upper() or 'look' in player_action.lower():
                            print("\n~~~~~\nThe dark forest knows its tricks are beaten. The", color.BOLD + "castle" + color.END, "reveals itself through the thick branches.")
                            continue
                        elif 'money' in player_action.upper() or 'money' in player_action.lower():
                            money(gems)
                            continue
                        elif 'life' in player_action.upper() or 'life' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                            life(life_span)
                            continue
                        elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        if 'back' in player_action.upper() or 'back' in player_action.lower():
                            print("\n~~~~~\nYou somehow find the path back towards the entrance of the forest and head to the graveyard.")
                            room = 'GRAVEYARD'
                            life_span = life_span - 1
                            cancel = 1
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    
        while room == 'VILLAGE':
            if intro6 == 0:
                print("\n~~~~~\nYou enter the forgotten village.")
                intro6 = 1
                break
            while intro6 == 1:
                if cancel == 1:
                    break
                player_action = input()
                if 'look' in player_action.upper() or 'look' in player_action.lower():
                    print('\n~~~~~\nYou stand in what you assume to be the town square. The cracked stone streets are bordered by short '
                          'cobbled shacks, their wood structures rotting. In the center of the square is an old', color.BOLD + 'well.' + color.END, 'There are three storefronts closest to it, '
                          'and despite their faded signs you can read; "', color.BOLD + 'GEAR, FOOD,' + color.END, 'and', color.BOLD + 'MYSTICS'+ color.END)
                elif 'well' in player_action.upper() or 'well' in player_action.lower():
                    print("\n~~~~~\nYou approach the moss covered well, the only thing in this town with vegetation. "
                          "Something glows underneath the algae of the water.")
                    while token == 1:
                        well_inspect = input()
                        if 'search' in well_inspect.upper() or 'search' in well_inspect.lower() or 'inspect' in well_inspect.upper() or 'inspect' in well_inspect.lower() and token == 1:
                            print("\n~~~~~\nYou reach into the murk and find a "
                                  "large gold coin depicting a goddess.")
                            if a == '( )':
                                a = 'Holy Token'
                                token = 0
                            elif b == '( )':
                                b = 'Holy Token'
                                token = 0
                            elif c == '( )':
                                c = 'Holy Token'
                                token = 0
                            elif d == '( )':
                                d = 'Holy Token'
                                token = 0
                            elif e == '( )':
                                e = 'Holy Token'
                                token = 0
                            elif f == '( )':
                                f = 'Holy Token'
                                token = 0
                            elif g == '( )':
                                g = 'Holy Token'
                                token = 0
                            elif h == '( )':
                                h = 'Holy Token'
                                token = 0
                            elif i == '( )':
                                i = 'Holy Token'
                                token = 0
                            elif j == '( )':
                                j = 'Holy Token'
                                token = 0
                            else:
                                print("\n~~~~~\nYour backpack is full.")
                                break
                        elif 'backpack' in well_inspect.upper() or 'backpack' in well_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in well_inspect.upper() or 'inventory' in well_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'money' in well_inspect.upper() or 'money' in well_inspect.lower():
                            money(gems)
                            continue
                        elif 'life' in well_inspect.upper() or 'life' in well_inspect.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in well_inspect.upper() or 'days remaining' in well_inspect.lower():
                            life(life_span)
                            continue
                        elif 'back' in well_inspect.upper() or 'back' in well_inspect.lower():
                            print("\n~~~~~\nYou turn back to the village")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                    while token == 0:
                        well_inspect = input()
                        if 'search' in well_inspect.upper() or 'search' in well_inspect.lower() or 'inspect' in well_inspect.upper() or 'inspect' in well_inspect.lower() and token == 0:
                            print("\n~~~~~\nJust an old well. You return to the village.")
                            break
                        elif 'backpack' in well_inspect.upper() or 'backpack' in well_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'inventory' in well_inspect.upper() or 'inventory' in well_inspect.lower():
                            inv(a, b, c, d, e, f, g, h, i, j)
                            continue
                        elif 'money' in well_inspect.upper() or 'money' in well_inspect.lower():
                            money(gems)
                            continue
                        elif 'life' in well_inspect.upper() or 'life' in well_inspect.lower():
                            life(life_span)
                            continue
                        elif 'days remaining' in well_inspect.upper() or 'days remaining' in well_inspect.lower():
                            life(life_span)
                            continue
                        elif 'back' in well_inspect.upper() or 'back' in well_inspect.lower():
                            print("\n~~~~~\nYou turn back to the courtyard.")
                            break
                        else:
                            print("\n- Invalid Input -\n")
                elif 'graveyard' in player_action.upper() or 'graveyard' in player_action.lower():
                    print("\n~~~~~\nYou take the beaten path back to the graveyard, never looking back.")
                    room = 'GRAVEYARD'
                    life_span = life_span - 1
                    cancel = 1
                    break
                elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'money' in player_action.upper() or 'money' in player_action.lower():
                    money(gems)
                    continue
                elif 'life' in player_action.upper() or 'life' in player_action.lower():
                    life(life_span)
                    continue
                elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                    life(life_span)
                    continue
                else:
                    print("\n- Invalid Input -\n")
        while room == 'CASTLE':
            if intro7 == 0:
                print("\n~~~~~\nThe castle is a menacing fortress  with towering pillars and black spires that stretch into the night sky. "
                      "In front of the castle lies a", color.BOLD + 'river' + color.END, "that is lost beyond sight into the woods. "
                      "Spanning the black waters is a well worn", color.BOLD + 'bridge,' + color.END, "and at the end is a knight in ornate black armor.")
                intro7 = 1
                break
            while intro7 == 1:
                print("\n~~~~~\nThe castle looms up ahead.")
                player_action = input()
                if 'look' in player_action.upper() or 'look' in player_action.lower():
                    print()
                elif 'backpack' in player_action.upper() or 'backpack' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'inventory' in player_action.upper() or 'inventory' in player_action.lower():
                    inv(a, b, c, d, e, f, g, h, i, j)
                    continue
                elif 'money' in player_action.upper() or 'money' in player_action.lower():
                        money(gems)
                        continue
                elif 'life' in player_action.upper() or 'life' in player_action.lower():
                    life(life_span)
                    continue
                elif 'days remaining' in player_action.upper() or 'days remaining' in player_action.lower():
                    life(life_span)
                    continue
                else:
                    print("\n- Invalid Input -\n")
        
             
                
    


