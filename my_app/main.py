# main.py (optimized with match-case)
from todo_list import ToDoList
# from storage import save_tasks, load_tasks

def main():
    todo_list = ToDoList()
    # load_tasks(todo_list)  # Charger les tâches enregistrées

    while True:
        print("\n📌 Menu To-Do List")
        print("1. Ajouter une tâche")
        print("2. Voir les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choice = input("👉 Choisissez une option : ")

        match choice:
            case "1":
                desc = input("📝 Entrez la description de la tâche : ")
                todo_list.add_task(desc)
                # save_tasks(todo_list)

            case "2":
                todo_list.view_tasks()
                

            case "3":
                # todo_list.view_tasks()
                try:
                    index = int(input("🔢 Entrez le numéro de la tâche à supprimer : ")) - 1
                    todo_list.remove_task(index)
                    # save_tasks(todo_list)
                except ValueError:
                    print("⚠️ Entrée invalide.")

            case "4":
                print("👋 Au revoir !")
                break

            case _:
                print("❌ Option invalide. Essayez encore.")

if __name__ == "__main__":
    main()
