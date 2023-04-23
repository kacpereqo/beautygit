import msvcrt as m
import os

from rich import print


def press_to_continue(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("\n[bold]Press any key to continue...[/]")
        m.getch()
    return wrapper


def clear_screen(func):
    def wrapper(*args, **kwargs):
        os.system("cls")
        func(*args, **kwargs)
    return wrapper
