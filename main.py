from services.project_service import add_project, display_projects
from services.task_service import add_task,remove_task, mark_task_done, display_tasks
import time
def main_menu():
    while True:
        print("\n--- Time Tracker ---")
        print("1. Add Project")
        print("2. Add Task to Project")
        print("3. Remove Task to Project")
        print("4. Mark Task as Done")
        print("5. Display Tasks")
        print("6. Display All Projects")
        print("7. Exit")

        choice = input(">>>Select an option: ")
        
        if choice == "1":
            project_name = input(">>>Enter project name: ")
            add_project(project_name)
        
        elif choice == "2":
            project_name = input(">>>Enter project name: ")
            task_name = input(">>>Enter task name: ")
            description = input(">>>Enter task description: ")
            add_task(project_name, task_name, description)
        
        elif choice == "3":
            project_name = input(">>>Enter project name: ")
            display_tasks(project_name)
            time.sleep(1)
            task_id = input(">>>Enter task ID: ") 
            remove_task(project_name, task_id)

        elif choice == "4":
            project_name = input(">>>Enter project name: ")
            display_tasks(project_name)
            task_id = input(">>>Enter task ID: ")
            start_time = input(">>>Enter start time (HH:MM): ")
            end_time = input(">>>Enter end time (HH:MM): ")
            mark_task_done(project_name, task_id, start_time, end_time)
        
        elif choice == "5":
            project_name = input(">>>Enter project name to display tasks: ")
            display_tasks(project_name)
        
        elif choice == "6":
            display_projects()
        
        elif choice == "7":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
