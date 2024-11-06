from models.task import Task
from services.project_service import get_project

def add_task(project_name, task_name, description):
    project = get_project(project_name)
    if not project:
        print(f"Project '{project_name}' does not exist.")
    else:
        task = Task(task_name, description)
        project.add_task(task)
        print(f"Task '{task_name}' added to project '{project_name}'.")

def remove_task(project_name, task_id):
    project = get_project(project_name)
    if not project:
        print(f"Project '{project_name}' does not exist.")
    else:
        if project.check_task(task_id):
            project.remove_task(task_id)
            print(f"Task with ID '{task_id}' removed from project '{project_name}'.")
        else:
            print(f"Task with ID '{task_id}' not found in project '{project_name}'.")

def mark_task_done(project_name, task_id, start_time, end_time):
    project = get_project(project_name)
    if not project:
        print(f"Project '{project_name}' does not exist.")
    else:
        task = project.get_task(task_id)
        if task:
            task.mark_done(start_time, end_time)
            print(f"Task '{task.name}' marked as done.")
        else:
            print("Task ID not found.")

def display_tasks(project_name):
    project = get_project(project_name)
    if not project:
        print(f"Project '{project_name}' does not exist.")
    else:
        project.list_tasks()
