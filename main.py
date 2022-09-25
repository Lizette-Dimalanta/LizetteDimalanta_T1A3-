# from prettytable import PrettyTable
# x = PrettyTable()

LOG_1 = """
------------------------------------------------
I woke up at my desk. I remember being awake all night but my memory is foggy. 
The room smells of smoke, it seems like something happened here.
...
It's dark, the light switch doesn't seem to turn on.
There is a matchbox in my pocket with a single match left.
------------------------------------------------
"""

print(LOG_1)

USE_MATCH_1 = """

Used match.
(Inventory: match -1)
"""

USE_MATCH_2 = """

I light the match. I see a candle - I'll light it on that.
"""

match_input = input("Should I use the match? [yes (-1 match) / no]: ")
if match_input == "yes":
    print(USE_MATCH_1)
    x.field_names = ["Item", "Quantity"]
    x.add_row(["Match", 0])
    print(x)
    print(USE_MATCH_2)
elif match_input == "no":
    print("I search the shelf for a torch. CLICK! It's bright! ")
else:
    print("Hmm..")

print("      ------------------------------------------------ ")
print("I could barely see past this fog, but something definitely happened here. This room is a mess. ")
print(" ")
print("Is this my handwriting? ")
print(" .----------------.   .----------------.")
print("| .--------------. | | .--------------. |")
print("| |   RECIPE 1   | | | |   RECIPE 2   | |")
print("| |              | | | |              | |")
print("| |   Aconitum   | | | |  Asteraceae  | |")
print("| |   Lucanidae  | | | |  Nightshade  | |")
print("| | Cerambycidae | | | | Chanterelle  | |")
print("| |              | | | |              | |")
print("| '--------------' | | '--------------' |")
print("  '----------------'  '----------------'")

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
-------------
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

