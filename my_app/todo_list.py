# todo_list.py
from task import Task

class ToDoList:
    """Gère une liste de tâches"""

    def __init__(self):
        self.tasks = []  # Liste des objets Task

    def add_task(self, description):
        """Ajoute une tâche à la liste"""
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        """Affiche toutes les tâches"""
        if not self.tasks:
            print("📭 Aucune tâche enregistrée.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, index):
        """Supprime une tâche par son index"""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("✅ Tâche supprimée avec succès.")
        else:
            print("❌ Index invalide.")
