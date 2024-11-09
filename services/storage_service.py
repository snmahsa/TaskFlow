import csv
from models.project import Project
from models.task import Task

def save_data(projects):
    with open('projects.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Project Name', 'Task ID', 'Task Name', 'Description', 'Status', 'Start Time', 'End Time', 'Duration'])
        
        for project in projects.values():
            if not project.tasks: 
                writer.writerow([project.name, '', '', '', '', '', '', ''])  
            else:
                for task in project.list_tasks():
                    writer.writerow([project.name, task.task_id, task.name, task.description, task.status, task.start_time, task.end_time, task.duration])

def load_data(projects):
    try:
        with open('projects.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                project_name, task_id, task_name, description, status, start_time, end_time, duration = row
                project = projects.get(project_name) or Project(project_name)
                task = Task(task_name, description)
                task.task_id = task_id
                task.status = status == 'True'
                task.start_time = start_time  
                task.end_time = end_time 
                task.duration = float(duration)
                project.add_task(task)
                projects[project_name] = project
    except FileNotFoundError:
        print("File 'projects.csv' not found. No data loaded.")