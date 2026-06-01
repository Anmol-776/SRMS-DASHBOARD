import json

EMPLOYEE_FILE = "data/employees.json"


def load_employees():
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_employees(data):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(data, file, indent=4)
TASK_FILE = "data/tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(data):
    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)
RESOURCE_FILE = "data/resources.json"

def load_resources():
    try:
        with open(RESOURCE_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_resources(data):
    with open(RESOURCE_FILE, "w") as file:
        json.dump(data, file, indent=4)