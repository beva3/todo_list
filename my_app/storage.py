# storage.py
import json
from task import Task

def save_tasks(todo_list, filename="tasks.json"):
    """Enregistre les tâches dans un fichier JSON"""
    with open(filename, "w") as file:
        json.dump([task.__dict__ for task in todo_list.tasks], file)

def load_tasks(todo_list, filename="tasks.json"):
    """Charge les tâches depuis un fichier JSON"""
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                task = Task(task_data["description"])
                task.completed = task_data["completed"]
                todo_list.tasks.append(task)
    except FileNotFoundError:
        print("🔍 Aucun fichier trouvé, démarrage avec une liste vide.")
