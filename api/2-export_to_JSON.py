#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import csv
import json
import sys
import urllib.request


url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """ This function gets data from the placeholders API """
    with urllib.request.urlopen(url_user + sys.argv[1]) as f:
        employee = json.loads(f.read().decode())
    with urllib.request.urlopen(url_user + sys.argv[1] + "/todos/") as f:
        todo_data = json.loads(f.read().decode())

    """ Calculate number of completed tasks and total number of tasks """
    number_of_done_task = sum(1 for todo in todo_data if todo["completed"])
    total_number_of_tasks = len(todo_data)
    employee_name = employee["name"]
    user_id = employee["id"]
    username = employee["username"]

    """ Export data to CSV format """
    data = []
    for todo in todo_data:
        task_title = todo["title"]
        task_completed_status = "True" if todo["completed"] else "False"
        data.append([user_id, username, task_completed_status, task_title])
    with open("{}.csv", mode="w" .format(user_id)) as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)

    """ Export data to JSON format """
    data = {user_id: [{"task": task_title, "completed": task_completed_status, "username": username} for todo in todo_data]}
    with open("{}.json".format(user_id), mode="w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    get_func()
