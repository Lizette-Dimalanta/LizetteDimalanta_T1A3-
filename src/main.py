"""POOF! A mysterious situation?
   A text-based mystery game."""

from simple_term_menu import TerminalMenu
import colorama
from colorama import Back, Fore, Style
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
from prettytable.colortable import ColorTable, Themes

colorama.init(autoreset=True)
x = PrettyTable()
x.set_style(DOUBLE_BORDER)
x = ColorTable(theme=Themes.OCEAN)
x.field_names = ["Item", "Quantity", "Description"]

# Recipe List
recipe_1 = ["Recipe 1", "Aconitum", "Lucanidae", "Sage"]
recipe_2 = ["Recipe 2", "Asteraceae", "Nightshade", "Chanterelle", "Match"]

# All Items in Game
storage = ["Torch", "Recipe 1", "Recipe 2", "Aconitum", "Lucanidae", "Sage", "Asteraceae", "Nightshade", "Chanterelle"]
inventory = ["Match"]
# inventory.extend(storage)

# FUNCTIONS ---------------------------------------------------------------------
def title_art():
    """ Title Art """
    print(f"{Fore.LIGHTWHITE_EX + Style.BRIGHT}            _.-^^---....,,--")
    print(f"{Fore.WHITE + Style.BRIGHT}        _--                  --_")
    print(f"{Fore.LIGHTWHITE_EX + Style.BRIGHT}       <                        >)")
    print(f"{Fore.WHITE + Style.BRIGHT}       |                         |")
    print(f"{Fore.WHITE + Style.NORMAL}        \\._                   _./")
    print(f"{Fore.WHITE + Style.BRIGHT}            ```--. . , ; .--'''")
    print(f"{Fore.LIGHTBLACK_EX + Style.BRIGHT}                | |   |")
    print(f"{Fore.WHITE + Style.BRIGHT}             .-=||  | |=-.")
    print(f"{Fore.LIGHTWHITE_EX + Style.BRIGHT}             `-=#$%&%$#=-'")
    print(f"{Fore.WHITE + Style.BRIGHT}                | ;  :|")
    print(f"{Fore.LIGHTBLACK_EX + Style.BRIGHT}        _____.,-#%&$@%#&#~,._____")
    print(f"{Fore.LIGHTBLUE_EX}\n    ██████╗░░█████╗░░█████╗░███████╗██╗")
    print(f"{Fore.CYAN}    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║")
    print(f"{Fore.LIGHTCYAN_EX + Style.BRIGHT}    ██████╔╝██║░░██║██║░░██║█████╗░░██║")
    print(f"{Fore.CYAN}    ██╔═══╝░██║░░██║██║░░██║██╔══╝░░╚═╝")
    print(f"{Fore.LIGHTBLUE_EX}    ██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░██╗")
    print(f"{Fore.BLUE}    ╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝\n")

def log_1():
    """ Introduction Log """
    print(f"{Fore.LIGHTBLACK_EX}____________________________________________________________________")
    print(f"{Style.BRIGHT}\nI woke up at my desk. I remember being awake all night but my memory is foggy.")
    print(f"{Style.BRIGHT}The room smells of smoke, it seems like something happened here.                ")
    print(f"{Style.BRIGHT}  ...  ")
    print(f"{Style.BRIGHT}\nIt's dark, the light switch doesn't seem to turn on.      ")
    print(f"{Style.BRIGHT}There is a matchbox in my pocket with a single match left.")
    print(f"{Fore.LIGHTBLACK_EX}\n____________________________________________________________________\n")

def light_match():
    """ Light Match Response """
    print(f"{Fore.WHITE + Style.DIM}      (Inventory: match -1)")
    print(f"{Fore.YELLOW + Style.BRIGHT}\n              )")
    print(f"{Fore.YELLOW + Style.BRIGHT}             (_)")
    print(f"{Fore.LIGHTRED_EX}            .-'-.")
    print(f"{Fore.LIGHTRED_EX}            |   |")
    print(f"{Fore.LIGHTRED_EX + Style.DIM}            |   |")
    print(f"{Fore.YELLOW + Style.DIM}            |   |")
    print(f"{Fore.YELLOW + Style.DIM}            |   |")
    print(f"{Fore.LIGHTYELLOW_EX + Style.DIM}          __|   |__   .-.")
    print(f"{Fore.YELLOW + Style.DIM}       .-'  |   |  `-:   :")
    print(f"{Fore.LIGHTRED_EX + Style.DIM}      :     `---'     :-'")
    print(f"{Fore.LIGHTRED_EX}       `-._       _.-'")
    print(f"{Style.BRIGHT}\n I light the match. I see a candle - I'll light it on that.")
    print(f"{Fore.LIGHTBLACK_EX}____________________________________________________________________")

def find_torch():
    """ Find Torch Response """
    print(f"{Fore.CYAN + Style.DIM}                      _.----.               .   *   ")
    print(f"{Fore.CYAN + Style.NORMAL}    .----------------' /  /  \\     .   '    ,   '    ")
    print(f"{Fore.CYAN + Style.BRIGHT}   (    [ ]         | |   |) |   '  *CLICK!*   .   *  ")
    print(f"{Fore.CYAN + Style.NORMAL}    `----------------._\  \  /  '    '    .   *   '  ")
    print(f"{Fore.CYAN + Style.DIM}                       '----'           '    .   *  ")
    print(f"{Style.BRIGHT}\nI search the shelf for a torch. CLICK! It's bright!")
    print(f"{Fore.LIGHTBLACK_EX}____________________________________________________________________")

def log_2():
    """ Log 2 """
    print(f"{Style.BRIGHT}\nI could barely see past this fog, but something definitely happened here.")
    print(f"{Style.BRIGHT}This room is a mess.")
    print(f"{Fore.YELLOW + Style.NORMAL}\n__ _____ ____ _____ ______ _______ _____ ______ ______ ______ ___")
    print(f"{Fore.YELLOW + Style.BRIGHT}__]_____]____]_____]______]_______]_____]______]______]______]___]")
    print(f"{Fore.YELLOW + Style.DIM}             _                       _______  |||'||;;|.||##||=|||")
    print(f"{Fore.YELLOW + Style.DIM}  _                           _     |   *  3| |||-|| =|-||==||+|||")
    print(f"{Fore.YELLOW + Style.DIM}  ____________       _              |       | |||_||__|_||__||_|||")
    print(f"{Fore.YELLOW + Style.NORMAL}|`.   --__     `.        _______    |       | ||================||")
    print(f"{Fore.YELLOW + Style.NORMAL}|  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||")
    print(f"{Fore.YELLOW + Style.NORMAL}|   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||")
    print(f"{Fore.YELLOW + Style.NORMAL}|   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||")
    print(f"{Fore.YELLOW + Style.NORMAL}|   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|  `|_|===========||_|  _____      ____(____)-.'(o)_|__|_|__|__|||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|   | |  .-------.||   `. ~~~ `.  `. ~~~ `.    `._\=============||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|   | |  |       |||     `. ____`.  `._____`.    `.     |       ||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|   | |`.|  ==== |||`._____________________________`.  o|o      ||")
    print(f"{Fore.YELLOW + Style.BRIGHT}|`. | |`.|_______||| |._.----------------.__.-------.|__|_______||")
    print(f"{Fore.YELLOW + Style.NORMAL}|  `|_|===========|| || '----------------'  | .---. ||  __")
    print(f"{Fore.YELLOW + Style.NORMAL}|   | |  .-------.|| ||               |     |_______||.'\.'.     ,   .")
    print(f"{Fore.YELLOW + Style.NORMAL}|   | |  |       ||| || ______________|     | .---. ||'.__.'    .  .")
    print(f"{Fore.YELLOW + Style.DIM}|   | |`.|  ==== ||| ||   .          . `.   |_______|||  _ |  .       /")
    print(f"{Fore.YELLOW + Style.DIM} `. | |`.|_______||| || ,     ,  .     @ `. | .---. |||_  ||     @")
    print(f"{Fore.YELLOW + Style.DIM}   `|_|===========||`||     ,   @      ,   `|_______|||____|      , .")
    print(f"{Fore.YELLOW + Style.DIM}       .         @      `.     ,        .     `.   .          ;")
    print(f"{Fore.YELLOW + Style.DIM}        @    .         ,  `.____________________`.     @.   ,    ,")
    print(f"{Fore.YELLOW + Style.NORMAL}      .     ,   `        ,    @       , '      ,        .      .      .")
    print(f"{Style.BRIGHT}  ...")
    print(f"{Style.BRIGHT}\nWhat's this?")

# Recipe Introduction
def inspect_recipes():
    """ Recipe Introduction """
    print(f"{Style.BRIGHT}Is this my handwriting?")
    print(f"{Fore.GREEN + Style.DIM}  .----------------.   .----------------.")
    print(f"{Fore.GREEN + Style.NORMAL} | .--------------. | | .--------------. |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |   RECIPE 1   | | | |   RECIPE 2   | |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |              | | | |              | |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |   Aconitum   | | | |  Asteraceae  | |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |   Lucanidae  | | | |  Nightshade  | |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |     Sage     | | | | Chanterelle  | |")
    print(f"{Fore.GREEN + Style.BRIGHT} | |      = ?     | | | |     = ?      | |")
    print(f"{Fore.GREEN + Style.NORMAL} | |              | | | |              | |")
    print(f"{Fore.GREEN + Style.NORMAL} | '--------------' | | '--------------' |")
    print(f"{Fore.GREEN + Style.DIM}  '----------------'   '----------------'")
    print(f"{Style.BRIGHT}\nIt seems to be two recipes of some sort.")
    print(f"{Style.BRIGHT}\n____________________________________________________________________\n")

# MAIN PROGRAM --------------------------------------------------------------------
# Title Screen
title_art()

# Start Menu
def start_menu():
    """ Title Screen Menu """
    options = ["Start", "Quit"]
    start_options = TerminalMenu(options, title = "What happened here?")
    quit_menu = False

    while quit_menu == 0:
        options_choice = start_options.show()
        if options_choice == 0:
            quit_menu = True

        elif options_choice == 1:
            quit()

if __name__ == "__main__":
    start_menu()

# Log: Part 1
log_1()

# Choice Point: Use Match
def match_log():
    """ Match Response """
    options = ["Yes (-1 match)", "No"]
    terminal_menu = TerminalMenu(options, title = "\nShould I use the match?")
    quit_menu = False

    while quit_menu == 0:
        options_choice = terminal_menu.show()
        if options_choice == 0:
            # del inventory[0]
            inventory.remove("Match")
            x.add_row(["Match", 0, "-"])
            print(x)
            light_match()
            quit_menu = True
        elif options_choice == 1:
            # storage.pop(0)
            inventory.append("Torch")
            x.add_row(["Match", 1, "A single match left."])
            x.add_row(["Torch", 1, "A bright torch."])
            print(x)
            find_torch()
            quit_menu = True      

if __name__ == "__main__":
    match_log()

# Inspect Room + Log: Part 2
def inspect_room():
    """ Continues to next dialogue """
    button = ["Inspect Room"]
    terminal_menu = TerminalMenu(button)
    quit_menu = False

    while quit_menu == 0:
        button = terminal_menu.show()
        log_2()
        quit_menu = True

if __name__ == "__main__":
    inspect_room()

# Inspect Desk
def inspect_desk():
    """ Introduce two recipes """
    button = ["Inspect Desk"]
    terminal_menu = TerminalMenu(button)
    quit_menu = False

    while quit_menu == 0:
        button = terminal_menu.show()
        inspect_recipes()
        quit_menu = True

if __name__ == "__main__":
    inspect_desk()

# Choice Point: Choose Recipe
def choose_recipe():
    """ User presented with recipes """
    recipe_options = ["Recipe 1", "Recipe 2"]
    terminal_menu = TerminalMenu(recipe_options, title = "Which recipe should I pick up?")
    quit_menu = False

    while quit_menu == 0:
        recipe_number = terminal_menu.show()
        if recipe_number == 0:
            print(f"{Style.BRIGHT}Alright. Recipe 1 it is.\n")
            storage.remove("Recipe 1")
            inventory.append("Recipe 1")
            x.add_row(["Recipe 1", 1, "Aconitum, Lucanidae & Sage."])
            print(x)
            print(f"{Style.DIM}                        (+1 Recipe)\n")
            quit_menu = True

        elif recipe_number == 1:
            print(f"{Style.BRIGHT}Alright. I'll go with Recipe 2.\n")
            # storage.pop(3)
            storage.remove("Recipe 1")
            inventory.append("Recipe 2")
            x.add_row(["Recipe 2", 1, "Asteraceae, Nightshade & Chanterelle"])
            print(x)
            print(f"{Style.DIM}                        (+1 Recipe)\n")
            quit_menu = True

if __name__ == "__main__":
    choose_recipe()

# Choice Point: Inspect Storage
def inspect_storage():
    """ User inspects different storage locations """
    print(f"{Style.BRIGHT}Where should I look first?\n")
    storage_options = ["Inspect Rack of Vials", "Inspect Drawers", "Inspect Workbench Jars"]
    print(storage_options)
    storage_input = input("\n[ Vials / Drawers / Jars ]\n")
    storage_choice = storage_input.capitalize()
    quit_menu = False
    
    # while storage_input != "Vials" or "Drawers" or "Jars":
    #     print("I'm a bit confused. Where should I inspect?")
    #     storage_input = input("[ Vials / Drawers / Jars ]\n")
    #     storage_choice = storage_input.capitalize()
    # else:
    #     print("Gotcha.")
    #     break
        
    while quit_menu == 0:
        
        #Inspect Rack of Vials
        if storage_choice == "Vials":
            vials_options = ["Pick Up Aconitum", "Pick Up Chanterelle", "Back"]
            vials_menu = TerminalMenu(vials_options, title = "Which ingredient should I pick up?")
            vials_index = vials_menu.show()
            vials_menu_back = False

            while vials_menu_back is False:
                if vials_index == 0:
                    print("Picked up Aconitum.")
                    # storage.pop(3)
                    storage.remove("Aconitum")
                    inventory.append("Aconitum")
                    x.add_row(["Aconitum", 1, "A flowering plant belonging to the family Ranunculaceae."])
                    print(x)
                    print(f"{Style.DIM}                                  (+1 Aconitum)\n")
                    vials_menu_back = True
                    # del vials_options[0]

                elif vials_index == 1:
                    print("Picked up Chanterelle.")
                    # storage.pop(8)
                    storage.remove("Chanterelle")
                    inventory.append("Chanterelle")
                    x.add_row(["Chanterelle", 1, "Found in mossy coniferous forests."])
                    print(x)
                    print(f"{Style.DIM}                       (+1 Chanterelle)\n")
                    vials_menu_back = True
                    # del vials_options[1]

                elif vials_index == 2:
                    return inspect_storage()

                # print("Already got it! Please select another one.")


        # Inspect Drawers
        elif storage_choice == "Drawers":
            drawers_options = ["Pick Up Asteraceae", "Pick Up Nightshade", "Back"]
            drawers_menu = TerminalMenu(drawers_options, title = "Which ingredient should I pick up?")
            drawers_index = drawers_menu.show()
            drawers_menu_back = False

            while drawers_menu_back is False:
                if drawers_index == 0:
                    print("Picked up Asteraceae.")
                    # storage.pop(6)
                    storage.remove("Asteraceae")
                    inventory.append("Asteraceae")
                    x.add_row(["Asteraceae", 1, "The fair-maid-of-France."])
                    print(x)
                    print(f"{Style.DIM}                            (+1 Asteraceae)\n")
                    drawers_menu_back = True

                elif drawers_index == 1:
                    print("Picked up Nightshade.")
                    # storage.pop(7)
                    storage.remove("Nightshade")
                    inventory.append("Nightshade")
                    x.add_row(["Nightshade", 1, "The Solanaceae."])
                    print(x)
                    print(f"{Style.DIM}                       (+1 Nightshade)\n")
                    drawers_menu_back = True

        # Inspect Workbench Jars
        elif storage_choice == "Jars":
            jars_options = ["Pick Up Lucanidae", "Pick Up Cerambycidae", "Back"]
            jars_menu = TerminalMenu(jars_options, title = "Which ingredient should I pick up?")
            jars_index = jars_menu.show()

            if jars_index == 0:
                print("Picked up Lucanidae.")
                # storage.pop(4)
                storage.remove("Lucanidae")
                inventory.append("Lucanidae")
                x.add_row(["Lucanidae", 1, "Also known as Phylum Arthropoda."])
                print(x)
                print(f"{Style.DIM}                            (+1 Lucanidae)\n")
                quit_menu = True

            elif jars_index == 1:
                print("Picked up Sage.")
                # storage.pop(5)
                storage.remove("Sage")
                inventory.append("Sage")
                x.add_row(["Sage", 1, "An evergreen subshrub."])
                print(x)
                print(f"{Style.DIM}                             (+1 Sage)\n")
                quit_menu = True

if __name__ == "__main__":
    inspect_storage()

# MAIN PROGRAM: Unfinished -----------------------------------------------------------------

# def main_program():
#     """ Program that executes the game """
#     # Title Screen
#     title_art()

#     # Start Menu
#     start_menu()

#     # DIALOGUE: Part 1
#     log_1()

#     # USER INPUT: Use Match?
#     match_log()

#     # DIALOGUE: Part 2 + Inspect Room
#     inspect_room()

#     # Continue Story: Inspect Desk
#     inspect_desk()

#     # USER INPUT: Choose recipe
#     choose_recipe()

#     # USER INPUT: Choose recipe
#     inspect_storage()

# main_program()

# UNUSED CODE -----------------------------------------------------------------

# def inspect_storage():
#     """ User inspects different storage locations """
#     storage_options = ["Inspect Rack of Vials", "Inspect Drawers", "Inspect Workbench Jars"]
#     storage_menu = TerminalMenu(storage_options, title = "Where should I look?")
#     quit_menu = False
    
#     while not quit_menu:
#         options_index = storage_menu.show()
#         options_choice = storage_options[options_index]
#         quit_menu = True

#         if options_choice == 0:
#             storage_options.remove("Inspect Rack of Vials")
#             v

#         elif options_choice == 1:
#             pass

#         elif options_choice == 2:
#             quit_menu = True

# if __name__ == "__main__":
#     inspect_storage()

# def inspect_storage():
#     """ User inspects different storage locations """
#     storage_options = ["Inspect Rack of Vials", "Inspect Drawers", "Inspect Workbench Jars"]
#     quit_menu = False
#     storage_menu = TerminalMenu(storage_options, title = "Where should I look first?")

#     vials_items = ["Pick Up Aconitum", "Pick Up Chanterelle", "Back"]
#     vials_menu_back = False
#     vials_menu = TerminalMenu(vials_items, title = "Which ingredient should I pick up?")
    
#     while not quit_menu:
#         options_index = storage_menu.show()
#         options_choice = storage_options[options_index]

#         if options_choice == 0 and vials_menu_back is False:
#                 vials_index = vials_menu.show()
#                 vials_choice = vials_items[vials_index]
#                 if vials_choice == "Inspect Rack of Vials":
#                     print(f"{Style.BRIGHT} Picked up Aconitum.")
#                     inventory.append("Aconitum")
#                     x.add_row(["Aconitum", 1, "A flowering plant belonging to the family Ranunculaceae."])
#                     print(x)
#                     print(f"{Style.DIM}                      (+1 Aconitum)\n")
#                     quit_menu = True
#                 elif vials_choice == 1:
#                     print(f"{Style.BRIGHT} Picked up Chanterelle.")
#                     inventory.append("Chanterelle")
#                     x.add_row(["Chanterelle", 1, "Found in mossy coniferous forests."])
#                     print(x)
#                     print(f"{Style.DIM}                     (+1 Chanterelle)\n")
#                     quit_menu = True
#                 elif vials_choice == 2:
#                     vials_menu_back = True

#         elif options_choice == 1:
#             pass

#         elif options_choice == 2:
#             quit_menu = True

# if __name__ == "__main__":
#     inspect_storage()

#     x.field_names = ["Item", "Quantity", "Description"]
# x.add_row(["Match", 1, "It has one match left."])
# x.add_row(["Aconitum", 1, "Flowering plant belonging to the family Ranunculaceae."])
# x.add_row(["Lucanidae", 1, "Also known as Phylum Arthropoda."])
# x.add_row(["Asteraceae", 1, "The fair-maid-of-France."])
# x.add_row(["Nightshade", 1, "The Solanaceae."])
# x.add_row(["Chanterelle", 1, "Found in mossy coniferous forests."])

# USER INPUT: Inspect storage
# def inspect_storage():
#     """ User inspects different storage locations.
#     """
#     storage_options = ["Inspect Rack of Vials)", "Inspect Drawers", "Inspect Workbench Jars"]
#     quit_menu = False
#     storage_menu = TerminalMenu(storage_options, title = "Where should I look first?")

#     vials_items = ["Pick Up Aconitum", "Pick Up Chanterelle", "Back"]
#     vials_menu_back = False
#     vials_menu = TerminalMenu(vials_items, title = "Which ingredient should I pick up?")
    

#     while not quit_menu:
#         options_index = storage_menu.show()
#         options_choice = storage_options[options_index]

#         if options_choice == 0:
#             vials_menu_back = False
#             while vials_menu_back is False:
#                 vials_options_sel = vials_menu.show()
#                 if vials_options_sel == 0:
#                     pass
#                 elif vials_options_sel == 1:
#                     pass
#                 elif vials_options_sel == 2:
#                     vials_menu_back = True

#         elif options_choice == 1:
#             pass

# if __name__ == "__main__":
#     inspect_storage()

        #     x.field_names = ["Item", "Quantity"]
        #     x.add_row(["Match", 0])
        #     print(x)
        #     print(LIGHT_MATCH)
        #     quit_menu = True

        # elif options_choice == 1:
        #     print(FIND_TORCH)
        #     quit_menu = True

# variable = function


# if inspect_Input == "rack":
#     print(f"  Pick up {'Aconitum'}")
#     print(f" from)



# while True:
#     search_Input = input("Which should I pick up?")
#         if search_Input == 'rack':

#     for item in storage:
#         if item ['rack'] == storage:
#             print(f"I picked up the {item['storage']}! ")
#     else:
#         print(f"I couldn't find the {item['storage']}. ")

# feature 2


# feature 3