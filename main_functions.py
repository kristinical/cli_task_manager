from file_functions import *
from edit_functions import *


def menu_selection():
    view_tasks()
    print(menu.center(width))
    action = input(actions)
    return action


def view_tasks():
    print("TO DO LIST:\n".center(width))
    if len(to_do_list) == 0:
        print(no_todo_tasks.center(width))
    else:
        sort_todo_list()
        print_task_list()
    print('\n')


def sort_todo_list():
    to_do_list.sort(key = lambda x: datetime.datetime.strptime(x['Due'], '%m-%d-%Y'))
    

def print_task_list():
    for item in to_do_list:
        task = item['Task']
        due = item['Msg']
        print(f'{task:>30} –– Due {due:<30}'.center(width))

