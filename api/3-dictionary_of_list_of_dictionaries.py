#!/usr/bin/python3
"""
    Using a REST API, retrieves information about list progress
    for all employees and exports data in CSV and JSON formats
"""

import json
import requests

url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """Get data from the placeholders API and export to CSV and JSON formats"""
    employee_data = requests.get(url_user).json()

    all_data = {}
    for emp in employee_data:
        with requests.get(url_user + str(emp["id"]) + "/todos/") as f:
            dat = f.json()

            """ Calculate number of completed tasks and total number of tasks """
            number_of_done_task = sum(1 for t in dat if t["completed"])
            total_number_of_tasks = len(dat)
            employee_name = emp["name"]
            user_id = emp["id"]
            username = emp["username"]

            """ Store task information for each employee """
            task_list = [{"username": username, "task": t["title"],
                          "completed": t["completed"]} for t in dat]

            """ Export data to JSON format """
            data = {user_id: task_list}
            all_data.update(data)

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(all_data, f)


if __name__ == "__main__":
    get_func()
