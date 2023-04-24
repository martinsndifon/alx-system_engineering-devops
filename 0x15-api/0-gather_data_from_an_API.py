#!/usr/bin/python3
"""Uses a REST API to get and return some information"""
import requests
from sys import argv


def main():
    """Returns information about a user's TODO list progress"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(url)
    res = requests.get(todo_url)

    if res.status_code == 200:
        res = res.json()
        name = requests.get(url).json().get('name')
        completed_tasks = [val for val in res if val.get('completed')]
        length = len(completed_tasks)
        total = len(res)
        print('Employee {} is done with tasks({}/{}):'.format(
            name, length, total))

        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))
    return 0


if __name__ == '__main__':
    main()
