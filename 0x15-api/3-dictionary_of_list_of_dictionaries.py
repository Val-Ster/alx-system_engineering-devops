#!/usr/bin/python3
import json
import requests


def export_all_to_json():
    """Export TODO lists of all employees to a single JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()

    # Fetch all tasks
    tasks_response = requests.get(f"{base_url}/todos")
    tasks_data = tasks_response.json()

    # Prepare JSON data
    all_data = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [task for task in tasks_data
                      if task.get("userId") == user_id]

        tasks_list = []
        for task in user_tasks:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

            all_data[user_id] = tasks_list

    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(all_data, file)


if __name__ == "__main__":
    export_all_to_json()
