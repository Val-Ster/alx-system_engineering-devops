#!/usr/bin/python3
"""
Fetches and displays information about an employee's TODO list progress
using a given REST API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress for a given employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user = user_response.json()
    employee_name = user.get('name')

    # Fetch todos information
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]

    # Print employee TODO progress
    print(f"Employee {employee_name} is done with tasks
          ({len(completed_tasks)} / {total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        fetch_employee_todo_progress(int(sys.argv[1]))
