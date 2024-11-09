from models.project import Project
from services.storage_service import save_data, load_data
projects = {}

def add_project(name):
    if name in projects:
        print(f"Project '{name}' already exists.")
    else:
        projects[name] = Project(name)
        print(f"Project '{name}' added successfully.")

def display_projects():
    if not projects:
        print("No projects available.")
    else:
        for project in projects.values():
            print(f"Project: {project.name}, Tasks: {len(project.tasks)}")

def get_project(name):
    return projects.get(name, None)

def get_all_project():
    return projects

def save_projects():
    save_data(projects)

def load_projects():
    load_data(projects)
