# Task Manager CLI

Welcome to the Task Manager CLI! This is a simple command-line tool where you can manage your daily tasks after logging in. It also supports multiple users, so each user can register and manage their own list of tasks.

## Features

1. **Register**: Create a new account with a unique username and password.
2. **Login**: Log in to your account to access your tasks.
3. **Task Management**:
   - **Add Task**: Add new tasks with details like title, description, due date, and priority.
   - **View Tasks**: See all your tasks neatly in a table.
   - **Delete Task**: Remove tasks you no longer need.
   - **Complete Task**: Mark tasks as completed to keep track of your progress.
4. **Logout**: Log out of your account.

## How It Works

The tool is based in the terminal/command line. You’ll register first, then log in with your username and password to access your tasks. Each user’s data is stored in a separate file to keep it private.

### File Structure

- **users.json**: This file stores usernames and passwords.
- **[username]_tasks.json**: Each user has a unique file (like `kenson_tasks.json`) to store their tasks.

### Commands and Navigation

1. **Starting the Program**: Run `python task_manager.py` to start.
2. **Choose Register or Login**: You’ll be asked if you want to register, log in, or exit.
3. **Inside Task Manager**:
   - Choose from options to add, view, delete, or complete tasks.
   - You can view tasks as a table with details like priority and completion status.
   - Choose “Logout” to go back to the main menu.

## Example

```plaintext
Welcome to the Task Manager CLI!

1. Register
2. Login
3. Exit

Choose an option: 1

--- Register ---
Enter a username: kenson
Enter a password: ****
Registration successful!
