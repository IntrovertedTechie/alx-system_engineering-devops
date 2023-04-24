#!/usr/bin/python3
"""
Gather data from an API and export TODO list progress for a given employee ID in CSV format
"""

import requests
import csv
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

            csv_file = "{}.csv".format(user_id)
            with open(csv_file, mode='w') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['user_id', 'username', 'task_completed_status', 'task_title'])
                for task in todo_data:
                    writer.writerow([user_id, user_data['username'], task['completed'], task['title']])
        except ValueError:
            print("Error: Invalid JSON format")
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")

