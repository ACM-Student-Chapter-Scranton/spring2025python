import csv
from task import Task

first = Task('First Task', 'This is the first task I am creating as a part of this program', 1, False)
second = Task('Second Task', 'A second task to complete after my first one.', 1, False)
third = Task('Third Task', 'This task has a higher priority than the other two', 3, False)
fourth = Task('Fourth Task', 'This task has already been completed because it\'s priority was so high', 10, True)

tasks =[first, second, third, fourth]

for task in tasks:
    print(task.name)

new_task = Task('New Task', 'Added using a Python program that opens files', 2, False)

with open('saved_tasks.txt', 'a') as file:
    entry = f'{new_task.name},{new_task.desc},{new_task.priority},{new_task.is_done}\n'
    file.write(entry)

with open('saved_tasks.csv', 'a') as csvfile:
    fieldnames = ['name', 'desc', 'priority', 'is_done']
    fieldvalues = [new_task.name, new_task.desc, new_task.priority, new_task.is_done]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    entry = dict(zip(fieldnames, fieldvalues))
    writer.writerow(entry)