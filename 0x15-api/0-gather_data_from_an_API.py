#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    done_tasks = [task for task in todo if task.get('completed') is True]
    total_tasks = len(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print('\t', task.get('title'))
