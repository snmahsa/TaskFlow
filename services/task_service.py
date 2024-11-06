from models.task import Task
from services.project_service import get_project, get_all_project
import matplotlib.pyplot as plt
import pandas as pd
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
        project.listـofـtasksـdetails()

def search_task(project_name, task_name):
    project = get_project(project_name)
    if not project:
        print(f"Project '{project_name}' doesn't exist.")
        return
    
    tasks = project.list_tasks()

    if not tasks:
        print("No tasks available in this project.")
        return

    for task in tasks:
        if task.name == task_name:
            print(f"ID: {task.task_id}, Name: {task.name}, Status: {'Done' if task.status else 'Not Done'}\n", end=' ')
            if task.status:
                print(f", Duration: {task.duration}")
                print(f", Start time: {task.start_time}")
                print(f", End time: {task.end_time}\n")

def chart_task_durations(project_name):
    project = get_project(project_name)
    # print(project.list_tasks())
    if not project:
        print(f"Project '{project_name}' dont already exists.")
        return 
    tasks = project.list_tasks()
    if not tasks:
        print("No tasks available in this project.")
        return
    
    task_names = [task.name for task in tasks]
    durations = [task.duration for task in tasks]
    plt.bar(task_names, durations)
    plt.xlabel('Tasks')
    plt.ylabel('Duration (hours)')
    plt.title(f'Task Durations for Project {project.name}')
    plt.show()

def plot_task_durations_for_all_projects():

    all_task_names = []
    all_durations = []
    all_projects = get_all_project()
    if not all_projects:
        print("No projects available.")
        return
    for project in all_projects.values():
        for task in project.list_tasks():
            if task.status:  
                all_task_names.append(task.name)
                all_durations.append(task.duration)

    plt.figure(figsize=(12, 7))
    plt.bar(all_task_names, all_durations, color='lightgreen')
    plt.xlabel('Task Names')
    plt.ylabel('Duration (hours)')
    plt.title('Task Durations Across All Projects')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()