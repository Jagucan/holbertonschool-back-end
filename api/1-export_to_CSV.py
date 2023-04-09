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
    username =  employee["username"]

    """ Display progress report """
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_task, total_number_of_tasks))
    for todo in todo_data:
        if todo["completed"]:
            print("\t{} ".format(todo["title"]))

    """ Export data to CSV format """
    task_data = []
    for todo in todo_data:
        task_title = todo["title"]
        task_completed_status = "True" if todo["completed"] else "False"
        task_data.append([user_id, username, task_completed_status, task_title])
    with open("{}.csv", mode="w" .format(user_id)) as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(task_data)

if __name__ == "__main__":
    get_func()
