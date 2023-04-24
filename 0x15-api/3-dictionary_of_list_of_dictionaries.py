#!/usr/bin/python3
"""Extend Python script to export data in JSON format."""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + '/users').json()

    todo_all_employees = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = requests.get(url + '/todos?userId={}'.format(user_id)).json()

        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            })

        todo_all_employees[user_id] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all_employees, f)
