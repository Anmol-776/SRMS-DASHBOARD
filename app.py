from flask import Flask, render_template, request, redirect, session
from storage import (
    load_employees,
    save_employees,
    load_tasks,
    save_tasks,
    load_resources,
    save_resources
)
from threads import auto_backup, deadline_monitor, resource_monitor
import threading
app = Flask(__name__)
app.secret_key = "srms_secret"

@app.route('/')
def dashboard():

    employees = load_employees()
    tasks_data = load_tasks()
    resources_data = load_resources()
    total_resources = len(resources_data)   

    total_members = len(employees)

    active_tasks = len(
        [task for task in tasks_data
         if task["status"] == "Pending"]
    )

    completed_tasks = len(
        [task for task in tasks_data
         if task["status"] == "Completed"]
    )

    return render_template(
        'dashboard.html',
        total_members=total_members,
        active_tasks=active_tasks,
        completed_tasks=completed_tasks,
        total_resources=total_resources
    )

@app.route('/team')
def team():

    employees = load_employees()

    return render_template(
        'team.html',
        employees=employees
    )
@app.route('/delete-member/<int:index>')
def delete_member(index):

    employees = load_employees()

    if 0 <= index < len(employees):
        employees.pop(index)

    save_employees(employees)

    return redirect('/team')
@app.route('/tasks')
def tasks():

    tasks_data = load_tasks()

    employees = load_employees()

    return render_template(
        'tasks.html',
        tasks=tasks_data,
        employees=employees
    )
@app.route('/complete-task/<int:index>')
def complete_task(index):

    tasks_data = load_tasks()

    if 0 <= index < len(tasks_data):
        tasks_data[index]["status"] = "Completed"

    save_tasks(tasks_data)

    return redirect('/tasks')
@app.route('/resources')
def resources():

    resources_data = load_resources()

    return render_template(
        'resources.html',
        resources=resources_data
    )
@app.route('/add-resource', methods=['POST'])
def add_resource():

    resources_data = load_resources()

    resources_data.append({
        "resource_name": request.form["resource_name"],
        "quantity": request.form["quantity"]
    })

    save_resources(resources_data)

    return redirect('/resources')
@app.route('/reports')
def reports():
    return render_template('reports.html')
@app.route('/add-member', methods=['POST'])
def add_member():

    employees = load_employees()

    employees.append({
        "name": request.form["name"],
        "role": request.form["role"],
        "department": request.form["department"]
    })

    save_employees(employees)

    return redirect('/team')
@app.route('/add-task', methods=['POST'])
def add_task():

    tasks_data = load_tasks()

    tasks_data.append({
        "task_name": request.form["task_name"],
        "assigned_to": request.form["assigned_to"],
        "priority": request.form["priority"],
        "status": "Pending"
    })

    save_tasks(tasks_data)

    return redirect('/tasks')
threading.Thread(
    target=auto_backup,
    daemon=True
).start()

threading.Thread(
    target=deadline_monitor,
    daemon=True
).start()

threading.Thread(
    target=resource_monitor,
    daemon=True
).start()
if __name__ == "__main__":
    app.run(debug=True)
