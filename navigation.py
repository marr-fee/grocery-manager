import menu
import os

menu_stack = [menu.menu_options]

def navigate(stack):
    """ 
    MAIN NAVIGATION FUNCTION 
    Handles the current state of the menu system using a stack. 
    Displays available options from the current menu and manages user navigation depth. 
    """
    current_menu = stack[-1]
    if isinstance(current_menu, dict):
        title = current_menu["title"]
        options = current_menu['options']
        run_selected_option(options, title)
        return_menu_display(len(stack))


def run_selected_option(options, title):
    """ 
    Displays or executes the selected menu option. 
    If 'options' is a dictionary, it prints all available choices. 
    If it's a callable or parameterized function, delegates to handle_func_parameters(). 
    """
    os.system('cls')
    print(f"{'-' * 50}")
    print(f"{title.upper()}")
    print(f"{'-' * 50}")
    if isinstance(options, dict):
        for key, val in options.items():
            print(f"{key}) {val['title'] if isinstance(val, dict) else val}")
    else:
        handle_func_parameters(options)


def return_menu_display(length):
    """ 
    Displays navigation options like 'Previous Menu' or 'Main Menu' 
    depending on how deep the user is in the menu hierarchy. 
    """
    if length == 2 or length > 2:
        print("R) Previous Menu")
    if length > 2:
        print("M) Main Menu")
    print()


def go_back():
    """ 
    Goes back one level in the menu stack and redisplays the previous menu. 
    """
    menu_stack.pop()
    navigate(menu_stack)


def handle_func_parameters(option):
    """ 
    Handles execution of a function option with or without parameters. 
    If the option is a tuple, it unpacks arguments and calls the function. 
    If the option is a direct callable, it executes it immediately. 
    """
    if isinstance(option, tuple):
        func = option[0]
        args = option[1:]
        func(*args)
    elif callable(option):
        option()
