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
        EMPLOYEE_NAME = json.loads(f.read().decode())
    with urllib.request.urlopen(url_user + sys.argv[1] + "/todos/") as f:
        todo_data = json.loads(f.read().decode())

    """ Calculate number of completed tasks and total number of tasks """
    NUMBER_OF_DONE_TASKS = sum(1 for todo in todo_data if todo["completed"])
    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    EMPLOYEE_NAME = EMPLOYEE_NAME["name"]

    """ Display progress report """
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for todo in todo_data:
        TASK_TITLE = todo["title"]
        if todo["completed"]:
            print("\t{} ".format(TASK_TITLE))

if __name__ == "__main__":
    get_func()
