#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import csv
import json
import urllib.request


url = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """ This function gets data from the placeholders API """
    with urllib.request.urlopen(url) as f:
        employee_data = json.loads(f.read().decode())

    all_data = {}
    for emp in employee_data:
        with urllib.request.urlopen(url + str(emp["id"]) + "/todos/") as f:
            t_data = json.loads(f.read().decode())

        """ Calculate number of completed tasks and total number of tasks """
        number_of_done_task = sum(1 for todo in t_data if todo["completed"])
        total_number_of_tasks = len(t_data)
        employee_name = emp["name"]
        user_id = emp["id"]
        username = emp["username"]

        for todo in t_data:
            task_completed_status = todo["completed"]
            task_title = todo["title"]

        """ Export data to JSON format """
        data = {user_id: [{"username": username, "task": task_title,
                           "completed": task_completed_status}
                           for todo in t_data]}
        all_data.update(data)
        with open("todo_all_employees.json", mode="w") as f:
            json.dump(all_data, f)

if __name__ == "__main__":
    get_func()
