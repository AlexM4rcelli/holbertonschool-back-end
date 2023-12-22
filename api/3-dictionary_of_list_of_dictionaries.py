#!/usr/bin/python3
"""Prints the completed tasks of all employee on json format"""



import requests, json

if __name__ == '__main__':
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')

    if users.status_code == 200:
        users_data = users.json()

    data = {}
    for user in users_data:
        user_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user['id']}/todos')

        if user_todos.status_code == 200:
            todos_data = user_todos.json()
            for task in todos_data:
                new = {}
                new['username'] = user['username']
                new['task'] = task['title']
                new['completed'] = task['completed']
            
                if user['id'] not in data:
                    data[user['id']] = []
                data[user['id']].append(new)

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
