#!/usr/bin/python3
"""Fetches data from a REST API and export it in JSON format."""

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

    username = user.get('username')
    tasks = [{"task": todo.get("title"), "completed": todo.get("completed"),
              "username": username} for todo in todos]

    with open(f"{user_id}.json", "w") as json_file:
        json.dump({user_id: tasks}, json_file)
