#!/usr/bin/python3
import requests
import sys


def get_employee_todo_list(employee_id):
    """Fetch and display the TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch tasks data
    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Calculate completed tasks
    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    # Display the progress
    print(f"Employee {employee_name} is done
          with tasks({number_of_done_tasks} / {total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
