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
    employee_id = sys.argv[1]
    api_url = url_user_id + "{}" .format(employee_id)

    response = requests.get(api_url)
    todo_list = response.json()

    NUMBER_OF_DONE_TASKS = sum(1 for todo in todo_list if todo["completed"])
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    EMPLOYEE_API_URL = url_user + "{}" .format(employee_id)

    employee_response = requests.get(EMPLOYEE_API_URL)
    employee = employee_response.json()
    employee_name = employee["name"]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for todo in todo_list:
        if todo["completed"]:
            print("\t {} " .format(todo["title"]))

if __name__ == '__main__':
    get_func()
