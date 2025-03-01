# task.py
class Task:
    """Représente une seule tâche de la To-Do List"""

    def __init__(self, description):
        self.description = description  # Description de la tâche
        self.completed = False  # Par défaut, la tâche n'est pas complétée

    def mark_completed(self):
        """Marque la tâche comme terminée"""
        self.completed = True

    def __str__(self):
        """Retourne une représentation textuelle de la tâche"""
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"


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


# storage.py
import json

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


# main.py
from todo_list import ToDoList
from storage import save_tasks, load_tasks

def main():
    todo_list = ToDoList()
    load_tasks(todo_list)  # Charger les tâches enregistrées

    while True:
        print("\n📌 Menu To-Do List")
        print("1. Ajouter une tâche")
        print("2. Voir les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choice = input("👉 Choisissez une option : ")

        if choice == "1":
            desc = input("📝 Entrez la description de la tâche : ")
            todo_list.add_task(desc)
            save_tasks(todo_list)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            try:
                index = int(input("🔢 Entrez le numéro de la tâche à supprimer : ")) - 1
                todo_list.remove_task(index)
                save_tasks(todo_list)
            except ValueError:
                print("⚠️ Entrée invalide.")

        elif choice == "4":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Option invalide. Essayez encore.")

if __name__ == "__main__":
    main()
