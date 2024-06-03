#!/usr/bin/python3
"""Fetch data from a REST API and export it in JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    # Extract user ID from command-line argument
    user_id = sys.argv[1]

    # Construct URLs for user and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    # Fetch user and todos data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Parse user and todos data as JSON
    user = user_response.json()
    todos = todos_response.json()

    # Extract user name
    user_name = user.get('name')

    # Construct tasks list with correct formatting
    tasks = [{"task": todo.get("title"), "completed": todo.get("completed"),
             "username": user_name} for todo in todos]

    # Write tasks to JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump({user_id: tasks}, json_file)
