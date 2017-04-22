#!/usr/bin/python3
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    with open('todo_all_employees.json', mode="w", newline="") as file:
        user_dic = {}
        for user in users:
            user_id = user.get('id')
            username = user.get('username')
            print(user_id)
            tasks = requests.get('{}{}/todos'.format(url, user_id)).json()
            dic_list = []
            for dic in tasks:
                new_dic = {}
                new_dic["task"] = dic.get('title')
                new_dic['completed'] = dic.get('completed')
                new_dic['username'] = username
                dic_list.append(new_dic)
            user_dic[user_id] = dic_list
        json.dump(user_dic, file)
