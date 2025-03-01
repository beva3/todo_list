# storage.py
import json
import os # Importer le module os pour gérer les fichiers
from task import Task

# define the path to store task
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # get the current file path
DATA_FOLDER = "Data"
TASKES_FILE = os.path.join(DATA_FOLDER, "tasks.json")

# ensure the data folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER) # create the folder {'data/'} if it doesn't exist

def save_tasks(todo_list):
    """Enregistre les tâches dans un fichier JSON"""
    with open(TASKES_FILE, "w", encoding="utf-8") as file:
        json.dump([task.__dict__ for task in todo_list.tasks], file, ensure_ascii=False, indent=4)

def load_tasks(todo_list, filename="tasks.json"):
    """Charge les tâches depuis un fichier JSON"""
    try:
        if not os.path.exists(filename):
            return
        
        with open(TASKES_FILE, "r", encoding="utf-8") as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                task = Task(task_data["description"])
                task.completed = task_data["completed"]
                todo_list.tasks.append(task)
    except FileNotFoundError:
        print("🔍 Aucun fichier trouvé, démarrage avec une liste vide.")
