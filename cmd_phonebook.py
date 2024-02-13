import os
import sys
from prompt_toolkit import prompt
from phonebook import Contact, Phonebook

def clear_screen():
    """Clears the screen depending on the operating system."""
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def main():
    """Displays the main menu and calls the corresponding functions."""
    clear_screen()
    my_phonebook.selected_contact = None
    print(my_phonebook)
    length = my_phonebook.length
    for i, menu_item in enumerate(main_menu.keys()):
        option = f'[{i + 1}] {menu_item}'
        if length == 0 and menu_item == 'Select':
            option += ' (Inactive)'
        print(option)
    item = ''
    while not item.isdigit() or int(item) < 1 or int(item) > len(main_menu):
        item = input('Please enter the number of one of the options:')
    item = int(item)- 1
    menu_key = list(main_menu.keys())[item]
    if length == 0 and menu_key == 'Select':
        function = main
    else:
        function = main_menu[menu_key]
    function()
    main()

def exit_phonebook():
    """Exits the program."""
    sys.exit()

def reset_select():
    """Resets the selected contact and calls the select function."""
    my_phonebook.selected_contact = None
    select()

def select():
    """Displays the list of contacts and allows the user to select one."""
    clear_screen()
    if my_phonebook.selected_contact is None:
        print(my_phonebook.select_str()) 
        num = ''
        while not num.isdigit()or int(num) < 1 or int(num) > my_phonebook.length:
            num = input('Please enter the number of one of the contacts:')
        num = int(num) - 1
        my_phonebook.selected_contact = num
        select()
    else:
        print(my_phonebook.active_contact().details())
        for i, menu_item in enumerate(select_menu.keys()):
            print(f'[{i + 1}] {menu_item}')
        item = ''
        while not item.isdigit() or int(item) < 1 or int(item) > len(select_menu):
            item = input('Please enter the number of one of the options:')
        item = int(item)- 1
        menu_key = list(select_menu.keys())[item]
        function = select_menu[menu_key]
        function()

def new():
    """Creates a new contact and adds it to the phonebook."""
    clear_screen()
    print('Create a new contact:')
    c = Contact()
    attrs = vars(c)
    for attr in attrs.keys():
        inp = input(f"Enter {attr.replace('_', ' ')}:")
        if inp != '':
            attrs[attr] = inp
    inp = input(
        f'''Confirm the following information to be saved:
                {c.details()}
        Enter "s" key to save and any other key to discard:'''
    )
    if inp.lower() == 's':
        my_phonebook.add(c)
        my_phonebook.save()
        print('Contact saved.')

def edit():
    """Edits the selected contact and saves the changes."""
    old_c = my_phonebook.active_contact()
    old_attrs = vars(old_c)
    c = Contact()
    attrs = vars(c)
    for attr in attrs.keys():
        inp = prompt(f"Enter {attr.replace('_', ' ')}:", default=old_attrs[attr] if old_attrs[attr] else '')
        if inp == '':
            attrs[attr] = None
        else:
            attrs[attr] = inp
    inp = input(
        f'''The contact was edited as follows, please confirm to save it:
                {c.details()}
        Enter "s" key to save and any other key to discard:'''    )
    if inp.lower() == 's':
        my_phonebook.edit(c)
        my_phonebook.save()
        print('The edited contact has been saved.')
    main()


def delete():
    """Deletes the selected contact from the phonebook."""
    c = my_phonebook.active_contact()
    inp = input(
        f'''Do you want to delete the following contact:
                {c.details()}
        Enter "d" key to delete and any other key to cancel:'''
    )
    if inp.lower() == 'd':
        my_phonebook.delete()
        my_phonebook.save()
        print('Contact deleted.')
        my_phonebook.selected_contact = None
        main()
    else:
        reset_select()

def find():
    """Finds contacts that match the search term."""
    clear_screen()
    print(my_phonebook)
    inp = input('Enter the search term:')
    if inp == '':
        return
    clear_screen()
    found_contacts = my_phonebook.find(inp)
    if len(found_contacts) == 0:
        input('No results were found!')
        return
    for i, c in enumerate(found_contacts):
        print(f'[{i + 1}] {c[1].__str__()}')
    inp = ''
    while not inp.isdigit() or int(inp) < 1 or int(inp) > len(found_contacts):
        inp = input('Please enter the number of one of the contacts or press the enter key to return to the menu :')
        if inp == '' :
            return
    item_number = found_contacts[int(inp) - 1][0]
    my_phonebook.selected_contact = item_number
    select()

if __name__ == '__main__':
    main_menu = {'Select': select, 'Find': find, 'New': new, 'Exit': exit_phonebook}
    select_menu = {'Reselect': reset_select, 'Edit': edit, 'Delete': delete, 'Back': main}
    my_phonebook = Phonebook()
    main()
