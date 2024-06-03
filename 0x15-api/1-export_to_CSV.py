#!/usr/bin/python3
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export TODO list of a given employee ID to a CSV file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks data
    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
