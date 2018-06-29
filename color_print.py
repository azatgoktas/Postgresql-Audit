import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True) # bring color back when print func finished


def print_red(str):
    print(Fore.RED + str )

def print_green(str):
    print(Fore.GREEN + str)
