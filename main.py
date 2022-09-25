from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
x = PrettyTable()

TITLE = """
      _.-^^---....,,--       
  _--                  --_  
 <                        >)
 |                         |
  \._                   _./ 
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

print(TITLE)

def main():
    """title screen"""
    options = ["Start", "Quit"]
    terminal_menu = TerminalMenu(options, title = "What happened here?")
    quit_menu = False

    while quit_menu == 0:
        options_choice = terminal_menu.show()
        if options_choice == 0:
            quit_menu = True

        elif options_choice == 1:
            quit()

if __name__ == "__main__":
    main()

LOG_1 = """
_____________________________________________________

I woke up at my desk. I remember being awake all night but my memory is foggy. 
The room smells of smoke, it seems like something happened here.
...
It's dark, the light switch doesn't seem to turn on.
There is a matchbox in my pocket with a single match left.
_____________________________________________________
"""

print(LOG_1)

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
_____________________________________________________
"""

FIND_TORCH = """

I search the shelf for a torch. CLICK! It's bright!
_____________________________________________________
"""

def match_log():
    """Match Response Log"""
    match_input = input("Should I use the match? [yes (-1 match) / no]: ")
    if match_input == "yes":
        x.field_names = ["Item", "Quantity"]
        x.add_row(["Match", 0])
        print([x, LIGHT_MATCH])
    elif match_input == "no":
        print(FIND_TORCH)
    else:
        print("Hmm..")
        match_log()
match_log()

LOG_2 = """
I could barely see past this fog, but something definitely happened here. This room is a mess.

Is this my handwriting?
  .----------------.   .----------------.
 | .--------------. | | .--------------. |
 | |   RECIPE 1   | | | |   RECIPE 2   | |
 | |              | | | |              | |
 | |   Aconitum   | | | |  Asteraceae  | |
 | |   Lucanidae  | | | |  Nightshade  | |
 | | Cerambycidae | | | | Chanterelle  | |
 | |              | | | |              | |
 | '--------------' | | '--------------' |
  '----------------'   '----------------'

It seems to be two recipes of some sort.
_____________________________________________________
"""

print(LOG_2)


print("It seems to be two recipes of some sort. ")
recipe_Input = input.capitalise("Which should I make? [recipe 1 / recipe 2]: ")
if recipe_Input == "RECIPE 1":
    print("I'll give recipe 1 a go. ")
elif recipe_Input == "RECIPE 2":
    print("Maybe recipe 2 could be right. ")

recipe_1 = [
    {'Aconitum' : "rack"},
    {'Lucanidae' : "drawers"},
    {'Cerambycidae' : "jars"}
]

recipe_2 = [
    {'Asteraceae' : "drawers"},
    {'Nightshade' : "jars"},
    {'Chanterelle' : "rack"}
]

print("I know I have these ingredients somewhere... ")

# def main():
#     options = ["  Inspect rack of vials. ", "  Inspect drawers. ", "  Inspect workbench jars. "]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     print(f"You have selected {options[menu_entry_index]}!")

# if __name__ == "__main__":
#     main()

# print("  Inspect rack of vials. ")
# print("  Inspect drawers. ")
# print("  Inspect workbench jars. ")


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

