#!/usr/bin/python3
"""Uses a REST API to get and return some information"""
import json
import requests


def main():
    """Save all information about a user's tasks to a json file"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url)

    if users.status_code == 200:
        with open("todo_all_employees.json", 'w') as json_file:
            objs = {}
            for user in users.json():
                todo_url = '{}{}/todos'.format(url, user['id'])
                todo = requests.get(todo_url)
                name = user['username']
                obj_props = []
                user_id = ''
                for task in todo.json():
                    obj = {
                            "task": task["title"],
                            "completed": task["completed"],
                            "username": name}
                    user_id = task["userId"]
                    obj_props.append(obj)
                objs[user_id] = obj_props
            json.dump(objs, json_file)

    return 0


if __name__ == '__main__':
    main()
