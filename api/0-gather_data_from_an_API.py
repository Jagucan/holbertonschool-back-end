#!/usr/bin/python3
"""
    Using an REST API for a given employee ID and
    returns information about list progress
"""

import requests
import sys

url_base = "https://jsonplaceholder.typicode.com/users/"
url_id = "https://jsonplaceholder.typicode.com/todos?userId="


def get_func():
    """ Get Data """
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    """ Get user information """
    user_url = url_base + "{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    """ Get list for the user """
    employee_api_url = url_id + "{}".format(employee_id)
    todo_response = requests.get(employee_api_url)
    todo_data = todo_response.json()

    """ Calculate number of completed tasks """
    number_of_done_task = sum(1 for todo in todo_data if todo["completed"])

    """ Calculate total number of tasks """
    total_number_of_tasks = len(todo_data)

    """ Print progress report """
    employee_name = user_data["name"]
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_task, total_number_of_tasks))

    for todo in todo_data:
        if todo["completed"]:
            print("\t{} ".format(todo["title"]))

if __name__ == "__main__":
    get_func()
