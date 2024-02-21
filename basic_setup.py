class Task:

    def __init__(
        self,
        name: str,
        description: str = None,
        status: str = None,
        start_date: str = None,
        due_date: str = None  
    ):
        self.task_id = 0
        
        self.name = name
        self.description = description
        self.status = status
        self.start_date = start_date
        self.due_date = due_date

    def __repr__(self):
        return f"Task {self.task_id}({self.name}, {self.status}, {self.start_date}, {self.due_date})"

task = Task("Clean room", "I need to clean my room", "New", "2025-01-01", "2026-01-01")

print(repr(task)) 
