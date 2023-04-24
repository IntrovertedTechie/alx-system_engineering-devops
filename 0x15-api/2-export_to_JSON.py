#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()

    task_list = []
    for task in tasks:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": user.get("username")}
        task_list.append(task_dict)
    task_dict = {user_id: task_list}

    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(task_dict, jsonfile)
