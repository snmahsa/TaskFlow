from services.project_service import add_project, display_projects, save_projects, load_projects
from services.task_service import add_task,remove_task, mark_task_done,display_tasks, search_task,chart_task_durations, plot_task_durations_for_all_projects
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
        print("7. Search Task With Name in Selected Project")
        print("8. Generate a bar chart for the durations of tasks in a specific project")
        print("9. Generate a bar chart for the durations of tasks across all projects")
        print("10. Save All Projects")
        print("11. Load csv Projects")
        print("0. Exit")

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
            print("Tasks :")
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
            project_name = input(">>>Enter project name: ")
            task_name = input(">>>Enter task name: ")
            search_task(project_name, task_name)
        
        elif choice == "8":
            project_name = input(">>>Enter project name for draw chart: ")
            chart_task_durations(project_name)

        elif choice == "9":
            plot_task_durations_for_all_projects()

        elif choice == "10":
            save_projects()

        elif choice == "11":
            load_projects()            
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
