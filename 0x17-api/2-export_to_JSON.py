#!/usr/bin/python3
import json
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
        with open('{}.json'.format(user_id), mode="w", newline="") as file:
            dic_list = []
            for dic in tasks:
                new_dic = {}
                new_dic["task"] = dic.get('title')
                new_dic['completed'] = dic.get('completed')
                new_dic['username'] = username
                dic_list.append(new_dic)
            json_dic = {}
            json_dic[user_id] = dic_list
            json.dump(json_dic, file)
