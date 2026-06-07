# models.py

class Task:
    def __init__(self, title):
        # Store task title
        self.title = title

        # Default state is not completed
        self.completed = False

    def complete(self):
        # Mark task as completed
        self.completed = True

        # Confirmation message
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        # Store user name
        self.name = name

        # Initialize empty task list
        self.tasks = []

    def add_task(self, task):
        # Add task to list
        self.tasks.append(task)

        # Confirmation message
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search tasks by title
        for task in self.tasks:
            if task.title == title:
                return task
        return None