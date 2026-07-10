"""
Create an enum class `TaskPriority` that represents different task priority levels:
`LOW`, `MEDIUM`, `HIGH`, and `URGENT`.

Each priority level shuold be associated with an integer value for comparison.
Create a `Task` class that represents a task with a title and priority.
Create a `TaskManager` class that:
- Stores tasks.
- Retrieves importnat tasks (HIGH or URGENT).
- Sorts tasks based on priority.

>>> TaskPriority.LOW < TaskPriority.HIGH
True
>>> print(TaskPriority.URGENT)
TaskPriority.URGENT
>>> task = Task("Submit report", TaskPriority.URGENT)
>>> print(task)
URGENT | Submit report
>>> manager = TaskManager()
>>> manager.add_task(Task("Report", TaskPriority.HIGH))
>>> manager.add_task(Task("Email", TaskPriority.LOW))
>>> list(map(str, manager.get_important_tasks()))
['HIGH | Report']
>>> manager.add_task(Task("Critical Bug Fix", TaskPriority.URGENT))
>>> list(map(str, manager.get_important_tasks()))
['HIGH | Report', 'URGENT | Critical Bug Fix']
>>> manager.add_task(Task("Routine check", TaskPriority.LOW))
>>> print(manager)
URGENT | Critical Bug Fix
HIGH | Report
LOW | Email
LOW | Routine check
"""

from enum import Enum


class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}"


class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"{self.priority.name} | {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_important_tasks(self):
        """
        Returns tasks that are HIGH or URGENT priority.
        """
        return [task for task in self.tasks if task.priority in (TaskPriority.HIGH, TaskPriority.URGENT)]

    def __str__(self):
        """
        Returns tasks sorted by priority.
        """
        return "\n".join(map(str, sorted(self.tasks, key=lambda task: task.priority, reverse=True)))
