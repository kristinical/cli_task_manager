from add_functions import *
from delete_functions import *
   

def print_edit_header():
    system('clear')
    print(edit_header)

def edit_task():
    if no_tasks(): return
    print_edit_header()
    edit_choice = edit_option()
    if edit_choice == "3":
        system('clear')
        print("EDIT ACTION CANCELLED\n".center(width))
    else:
        complete_edit(edit_choice)
        system('clear')
        print("TASK EDITED!\n".center(width))


def edit_option():
    option = input(edit_actions)
    while option < "1" or option > "3":
        print_edit_header()
        print("\tInvalid selection\n")
        option = input(edit_actions)
    return option


def complete_edit(choice):
    system('clear')
    print(edit_header)
    list_valid_tasks()
    task_item = validate_task(edit_prompt, edit_header)
    # validate_task returns (name, index) tuple
    if choice == "1":
        edit_name(task_item[1])
    elif choice == "2":
        edit_date(task_item[1])


def edit_name(task_index):
    new_name = get_task_name("\tUpdated task name: ")
    to_do_list[task_index]['Task'] = new_name


def edit_date(task_index):
    print(f"\n\tCurrent due date: {to_do_list[task_index]['Due']}")
    new_date = get_due_date("\tUpdated due date (MM-DD-YYYY): ")
    to_do_list[task_index]['Due'] = new_date
    to_do_list[task_index]['Msg'] = get_message(new_date)
