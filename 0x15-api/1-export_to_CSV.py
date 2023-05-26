#!/usr/bin/python3
"""
    Write a Python script that, using this REST API, for a given
    employee ID, returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    u_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, u_id)).json()

    user_todos = requests.get("{}todos?userId={}".format(url, u_id)).json()

    file = '{}.csv'.format(u_id)
    with open(file, 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in user_todos:
            name = user.get("username")
            title = task.get("title")
            completed = task.get("completed")
            writer.writerow([int(u_id), name, completed, title])
