#!/usr/bin/python3
"""Uses a REST API to get and return some information"""
import csv
import requests
from sys import argv


def main():
    """Save information about a user TODO list progress to a CSV file"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(url)
    res = requests.get(todo_url)

    if res.status_code == 200:
        res = res.json()
        name = requests.get(url).json().get('username')
        filename = "{}.csv".format(argv[1])

        with open(filename, 'w', encoding='utf8') as csv_file:
            csv_file = csv.writer(
                    csv_file, delimiter=',',
                    quoting=csv.QUOTE_ALL, quotechar='"')
            for task in res:
                csv_file.writerow(
                        [
                            task['userId'], name,
                            task['completed'], task['title']])

    return 0


if __name__ == '__main__':
    main()
