import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("📝 Enter task: ").strip()
    if title:
        task = {
            "title": title,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        print("✅ Task added!")
    else:
        print("⚠️ Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return

    print("\n📋 Your To-Do List:")
    print(f"{'No.':<5}{'Task':<40}{'Status':<10}{'Created At'}")
    print("-" * 70)
    for i, task in enumerate(tasks, start=1):
        status = "✔️ Done" if task["done"] else "❌ Pending"
        print(f"{i:<5}{task['title']:<40}{status:<10}{task['created_at']}")
    print("-" * 70)

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("🔢 Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("🗑️ Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"❌ Task '{removed['title']}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n📌 Menu:\n1. View Tasks\n2. Add Task\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
