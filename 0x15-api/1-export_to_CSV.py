#!/usr/bin/python3
"""Script to access a REST API for TODO lists of employees"""

import requests
import sys
from sys import argv


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeId = sys.argv[1]
    url = baseUrl + "/" + employeeId

    # Get employee name
    response = requests.get(url)
    username = response.json().get('username')

    # Get data on the ToDo of the employee
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # CSV format
    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
