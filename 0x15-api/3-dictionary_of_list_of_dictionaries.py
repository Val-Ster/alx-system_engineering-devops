#!/usr/bin/python3
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        todos_url =
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        username = user.get('username')
        tasks = [{"username": username, "task": todo.get("title"),
                  "completed": todo.get("completed")} for todo in todos]
        data[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
