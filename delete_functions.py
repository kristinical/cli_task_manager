from os import system
from prompts import *
from main_functions import to_do_list
from add_functions import width


def delete_task():
    if no_tasks(): return
    system('clear')
    print(delete_header)
    list_valid_tasks()
    delete_item = validate_task(delete_prompt, delete_header)
    confirm = confirm_deletion(delete_item[0])
    process_deletion(confirm, delete_item[1])


def process_deletion(confirm, index):
    system('clear')
    if confirm == "y":
        del to_do_list[index]
        print("TASK DELETED!\n".center(width))
    else:
        print("DELETE ACTION CANCELLED\n".center(width))


def no_tasks():
    if len(to_do_list) == 0:
        system('clear')
        return True


def validate_task(prompt, header):
    name = input(prompt)
    task_index = valid_task(name.capitalize())
    while task_index == -1:
        system('clear')
        print(header)
        print("\tTask does not exist.\n")
        list_valid_tasks()
        name = input(prompt)
        task_index = valid_task(name.capitalize())
    return name.capitalize(), task_index


def valid_task(name):
    for i in range(len(to_do_list)):
        if to_do_list[i]["Task"] == name:
            return i
    return -1


def list_valid_tasks():
    """
    Displays list of current tasks on To-Do List in alphabetical order
    """
    print("\tCurrent tasks:")
    to_do_list.sort(key = lambda x: x['Task'])
    for task in to_do_list:
        print("\t  " + task['Task'])
    print()


def confirm_deletion(task):
    delete = input(f'\tAre you sure you want to delete "{task}"? (y/n) ')
    while delete != "y" and delete != "n":
        print("\n\tPlease press 'y' for yes or 'n' for no.")
        delete = input(f'\tAre you sure you want to delete "{task}"? ')
    return delete
