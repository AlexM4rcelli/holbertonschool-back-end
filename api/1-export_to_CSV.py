#!/usr/bin/python3
"""Prints the completed tasks of an employee on csv Format"""



import requests, sys , csv

users = requests.get(f'https://jsonplaceholder.typicode.com/users')

if users.status_code == 200:
    users_data = users.json()
    for usr in users_data:
        if usr['id'] == int(sys.argv[1]):
            user = usr

user_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user['id']}/todos')

if user_todos.status_code == 200:
    todos_data = user_todos.json()
    with open(f'{sys.argv[1]}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([str(user['id']), user['username'], str(task['completed']), task['title']])