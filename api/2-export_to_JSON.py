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
    """Get data from the placeholders API and export to JSON format"""
    USER_ID = sys.argv[1]
    EMPLOYEE_DATA = requests.get(url_user + USER_ID).json()
    todo_data = requests.get(url_user + USER_ID + "/todos/").json()

    """Count completed tasks and generate task titles"""
    NUMBER_OF_DONE_TASK = 0
    TASK_TITLE = []
    for todo in todo_data:
        if todo["completed"] is True:
            TASK_TITLE.append(todo["title"])
            NUMBER_OF_DONE_TASK += 1

    """ Export data to JSON format """
    data = []
    USERNAME = EMPLOYEE_DATA['username']
    for todo in todo_data:
        TASK_TITLE = todo["title"]
        TASK_COMPLETED_STATUS = "True" if todo["completed"] else "False"
        data.append({"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,
                     "username": USERNAME})
    with open("{}.json".format(USER_ID), mode="w") as f:
        json.dump({USER_ID: data}, f)


if __name__ == "__main__":
    get_func()
