#!/usr/bin/python3
"""
    Gather data from an API and display TODO list progress for a given employee ID
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        user_res = requests.get(base_url + "/users/{}".format(user_id))
        todo_res = requests.get(base_url + "/todos?userId={}".format(user_id))

        try:
            user_data = user_res.json()
            todo_data = todo_res.json()

            total_tasks = len(todo_data)
            completed_tasks = len([task for task in todo_data if task.get("completed")])

            print("Employee {} is done with tasks({}/{}):".format(user_data.get("name"),
                                                                    completed_tasks,
                                                                    total_tasks))

            for task in todo_data:
                if task.get("completed"):
                    print("\t {}".format(task.get("title")))
        except ValueError:
            print("Error: Invalid JSON format")
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
