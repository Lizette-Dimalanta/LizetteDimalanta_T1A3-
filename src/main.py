from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import art

x = PrettyTable()

# TEXT LOG ----------------------------------------------------------
TITLE = """
        _.-^^---....,,--       
    _--                  --_  
   <                        >)
   |                         |
   \\._                   _./ 
        ```--. . , ; .--'''    
            | |   |       
         .-=||  | |=-.   
         `-=#$%&%$#=-'   
            | ;  :|     
    _____.,-#%&$@%#&#~,._____

    ██████╗░░█████╗░░█████╗░███████╗██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║
    ██████╔╝██║░░██║██║░░██║█████╗░░██║
    ██╔═══╝░██║░░██║██║░░██║██╔══╝░░╚═╝
    ██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░██╗
    ╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
"""

LOG_1 = """
____________________________________________________________________

I woke up at my desk. I remember being awake all night but my memory is foggy. 
The room smells of smoke, it seems like something happened here.
 ...
It's dark, the light switch doesn't seem to turn on.
There is a matchbox in my pocket with a single match left.
____________________________________________________________________
"""

LIGHT_MATCH = """
(Inventory: match -1)
              )
             (_)
            .-'-.
            |   |
            |   |
            |   |
            |   |
          __|   |__   .-.
       .-'  |   |  `-:   :
      :     `---'     :-'
  jgs  `-._       _.-'
            '""""""

I light the match. I see a candle - I'll light it on that.
____________________________________________________________________
"""

FIND_TORCH = """I search the shelf for a torch. CLICK! It's bright!
____________________________________________________________________
"""

LOG_2 = """ I could barely see past this fog, but something definitely happened here.
This room is a mess.
__ _____ ____ _____ ______ _______ _____ ______ ______ ______ ___
__]_____]____]_____]______]_______]_____]______]______]______]___]
             _                       _______  |||"||;;|.||##||=|||
  _                           _     |   *  3| |||-|| =|-||==||+|||
  ____________       _              |       | |||_||__|_||__||_|||
|`.   --__     `.        _______    |       | ||================||
|  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||
|   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||
|   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||
|   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||
|   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||
|`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||
|  `|_|===========||_|  _____      ____(____)-.'(o)_|__|_|__|__|||
|   | |  .-------.||   `. ~~~ `.  `. ~~~ `.    `._\=============||
|   | |  |       |||     `. ____`.  `._____`.    `.     |       ||
|   | |`.|  ==== |||`._____________________________`.  o|o      ||
|`. | |`.|_______||| |._.----------------.__.-------.|__|_______||
|  `|_|===========|| || '----------------'  | .---. ||  __
|   | |  .-------.|| ||               |     |_______||.'\.'.     ,   .
|   | |  |       ||| || ______________|     | .---. ||'.__.'    .  .
|   | |`.|  ==== ||| ||   .          . `.   |_______|||  _ |  .       /
 `. | |`.|_______||| || ,     ,  .     @ `. | .---. |||_  ||     @
   `|_|===========||`||     ,   @      ,   `|_______|||____|      , .
       .         @      `.     ,        .     `.   .          ;
        @    .         ,  `.____________________`.     @.   ,    ,
      .     ,   `        ,    @       , '      ,        .      .      .
  ...
What's this?
 """

LOG_3 = """
Is this my handwriting?
  .----------------.   .----------------.
 | .--------------. | | .--------------. |
 | |   RECIPE 1   | | | |   RECIPE 2   | |
 | |              | | | |              | |
 | |   Aconitum   | | | |  Asteraceae  | |
 | |   Lucanidae  | | | |  Nightshade  | |
 | | Cerambycidae | | | | Chanterelle  | |
 | |      = ?     | | | |     = ?      | |
 | |              | | | |              | |
 | '--------------' | | '--------------' |
  '----------------'   '----------------'

It seems to be two recipes of some sort.
____________________________________________________________________

I'm sure they're somewhere.
"""

# FUNCTIONS ---------------------------------------------------------------------
# Start Menu
def start_menu():
        """ Title screen menu.
        """
        options = ["Start", "Quit"]
        start_options = TerminalMenu(options, clear_screen = False, title = "What happened here?")
        quit_menu = False

        while quit_menu == 0:
            options_choice = start_options.show()
            if options_choice == 0:
                quit_menu = True

            elif options_choice == 1:
                quit()

if __name__ == "__main__":
    start_menu()

# Choice Point: Use Match
def match_log():
    """Match Response
    """
    options = ["Yes (-1 match)", "No"]
    terminal_menu = TerminalMenu(options, title = "Should I use the match?")
    quit_menu = False

    while quit_menu == 0:
        options_choice = terminal_menu.show()
        if options_choice == 0:
            x.field_names = ["Item", "Quantity"]
            x.add_row(["Match", 0])
            print(x)
            print(LIGHT_MATCH)
            quit_menu = True

        elif options_choice == 1:
            print(FIND_TORCH)
            quit_menu = True

if __name__ == "__main__":
    match_log()

# Inspect Room
def inspect_room():
    """Continues to next dialogue.
    """
    button = ["Inspect Room"]
    terminal_menu = TerminalMenu(button)
    quit_menu = False

    while quit_menu == 0:
        button = terminal_menu.show()
        print(LOG_2)
        quit_menu = True

if __name__ == "__main__":
    inspect_room()

# Inspect Desk
def inspect_desk():
    """Introduce two recipes.
    """
    button = ["Inspect Desk"]
    terminal_menu = TerminalMenu(button)
    quit_menu = False

    while quit_menu == 0:
        button = terminal_menu.show()
        print(LOG_2)
        quit_menu = True

if __name__ == "__main__":
    inspect_desk()

# Choice Point: Choose Recipe
def choose_recipe():
    """User chooses a recipe.
    """
    recipe = ["Recipe 1", "Recipe 2"]
    terminal_menu = TerminalMenu(recipe, title = "Which recipe should I pick up?")
    RECIPE_CHOICE = """ Alright. {recipe_choice} it is.
    (+1 Recipe)
    """

    quit_menu = False

    while quit_menu == 0:
        recipe_choice = terminal_menu.show()
        if recipe_choice == 0:
            print("Alright. {recipe_choice} it is. \n(+1 Recipe)")
            x.field_names = ["Item", "Quantity", "Description"]
            x.add_row(["Recipe 1", 1, "A recipe of some sort."])
            print(x)
            quit_menu = True

        elif recipe_choice == 1:
            print("Alright. I'll go with Recipe 2.")
            print("(+1 Recipe)")
            x.field_names = ["Item", "Quantity", "Description"]
            x.add_row(["Recipe 2", 1, "A recipe of some sort."])
            print(x)
            quit_menu = True

if __name__ == "__main__":
    choose_recipe()

# MAIN PROGRAM -----------------------------------------------------------------
def main_program():
    """ Program that executes the game.
    """
    # Title Screen
    print(TITLE)

    # Start Menu
    start_menu()

    # DIAGLOGUE: Part 1
    print(LOG_1)

    # USER INPUT: Use Match?
    match_log()

    # DIAGLOGUE: Part 2 + Inspect Room
    inspect_room()

    # Continue Story: Inspect Desk
    inspect_desk()

    # USER INPUT: Choose recipe
    choose_recipe()

# def choose_recipe():
#     """User chooses a recipe.
#     """
#     options = ["Recipe 1", "Recipe 2"]
#     terminal_menu = TerminalMenu(options, title = "Which recipe should I pick up?")
#     quit_menu = False

#     while quit_menu == 0:
#         options_choice = terminal_menu.show()
#         if options_choice == 0:
#             print("Alright. Recipe 1 it is.")
#             print("(+1 Recipe)")
#             x.field_names = ["Item", "Quantity", "Description"]
#             x.add_row(["Recipe 1", 1, "A recipe of some sort."])
#             print(x)
#             quit_menu = True

#         elif options_choice == 1:
#             print("Alright. I'll go with Recipe 2.")
#             print("(+1 Recipe)")
#             x.field_names = ["Item", "Quantity", "Description"]
#             x.add_row(["Recipe 2", 1, "A recipe of some sort."])
#             print(x)
#             quit_menu = True

# if __name__ == "__main__":
#     choose_recipe()

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

main_program()

        #     x.field_names = ["Item", "Quantity"]
        #     x.add_row(["Match", 0])
        #     print(x)
        #     print(LIGHT_MATCH)
        #     quit_menu = True

        # elif options_choice == 1:
        #     print(FIND_TORCH)
        #     quit_menu = True


# recipe_1 = [
#     {'Aconitum' : "rack"},
#     {'Lucanidae' : "drawers"},
#     {'Cerambycidae' : "jars"}
# ]

# recipe_2 = [
#     {'Asteraceae' : "drawers"},
#     {'Nightshade' : "jars"},
#     {'Chanterelle' : "rack"}
# ]

# variable = function
inspect_Input = input("Where should I look first? [rack / drawers / jars]")


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

