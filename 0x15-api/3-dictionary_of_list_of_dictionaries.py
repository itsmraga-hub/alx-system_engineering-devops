#!/usr/bin/python3
"""
    Write a Python script that, using this REST API, for a given
    employee ID, returns information about his/her TODO list progress.
"""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get("{}users".format(url)).json()

    todos = requests.get(url + "todos").json()

    todos_all = {}

    for user in users:
        user_id = user.get('id')
        username = user.get("username")
        user_todos = []

        for todo in todos:
            todo_user_id = todo.get('userId')
            title = todo.get("title")
            completed = todo.get("completed")
            obj = {"username": username, "task": title, "completed": completed}
            if user_id == todo_user_id:
                user_todos.append(obj)

        todos_all[user_id] = user_todos


    todos_json = json.dumps(todos_all)
    file = 'todo_all_employees.json'
    with open(file, 'w') as f:
        f.write(todos_json)
