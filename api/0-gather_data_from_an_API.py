#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import json
import sys
import urllib.request


url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """ This function gets data from the placeholders API """
    with urllib.request.urlopen(url_user + sys.argv[1]) as f:
        employee_name = json.loads(f.read().decode())
    with urllib.request.urlopen(url_user + sys.argv[1] + "/todos/") as f:
        todo_data = json.loads(f.read().decode())

    """ Calculate number of completed tasks and total number of tasks """
    number_of_done_task = sum(1 for todo in todo_data if todo["completed"])
    total_number_of_tasks = len(todo_data)
    employee_name = employee_name["name"]

    """ Display progress report """
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_task, total_number_of_tasks))
    for todo in todo_data:
        if todo["completed"]:
            print("\t{} ".format(todo["title"]))

if __name__ == "__main__":
    get_func()
