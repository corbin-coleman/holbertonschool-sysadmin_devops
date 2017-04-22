#!/usr/bin/python3
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        user = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        user_req = requests.get('{}users/{}'.format(url, user))
        name = user_req.json().get('name')
        if name is not None:
            req = requests.get('{}todos?userId={}'.format(url, user)).json()
            done = [x for x in req if x.get('completed') is True]
            tasks = len(req)
            print("Employee {} is done with tasks({:d}/{:d}):".format(
                name, len(done), tasks))
            for dic in done:
                print('\t {}'.format(dic.get('title')))
