from pydantic import BaseModel

class DraftingTask(BaseModel):
    context: str
    purpose: str
    constraints: str = ""


def load_drafting_tasks():
    return [
        DraftingTask(
            context="Your team failed to submit the project deliverables on time.",
            purpose="Write an apology mail to the manager.",
            constraints="Polite, brief, professional"
        ),
        DraftingTask(
            context="You need information about upcoming internship opportunities.",
            purpose="Write an email asking the placement cell.",
            constraints="Clear, concise, respectful"
        ),
        DraftingTask(
            context="You are unable to attend tomorrow’s meeting.",
            purpose="Draft a mail requesting rescheduling.",
            constraints="Short, polite"
        ),
    ]
