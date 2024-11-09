# Project Management System

This project is a simple project management system that allows users to manage projects and tasks. The system includes capabilities to add, delete, and update the status of tasks within each project.

## Project Contents

- **models**
  - `task.py`: Defines the `Task` class for managing tasks.
  - `project.py`: Defines the `Project` class for managing projects and their associated tasks.

- **services**
  - `project_service.py`: Services related to managing projects.
  - `task_service.py`: Services related to managing tasks.
  - `storage_service.py`: Services for saving and loading data from a CSV file.

## Features

- **Project Management**: Ability to add new projects and display existing projects.
- **Task Management**: Ability to add, remove tasks, and mark them as completed. It also allows recording the time period for tasks.
- **Task Details Visualization**: Display complete information about tasks, including status, start time, end time, and duration.
- **Task Duration Charts**: Ability to visualize bar charts of task durations for each project and across all projects.
- **Data Storage**: Ability to save project and task information in a CSV file.

## How to Use

### Installation

1. Clone this repository from GitHub.
2. Install the necessary requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Setup

To use the system, first add projects and tasks:

```
python3 main.py
```

## Video Tutorial

For a step-by-step guide on how to use this project, please watch the following video tutorial:

[Watch the Video Tutorial](https://github.com/snmahsa/myrep/blob/main/TaskFlow_1.mp4)


## Contributing

To contribute to this project, you can submit your suggestions and changes via Pull Request.

## Authors

- [Mahsa Sanaei ]

## License

This project is licensed under the MIT License.