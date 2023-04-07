#!/usr/bin/python3
""" Using an REST API for a given employee ID and
    returns information about his/her TODO list progress """

import requests
import sys


EMPLOYEE_ID = sys.argv[1]
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(EMPLOYEE_ID)

response = requests.get(TODO_API_URL)
todo_list = response.json()

NUMBER_OF_DONE_TASKS = sum(1 for todo in todo_list if todo["completed"])
TOTAL_NUMBER_OF_TASKS = len(todo_list)

EMPLOYEE_API_URL = "https://jsonplaceholder.typicode.com/users/{}"\
                    .format(EMPLOYEE_ID)

employee_response = requests.get(EMPLOYEE_API_URL)
employee = employee_response.json()
EMPLOYEE_NAME = employee["name"]

print("Employee {} is done with tasks({}/{}):"\
      .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for todo in todo_list:
    if todo["completed"]:
        print("\t{}" .format(todo["title"]))
