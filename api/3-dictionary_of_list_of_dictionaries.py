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
            dat = json.loads(f.read().decode())

        """ Calculate number of completed tasks and total number of tasks """
        number_of_done_task = sum(1 for t in dat if t["completed"])
        total_number_of_tasks = len(dat)
        employee_name = emp["name"]
        user_id = emp["id"]
        username = emp["username"]

        for t in dat:
            task_completed_status = t["completed"]
            task_title = t["title"]

        """ Export data to JSON format """
        data = {user_id: [{"username": username, "task": task_title,
                           "completed": task_completed_status} for t in dat]}
        all_data.update(data)
        with open("todo_all_employees.json", mode="w") as f:
            json.dump(all_data, f)

if __name__ == "__main__":
    get_func()

