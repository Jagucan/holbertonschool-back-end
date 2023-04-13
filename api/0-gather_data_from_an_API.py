#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import json
import requests
import sys


url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """ This function gets data from the placeholders API """
    EMPLOYEE_NAME = requests.get(url_user + sys.argv[1]).json()
    todo_data = requests.get(url_user + sys.argv[1] + "/todos/").json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    TASK_TITLE = ""

    for todo in todo_data:
        if todo["completed"] is True:
            TASK_TITLE += "\t {}\n".format(todo["title"])
            NUMBER_OF_DONE_TASKS += 1

    """ Display progress report """
    print("Employee {} is done with tasks({}/{}):\n{}"
          .format(EMPLOYEE_NAME["name"], NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS, TASK_TITLE), end="")


if __name__ == "__main__":
    get_func()
