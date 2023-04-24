#!/usr/bin/python3
"""Uses a REST API to get and return some information"""
import requests
import json
from sys import argv


def main():
    """Save information about a user TODO list progress to a CSV file"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(url)
    res = requests.get(todo_url)

    if res.status_code == 200:
        res = res.json()
        name = requests.get(url).json().get('username')
        filename = "{}.json".format(argv[1])

        with open(filename, 'w', encoding='utf8') as json_file:
            obj_props = []
            user_id = ''
            for task in res:
                obj = {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": name}
                user_id = task["userId"]
                obj_props.append(obj)
            json.dump({user_id: obj_props}, json_file)

    return 0


if __name__ == '__main__':
    main()
