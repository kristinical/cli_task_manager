import datetime
from os import system
from file_functions import *

# set width of console
width = 65


def add_task():
    system('clear')
    print("ADD A TASK\n".center(width))
    name = get_task_name("New task name (enter -1 to cancel): ")
    if name != "-1":
        insert_new_task(name)
    else:
        system('clear')
        print("CREATE TASK CANCELLED\n".center(width))
    

def insert_new_task(name):
    due_date = get_due_date("Due date (MM-DD-YYYY): ")
    message = get_message(due_date)
    to_do_list.append({'Task':name, 'Due':due_date, 'Msg':message})
    system('clear')
    print("TASK ADDED!\n".center(width))


def get_task_name(prompt):
    name = input(prompt)
    while not valid_name(name.capitalize()) or name == "":
        if name == "":
            print("\nName cannot be blank")
        else:
            print("\nTask name already exists.")
        name = input(prompt)
    return name.capitalize()
    
    
def valid_name(new_name):
    for task in to_do_list:
        name = task['Task']
        if new_name == name:
            return False
    return True


def get_due_date(prompt):
    date = input(prompt)
    while not valid_date(date):
        print("\nInvalid format.")
        date = input(prompt)
    return date


def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%m-%d-%Y")
        return True
    except ValueError:
        return False