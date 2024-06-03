#!/usr/bin/python3
"""Fetch data from a REST API and export it in JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    user_name = user.get('name')
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo.get('completed'))

    tasks = [{"task": todo.get("title"), "completed": todo.get("completed"),
             "username": user_name} for todo in todos]

    with open(f"{user_id}.json", "w") as json_file:
        json.dump({user_id: tasks}, json_file)

    print(f"Employee {user_name} is done with tasks
          ({completed_tasks}/{total_tasks}): ")
    for task in tasks:
        if task["completed"]:
            print(f"\t{task['task']}")
