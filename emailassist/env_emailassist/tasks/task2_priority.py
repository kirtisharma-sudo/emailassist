from pydantic import BaseModel

class PriorityTask(BaseModel):
    email_text: str
    correct_priority: str


def load_priority_tasks():
    return [
        PriorityTask(
            email_text="URGENT: Server is down. Need immediate fix.",
            correct_priority="High"
        ),
        PriorityTask(
            email_text="Reminder: Monthly report due next week.",
            correct_priority="Medium"
        ),
        PriorityTask(
            email_text="FYI: Office cafeteria menu updated.",
            correct_priority="Low"
        ),
        PriorityTask(
            email_text="Please approve the budget sometime today.",
            correct_priority="Medium"
        ),
    ]
