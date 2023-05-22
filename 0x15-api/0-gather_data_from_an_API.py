#!/usr/bin/python3
"""
    Write a Python script that, using this REST API, for a given
    employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    u_id = sys.argv[1]
    user = requests.get("{}users/{}".format(url, u_id)).json()

    user_todos = requests.get("{}users/{}/todos".format(url, u_id)).json()

    completed_tasks = []

    for todo in user_todos:
        if todo.get("completed") == True:
            completed_tasks.append(todo)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(user_todos)
        ))
    for task in completed_tasks:
        print("\t", task.get("title"))
