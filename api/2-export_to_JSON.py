#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import csv
import json
import requests
import sys


url_user = "https://jsonplaceholder.typicode.com/users/"


def get_func():
    """Get data from the placeholders API and export to CSV format"""
    EMPLOYEE_NAME = requests.get(url_user + sys.argv[1]).json()
    todo_data = requests.get(url_user + sys.argv[1] + "/todos/").json()

    """Count completed tasks and generate task titles"""
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for todo in todo_data:
        if todo["completed"] is True:
            TASK_TITLE.append(todo["title"])
            NUMBER_OF_DONE_TASKS += 1

    """Export data to CSV format"""
    USER_ID = sys.argv[1]
    USERNAME = EMPLOYEE_NAME['username']
    data = []
    for todo in todo_data:
        TASK_TITLE = todo["title"]
        TASK_COMPLETED_STATUS = "True" if todo["completed"] else "False"
        data.append([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
    with open("{}.csv".format(USER_ID), mode="w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)

    """ Export data to JSON format """
    data = {USER_ID: [{"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,
                       "username": USERNAME} for todo in todo_data]}
    with open("{}.json".format(USER_ID), mode="w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    get_func()
