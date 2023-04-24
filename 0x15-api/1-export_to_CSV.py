#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json().get('username')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    with open(user_id + ".csv", mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user_name, task.get('completed'),
                             task.get('title')])
