import menu
import navigation as nav
import programData as dta


def main():
    dta.load_data()
    nav.navigate(nav.menu_stack)

    while True:    
        # try:
            current_menu = nav.menu_stack[-1]
            menu_choice = input("Enter option: ").lower()
            if menu_choice == 'r':
                nav.go_back()
            elif menu_choice == 'm':
                nav.menu_stack = [menu.menu_options]
            elif menu_choice == 'x':
                break
            else: 
                nav.menu_stack.append(current_menu['options'][menu_choice])

            nav.navigate(nav.menu_stack)
        # except:
        #     print("Invalid input")
    
    dta.dump_data()
          


if __name__ == '__main__': main()