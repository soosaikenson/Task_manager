import json
import os
import getpass
import platform
from prettytable import PrettyTable

# Utility function to clear the screen based on the OS
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# ---------------- User Authentication ----------------

def load_users():
    """Load user credentials from users.json"""
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_users(users):
    """Save user credentials to users.json"""
    with open('users.json', 'w') as file:
        json.dump(users, file)

def register():
    """Register a new user"""
    users = load_users()
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try again.")
        return None

    password = getpass.getpass("Enter a password: ")
    users[username] = password
    save_users(users)
    print("Registration successful!")
    return username

def login():
    """User login"""
    users = load_users()
    print("\n--- Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if users.get(username) == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

# ---------------- Task Management ----------------

class Task:
    def __init__(self, id, title, description, due_date, priority, completed=False):
        """Initialize a new task"""
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else "✓"
        # status = "✓" if self.completed else "✗"
        return (f"[{status}] {self.id}: {self.title} | Priority: {self.priority} | "
                f"Due: {self.due_date} | Description: {self.description}")

def get_task_file_path(username):
    """Generate the file path for the user's tasks"""
    return f"{username}_tasks.json"

def load_tasks(username):
    """Load tasks for a user from their JSON file"""
    file_path = get_task_file_path(username)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                return [Task(**task) for task in json.load(file)]
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks, username):
    """Save tasks to the user's JSON file"""
    file_path = get_task_file_path(username)
    with open(file_path, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

# ---------Task Management Functions-------------------

def add_task(tasks, username):
    """Add a new task and auto-save"""
    print("\n--- Add Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High, Medium, Low): ")
    task_id = len(tasks) + 1
    new_task = Task(task_id, title, description, due_date, priority)
    tasks.append(new_task)
    save_tasks(tasks, username)
    print(f"Task added: {new_task.title}")

def view_tasks(tasks):
    """Display tasks in a table format"""
    clear_screen()
    if not tasks:
        print("No tasks available.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Title", "Description", "Due Date", "Priority", "Completed"]
        for task in tasks:
            status = "✓" if task.completed else "✗"
            table.add_row([task.id, task.title, task.description, task.due_date, task.priority, status])
        print(table)
    input("\nPress Enter to continue...")

def delete_task(tasks, username):
    """Delete a task by ID and auto-save"""
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task.id == task_id:
                tasks.remove(task)
                save_tasks(tasks, username)
                print(f"Task deleted: {task.title}")
                return
        print(f"No task found with ID {task_id}")
    except ValueError:
        print("Invalid ID format.")
    input("\nPress Enter to continue...")

def complete_task(tasks, username):
    """Mark a task as completed and auto-save"""
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        for task in tasks:
            if task.id == task_id:
                task.completed = True
                save_tasks(tasks, username)
                print(f"Task marked as complete: {task.title}")
                return
        print(f"No task found with ID {task_id}")
    except ValueError:
        print("Invalid ID format.")
    input("\nPress Enter to continue...")

def task_manager(username):
    """Task management functionality after user login"""
    tasks = load_tasks(username)
    while True:
        clear_screen()
        print(f"\n--- Task Manager for {username} ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks, username)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks, username)
        elif choice == '4':
            complete_task(tasks, username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main loop with login functionality"""
    clear_screen()
    print("Welcome to the Task Manager CLI!")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                task_manager(username)
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()