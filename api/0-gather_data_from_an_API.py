#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import requests
import sys

url_user = "https://jsonplaceholder.typicode.com/users/"
url_user_id = "https://jsonplaceholder.typicode.com/todos?userId="


def get_func():
    """ Get Data """
    EMPLOYEE_ID = sys.argv[1]
    TODO_API_URL = url_user_id + "{}" .format(EMPLOYEE_ID)

    response = requests.get(TODO_API_URL)
    todo_list = response.json()

    NUMBER_OF_DONE_TASKS = sum(1 for todo in todo_list if todo["completed"])
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    EMPLOYEE_API_URL = url_user + "{}" .format(EMPLOYEE_ID)

    employee_response = requests.get(EMPLOYEE_API_URL)
    employee = employee_response.json()
    EMPLOYEE_NAME = employee["Name"]

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for todo in todo_list:
        if todo["completed"]:
        print("\t {}\n" .format(todo["title"]))

if __name__ == '__main__':
    get_func()
