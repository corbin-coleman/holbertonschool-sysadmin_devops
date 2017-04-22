#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        get_user = requests.get('{}{}'.format(url, user_id))
        username = get_user.json().get('username')
        tasks_req = requests.get('{}{}/todos'.format(url, user_id))
        tasks = tasks_req.json()
        with open('{}.csv'.format(user_id), mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            writer.writerows([user_id, username,
                              dic.get('completed'), dic.get('title')]
                             for dic in tasks)
