#!/usr/bin/python3
"""Prints the completed tasks of an employee"""


import requests
import sys

users = requests.get(f'https://jsonplaceholder.typicode.com/users')

if users.status_code == 200:
    users_data = users.json()
    for usr in users_data:
        if usr['id'] == int(sys.argv[1]):
            user = usr

user_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user['id']}/todos')

if user_todos.status_code == 200:
    todos_data = user_todos.json()
    tasks_done = [task for task in todos_data if task['completed']]
    print(f"Employee {user['name']} is done with tasks({len(tasks_done)}/{len(todos_data)})")
    for task in tasks_done:
        print('\t ' + task['title'])
