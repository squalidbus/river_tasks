class Project:

    def __init__(
        self,
        name: str,
        description: str = None,
        status: str = None,
        start_date: str = None,
        due_date: str = None,
    ):
        self.task_id = 0
        
        self.name = name
        self.description = description
        self.status = status
        self.start_date = start_date
        self.due_date = due_date

class Task:

    def __init__(
        self,
        name: str,
        description: str = None,
        status: str = None,
        start_date: str = None,
        due_date: str = None,
        project: Project = None,
    ):
        self.task_id = 0
        
        self.name = name
        self.description = description
        self.status = status
        self.start_date = start_date
        self.due_date = due_date
        self.project = project

    def __repr__(self):
        return f"Task {self.task_id}({self.name}, {self.status}, {self.start_date}, {self.due_date}, {self.project.name})"

project = Project("Fix my life", "Need to get my life on track", "In Progress", "2025-01-01", "2026-01-1")
task = Task("Clean room", "I need to clean my room", "New", "2025-01-02", "2026-01-03", project)

print(repr(task)) 
