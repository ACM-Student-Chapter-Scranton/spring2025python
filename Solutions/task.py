import csv
import datetime

class Task:
    def __init__(self, name, desc, priority, deadline=datetime.datetime.max):
        self.name = name
        self.desc = desc
        self.priority = priority
        self.is_done = False
        self.time_created = datetime.datetime.now()
        self.deadline = deadline
    
    def __repr__(self):
        return f'''{self.name}: Priority ({self.priority})\n{self.desc}\nDeadline: {self.deadline}\nCompleted: {self.is_done}'''
    
    def toggle_complete(self):
        self.is_done = not self.is_done

    def save_task(self, filename='saved_tasks.csv'):
        with open(filename, "r+") as file:
            rows = csv.reader(file)
            fieldnames = next(rows)
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            data = [self.name, self.desc, self.priority, self.deadline, self.is_done]
            entry = dict(zip(fieldnames, data))
            writer.writerow(entry)