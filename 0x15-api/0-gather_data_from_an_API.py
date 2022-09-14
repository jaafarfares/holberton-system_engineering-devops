#!/usr/bin/python3
""" REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    name = requests.get("https://jsonplaceholder.typicode.com/users/" + id)
    data = todo.json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in tasks))
