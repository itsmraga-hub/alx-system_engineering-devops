#!/usr/bin/python3
"""
    Write a Python script that, using this REST API, for a given
    employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    u_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, u_id)).json()

    user_todos = requests.get(url + "todos", params={"userId": u_id}).json()

    todos = {
                u_id: []
            }
    for todo in user_todos:
        title = todo.get("title")
        username = user.get("name")
        completed = todo.get("completed")
        obj = {"task": title, "completed": completed, "username": username}
        todos[u_id].append(obj)

    todos_json = json.dumps(todos)
    file = '{}.json'.format(u_id)
    with open(file, 'w') as f:
        f.write(todos_json)
