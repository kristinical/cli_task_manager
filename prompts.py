from add_functions import width

# set indentation
tabs = '\t' * 3 #+ ' ' * 4

welcome_message = "WELCOME TO YOUR TASK MANAGER!\n"

no_todo_tasks = "You currently have no tasks to do."

no_completed_tasks = "You have no completed tasks."

delete_header = "DELETE A TASK\n".center(width)

delete_prompt = "\tWhat task do you want to delete? "

edit_header = "EDIT A TASK\n".center(width)

edit_prompt = "\tWhat task do you want to edit? "

complete_header = "COMPLETE A TASK\n".center(width)

complete_prompt = "\tWhat task have you completed? "

menu = "WHAT WOULD YOU LIKE TO DO?"

actions = tabs + "1. Create new task\n" \
    + tabs + "2. Edit a task\n" \
    + tabs + "3. Delete a task\n" \
    + tabs + "4. Mark task as complete\n" \
    + tabs + "5. View completed tasks\n" \
    + tabs + "6. Exit\n" \
    + "\n"

edit_actions = "\tWhat would you like to do?\n" \
    + "\t  1. Edit a task name\n" \
    + "\t  2. Edit a due date\n" \
    + "\t  3. Cancel\n" \
    + "\n"

tasks_saved = "Your tasks have been saved!".center(width)
goodbye = "Exiting program\n\n".center(width)
