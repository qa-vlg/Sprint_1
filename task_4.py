new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(new_tasks.index('task_005'))) # moving 'task_005' to completed_tasks

new_tasks.remove('task_007') # removing 'task_007' from the list

print(new_tasks[-1]) # printing last task in the list