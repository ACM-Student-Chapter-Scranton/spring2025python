# task = {
#     'name': 'temp',
#     'desc': 'example',
#     'priority': 3,
#     'is_done': False
# }

def create_task(name, desc, priority, is_done):
    return {
        'name': name,
        'desc': desc,
        'priority': priority,
        'is_done': is_done
    }

task = create_task('temp', 'example', 3, False)

print(task['name'])
print(task['desc'])
print(task['priority'])
print(task['is_done'])