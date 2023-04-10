#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import csv
import json
import urllib.request


url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """ This function gets data from the placeholders API """
    with urllib.request.urlopen(url_user) as f:
        employee_data = json.loads(f.read().decode())

    all_data = {}
    for employee in employee_data:
        with urllib.request.urlopen(url_user + str(employee["id"]) + "/todos/") as f:
            todo_data = json.loads(f.read().decode())

        """ Calculate number of completed tasks and total number of tasks """
        number_of_done_task = sum(1 for todo in todo_data if todo["completed"])
        total_number_of_tasks = len(todo_data)
        employee_name = employee["name"]
        user_id = employee["id"]
        username = employee["username"]
        
        for todo in todo_data:
            task_completed_status = todo["completed"]
            task_title = todo["title"]

        """ Export data to JSON format """
        data = {user_id: [{"username": username, "task": task_title, "completed": task_completed_status} for todo in todo_data]}
        all_data.update(data)
        with open("todo_all_employees.json", mode="w") as f:
            json.dump(all_data, f)

if __name__ == "__main__":
    get_func()
