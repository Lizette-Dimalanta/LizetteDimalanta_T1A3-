import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

def log_1():
    """Introduction Log"""
    print(f"{Fore.LIGHTBLACK_EX}____________________________________________________________________")
    print(f"{Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX}\nI woke up at my desk. I remember being awake all night but my memory is foggy.")
    print(f"{Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX}The room smells of smoke, it seems like something happened here.                ")
    print(f"{Back.LIGHTBLACK_EX} ...  ")
    print(f"{Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX}It's dark, the light switch doesn't seem to turn on.      ")
    print(f"{Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX}There is a matchbox in my pocket with a single match left.")
    print(f"{Fore.LIGHTBLACK_EX}\n____________________________________________________________________")

log_1()