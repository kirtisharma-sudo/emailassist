from pydantic import BaseModel

class CategoryTask(BaseModel):
    email_text: str
    correct_category: str


def load_category_tasks():
    return [
        CategoryTask(
            email_text="Please send me the updated sales figures for Q3.",
            correct_category="Work"
        ),
        CategoryTask(
            email_text="Your Amazon order has been shipped!",
            correct_category="Notification"
        ),
        CategoryTask(
            email_text="Can we reschedule our meeting to Monday?",
            correct_category="Work"
        ),
        CategoryTask(
            email_text="Your Netflix subscription will renew tomorrow.",
            correct_category="Notification"
        ),
    ]
