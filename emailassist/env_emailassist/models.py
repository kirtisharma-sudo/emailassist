from pydantic import BaseModel


# ---------------------------
# Task 1: Category Classification
# ---------------------------
class CategoryTask(BaseModel):
    email_text: str
    correct_category: str


# ---------------------------
# Task 2: Priority Classification
# ---------------------------
class PriorityTask(BaseModel):
    email_text: str
    correct_priority: str


# ---------------------------
# Task 3: Email Drafting
# ---------------------------
class DraftingTask(BaseModel):
    context: str           # Background info
    purpose: str           # What the email should achieve
    constraints: str = ""  # (Optional) Tone, format instructions


# ---------------------------
# LLM Outputs
# ---------------------------
class CategoryPrediction(BaseModel):
    category: str


class PriorityPrediction(BaseModel):
    priority: str


class DraftedEmail(BaseModel):
    email_text: str


# ---------------------------
# Reward Return Format
# ---------------------------
class RewardResponse(BaseModel):
    reward: float
