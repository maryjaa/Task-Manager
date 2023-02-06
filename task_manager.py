#=====importing libraries===========
import datetime
from datetime import date

#=====defining functions===========
#? Function to register a new user (without repeating already existing users)
def reg_user():
    with open('user.txt', 'a+') as f:
        f.seek(0)
        existing_users = f.readlines()
        while True:
            new_user = input('\nRegister a New User\n\nPlease enter the new username: ')
            new_pass = input('Please enter the password for the new username: ')
            confirmation = input('Please enter the new password again: ')
            existing_users = [user.strip().split(',')[0] for user in existing_users]
            if new_user in existing_users:
                print(f'\nSorry, the username {new_user} already exists.')
                continue
            if new_pass != confirmation:
                print('\nThe entered passwords are not the same! Try again.\n')
                continue
            else:
                f.write(f'\n{new_user}, ')
                f.write(new_pass)
                print('\nYou have successfully registered a new user!')
                break
#? Function to add a new task
def add_task():
    with open('tasks.txt', 'a+') as f:
        # Asking the user for all the information about the new task
        whose_task = input('Enter the username of the person whom the task is assigned to:\n')
        title = input('Enter the title of the task:\n')
        description = input('Enter the description of the task:\n')
        due = input('Enter the due date of the task (f. ex. 01 Jan 2000):\n')
        # (Adding the current date in the appropriate format)
        today = date.today()
        todays_date = today.strftime('%d %b %Y')
        
        # Writing in the 'tasks.txt' file the new information
        f.write('\n')
        f.write(f'{whose_task}, {title}, {description}, {due}, {todays_date}, No')
        print('\nYou have successfully added a new task!')
#? Function to view all tasks
def view_all():
    with open('tasks.txt', 'r') as f:
            lines = f.readlines()

            # Putting each task (e.g. each line of 'tasks.txt') as a seperate item in an empty list
            line_lists = []
            for line in lines:
                line_lists.append(line)
            
            # Seperating every detail of each task as a seperate element in a list
            # and printing appropriate indexes of that list to display the info about the task
            for i in line_lists:
                x = i.replace('\n', '')
                oneTask = x.split(', ')
                print(f'\n▭▭▭▭▭▭▭▭▭▭ TASK {line_lists.index(i)+1} ▭▭▭▭▭▭▭▭▭▭\n')
                print(f'Task:                   {oneTask[1]}')
                print(f'Assigned to:            {oneTask[0]}')
                print(f'Date assigned:          {oneTask[3]}')
                print(f'Due date:               {oneTask[4]}')
                print(f'Task complete:          {oneTask[5]}')
                print(f'''Task description:
    {oneTask[2]}''')
#? Function to view logged in user's tasks specifically
def view_mine():
    tasks_read = open('tasks.txt', 'r')
    data = tasks_read.readlines()
    user_tasks = [x for x in data if x.startswith(enterUsername)]

    print('\n▭▭▭▭▭▭▭▭▭▭ YOUR TASKS ▭▭▭▭▭▭▭▭▭▭\n')
    tasks_found = False
    for pos, line in enumerate(user_tasks):
        split_data = line.strip(' ').split(', ')
        tasks_found = True
        print(f'TASK {pos + 1}')
        print(f'Task name:      {split_data[1]}')
        print(f'Description:    {split_data[2]}')
        print(f'Date assigned:  {split_data[3]}')
        print(f'Due date:       {split_data[4]}')
        print(f'Is completed:   {split_data[5]}')
        print('')

    if not tasks_found:
        print('There aren\'t currently any tasks assigned to you!\n')
        
    while True:
        task_num = input("Enter the number of the task you would like to select, or enter -1 to return to the main menu: ")
        if task_num == "-1":
            return 
        elif task_num.isdigit() and int(task_num) <= len(user_tasks) and int(task_num) > 0:
            task_data = user_tasks[int(task_num)-1]
            task_index = data.index(task_data)
            task_split = task_data.strip('\n').split(", ")
            
            # when the task is already marked completed, the user won't be able to edit it further
            if task_split[5] == 'Yes':
                print("\nThis task has already been completed, it cannot be edited anymore.\n")
                continue
            
            # when the task is marked uncompleted, the user gets the choice to edit the task
            elif task_split[5] == 'No':
                task_action = int(input('''\nWhat would you like to do with this task? 

Press 1 - Mark complete
Press 2 - Edit 

Your choice: '''))
                # when user chooses to mark the task complete
                if task_action == 1:
                    with open('tasks.txt', 'w') as f:
                        task_split[5] = "Yes"
                        data[task_index] = ', '.join(task_split)
                        f.write(''.join(data))
                        print("\nThe task has been marked as complete!\n")
                    return
                
                # when user chooses to edit the task, he is offered a new menu to choose from
                elif task_action == 2:
                    while True:
                        task_field = int(input('''\nWhich field of the task would you like to edit? 

Press 1 - Change the assigned username 
Press 2 - Change the due date 
                        
Your choice: '''))
                        # user chooses to change username, so he has to enter a new username to assign the task to
                        if task_field == 1:
                            new_name = input("Enter the new username: ")
                            with open('tasks.txt', 'w') as f:
                                task_split[0] = new_name
                                data[task_index] = ', '.join(task_split)
                                f.write(''.join(data))
                                print("\nThe username for this task has been changed!\n")
                            return

                        # user chooses to change the due date so he has to enter a new due date
                        elif task_field == 2:
                            new_date = input("Enter the new due date (ex. 01 Jan 2000): ")
                            with open('tasks.txt', 'w') as f:
                                task_split[4] = new_date
                                data[task_index] = ', '.join(task_split)
                                f.write(''.join(data))
                                print("\nThe due date for this task has been changed!\n")
                            return

                        else:
                            print("Invalid input. Please enter 1 or 2.")
                else:
                    print("Invalid input. Please enter 1 or 2.")
        else:
            print("Invalid input. Please enter a valid task number or -1 to return to the main menu.")
#? Function that asks the user, after he's done his activity, whether he wants to exit or see the main menu
def what_next():
    final_quest = input('''\nWould you like to go back to the main menu or exit the program?
Press any key for main menu or 'e' to exit The Task Manager: ''').lower()
    if final_quest != 'e':
        return 'continue'
    elif final_quest == 'e':
        print('\nUntil next time!')
        return 'break'
#? Function to generate reports for the user 'admin'
def generate_reports():
    # read tasks from tasks.txt file
    tasks = []
    with open('tasks.txt', 'r') as f:
        for line in f:
            task_info = line.strip('\n').split(', ')
            tasks.append({
                'name': task_info[1],
                'assigned_to': task_info[0],
                'due_date': task_info[4],
                'completed': task_info[5] == 'Yes'
            })

    # read users from user.txt file
    users = {}
    with open('user.txt', 'r') as f:
        for line in f:
            user_info = line.strip().split(', ')
            users[user_info[0]] = user_info[1]

    # tasks overview
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed'] == True])
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = len([task for task in tasks if task['completed'] == False and datetime.datetime.now() > datetime.datetime.strptime(task['due_date'], "%d %b %Y")])
    incomplete_percentage = round((uncompleted_tasks / total_tasks) * 100, 2)
    overdue_percentage = round((overdue_tasks / total_tasks) * 100, 2)

    with open("task_overview.txt", "w") as f:
        f.write(f"Total tasks:              {total_tasks}\n")
        f.write(f"Completed tasks:          {completed_tasks}\n")
        f.write(f"Uncompleted tasks:        {uncompleted_tasks}\n")
        f.write(f"Overdue tasks:            {overdue_tasks}\n")
        f.write(f"Incomplete percentage:    {incomplete_percentage}%\n")
        f.write(f"Overdue percentage:       {overdue_percentage}%\n")

    # users overview
    with open("user_overview.txt", "w") as f:
        f.write(f"Total of users registered:   {len(users)}\n")
        f.write(f"Total of tasks:              {total_tasks}\n")
        for user in users.keys():
            user_tasks = [task for task in tasks if task['assigned_to'] == user]
            user_tasks_count = len(user_tasks)
            if user_tasks_count == 0:
                f.write(f"\nUSER: {user}\n")
                f.write(f"Total tasks assigned:                 {user_tasks_count}\n")
                f.write("Percentage of total tasks assigned:   0%\n")
                f.write("Percentage of tasks completed:        0%\n")
                f.write("Percentage of tasks uncompleted:      0%\n")
                f.write("Percentage of tasks overdue:          0%\n")
            else:
                user_tasks_percentage = round((user_tasks_count / total_tasks) * 100, 2)
                completed_user_tasks_count = len([task for task in user_tasks if task['completed'] == True])
                completed_user_tasks_percentage = round((completed_user_tasks_count / user_tasks_count) * 100, 2)
                uncompleted_user_tasks_count = user_tasks_count - completed_user_tasks_count
                uncompleted_user_tasks_percentage = round((uncompleted_user_tasks_count / user_tasks_count) * 100, 2)
                overdue_user_tasks_count = len([task for task in user_tasks if task['completed'] == False and datetime.datetime.now() > datetime.datetime.strptime(task['due_date'], "%d %b %Y")])
                overdue_user_tasks_percentage = round((overdue_user_tasks_count / user_tasks_count) * 100, 2)

                f.write(f"\nUSER: {user}\n")
                f.write(f"Total tasks assigned:                 {user_tasks_count}\n")
                f.write(f"Percentage of total tasks assigned:   {user_tasks_percentage}%\n")
                f.write(f"Percentage of tasks completed:        {completed_user_tasks_percentage}%\n")
                f.write(f"Percentage of tasks uncompleted:      {uncompleted_user_tasks_percentage}%\n")
                f.write(f"Percentage of tasks overdue:          {overdue_user_tasks_percentage}%\n")
#? Function to display (or generate from 'generate_reports()' if not found) statistics
def display_statistics():
    print('\n═══════════════STATISTICS═══════════════════\n')
    try:
        with open('task_overview.txt', 'r') as f:
            print('══════════════Task Overview═════════════════\n')
            for line in f:
                print(line.strip('\n'))
    except FileNotFoundError:
        print('task_overview.txt not found. Generating the report...\n')
        generate_reports()
        with open('task_overview.txt', 'r') as f:
            print('\nTask Overview:\n')
            for line in f:
                print(line.strip('\n'))
    
    try:
        with open('user_overview.txt', 'r') as f:
            print('\n══════════════User Overview═════════════════\n')
            for line in f:
                print(line.strip('\n'))
    except FileNotFoundError:
        print('user_overview.txt not found. Generating the report...')
        generate_reports()
        with open('user_overview.txt', 'r') as f:
            print('\nUser Overview:\n')
            for line in f:
                print(line.strip('\n'))

#!====Login Section====

# Welcome message
print('''════════════════ HELLO! ════════════════
Welcome to The Task Manager!

Here you can register a new user, add a task or view existing tasks.

In order to access The Task Manager, please enter the correct username and password.
''')

details = open('user.txt', 'r')
details_dict = {}

for detail in details:
    k, v = detail.split(', ')
    details_dict[k] = v.strip('\n')

while True:
    enterUsername = input('Enter the username: ')
    enterPassword = input('\nEnter the password: ')

    correct_pass = details_dict.get(enterUsername)

    if correct_pass == enterPassword:
        print(f'\nWelcome, {enterUsername}! You\'re in!')
        break

    print('\nIncorrect details, please try again.\n')

#!==== The Task Manager opens when the user enters a correct username and a correct accompanying password: 

while True:
    # When the username entered in the login section is 'admin', the menu shown is extended to two additional options:
    # registering a new user and displaying statistics
    if enterUsername == 'admin':
        menu = input('''\n═════════════════ MENU ════════════════════

Please select one of the following options:

☑ r  ▹ register an user
☑ a  ▹ add a task
☑ va ▹ view all tasks
☑ vm ▹ view my tasks
☑ gr ▹ generate reports
☑ s  ▹ see statistics
☑ e  ▹ exit

Your choice: ''').lower()
    
    # For all other users, the menu shown is restricted
    else:
       menu = input('''\n═════════════════ MENU ════════════════════

Please select one of the following options:

☑ a  ▹ add a task
☑ va ▹ view all tasks
☑ vm ▹ view my tasks
☑ e  ▹ exit

Your choice: ''').lower() 

    #!==== When the user admin chooses to register a new username (r):
    if menu == 'r':
        if enterUsername == 'admin':
            # Calling the function to register a new user (without repetitions)
            reg_user()
            
            # Calling the function 'what_next' to determine whether the user wants to exit the program or
            # view the main menu
            final_choice = what_next()
            if final_choice == 'continue':
                continue
            elif final_choice == 'break':
                break

    #!==== When the user chooses to add a new task (a):
    elif menu == 'a':
        # Calling the function to add a new task
        add_task()

        final_choice = what_next()
        if final_choice == 'continue':
            continue
        elif final_choice == 'break':
            break

    #!==== When the user chooses to view all tasks (va):
    elif menu == 'va':
        # Calling the function to view all tasks
        view_all()
        
        final_choice = what_next()
        if final_choice == 'continue':
            continue
        elif final_choice == 'break':
            break
        
    #!==== When the user chooses to only view tasks assigned to them (vm):
    elif menu == 'vm':
        # Calling the function to view the logged in user's tasks only
        view_mine()

        final_choice = what_next()
        if final_choice == 'continue':
            continue
        elif final_choice == 'break':
            break

    #!==== When the user 'admin' chooses to generate reports (gr):
    elif menu == 'gr':
        if enterUsername == 'admin':
            generate_reports()
            print('\nYour reports have been generated succesfully.')

            final_choice = what_next()
            if final_choice == 'continue':
                continue
            elif final_choice == 'break':
                break
        else:
            print("\nSorry, this option does not exist, try again.")
            continue

    #!==== When the user 'admin' chooses to display the statistics (s):
    elif menu == 's':
        if enterUsername == 'admin':
            display_statistics()
            
            final_choice = what_next()
            if final_choice == 'continue':
                continue
            elif final_choice == 'break':
                break 

        else:
            print("\nSorry, this option does not exist, try again.")
            continue

    #!==== When the user chooses to exit the program (e):
    elif menu == 'e':
        print('\nUntil next time!')
        break

    #!==== When the user enters any other option that's not in the menu:
    else:
        print("\nSorry, this option does not exist, try again.")
        continue