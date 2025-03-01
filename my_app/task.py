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
