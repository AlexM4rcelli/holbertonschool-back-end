#!/usr/bin/python3
"""Prints the completed tasks of an employee on json format"""



import requests, sys , json

users = requests.get(f'https://jsonplaceholder.typicode.com/users')

if users.status_code == 200:
    users_data = users.json()
    for usr in users_data:
        if usr['id'] == int(sys.argv[1]):
            user = usr

user_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user['id']}/todos')

if user_todos.status_code == 200:
    todos_data = user_todos.json()

    with open(f'{user['id']}.json', 'w', encoding='utf-8') as file:
        data = {}
        for task in todos_data:
            new = {}
            new['task'] = task['title']
            new['completed'] = task['completed']
            new['username'] = user['username']
        
            if user['id'] not in data:
                data[user['id']] = []
            data[user['id']].append(new)
        file.write(json.dumps(data))