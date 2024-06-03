#!/usr/bin/python3
import json
import requests
import sys


def export_to_json(employee_id):
    """Export TODO list of a given employee ID to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks data
    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Prepare JSON data
    tasks_list = []
    for task in tasks_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
            })

        json_data = {employee_id: tasks_list}

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
