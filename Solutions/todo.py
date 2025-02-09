import csv
import pandas
import datetime

from task import Task

def create_task():
    name = input("Task Name: ")
    desc = input("Task Desc: ")
    priority = input("Task Priority: ")

    deadline_choice = input('Set Deadline [y/n]? ')
    date = None

    if deadline_choice == 'y':
        year = int(input('Year: '))
        month = int(input('Month: '))
        day = int(input('Day: '))
        date = datetime.datetime(year, month, day)

    if date:
        new_task = Task(name, desc, priority, date)
    else:
        new_task = Task(name, desc, priority)

    print("Creation Success!")
    print(new_task)

    save_task = input("Save Task [y/n]?")

    if save_task == 'y':
        new_task.save_task()
        print("Saved!")

def list_tasks(select=None):
    with open('saved_tasks.csv', 'r') as file:
        file.seek(0)
        rows = csv.reader(file)
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        print("Tasks")
        print('--------------------------------')

        for line_no, line in enumerate(rows, start=1):

            if indices:
                line = [ line[index] for index in indices ]

            print(line_no, line)
            print('--------------------------------')

def modify_tasks():
    list_tasks(select=['name', 'is_done'])
    choice = int(input('Choose Task to Modify: ')) - 1

    df = pandas.read_csv('saved_tasks.csv')
    df.loc[choice, 'is_done'] = not df.loc[choice, 'is_done']
    df.to_csv('saved_tasks.csv', index=False)    

def main():
    print('Hello, User!')
    choice = ''
    while choice != '0':
        print('Main Menu (type number)')
        print('0. Exit')
        print('1. Create New Task')
        print('2. Show Saved Tasks')
        print('3. Modify Task Status')
        choice = input('>>>>> ')
        if choice == '1':
            create_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            modify_tasks()
        elif choice != '0':
            print('Invalid choice, please type a single digit.')

    print('Goodbye!')

if __name__ == '__main__':
    main()