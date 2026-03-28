"""
Baseline inference script for EmailAssist Environment.

This model is intentionally simple, rule-based, and fully deterministic.
It ensures that the environment never crashes during evaluation.
"""

import re


# -----------------------------
# 1. Category Prediction
# -----------------------------
def predict_category(email_text: str) -> str:
    text = email_text.lower()

    if any(word in text for word in ["meeting", "project", "report", "team", "work"]):
        return "Work"
    if any(word in text for word in ["order", "shipped", "delivery", "invoice"]):
        return "Notification"
    if "offer" in text or "discount" in text:
        return "Promotion"

    return "General"


# -----------------------------
# 2. Priority Prediction
# -----------------------------
def predict_priority(email_text: str) -> str:
    text = email_text.lower()

    if "urgent" in text or "asap" in text or "immediately" in text:
        return "High"
    if "reminder" in text or "due" in text:
        return "Medium"

    return "Low"


# -----------------------------
# 3. Email Draft Generation
# -----------------------------
def generate_draft(context: str, purpose: str, constraints: str = "") -> str:
    """
    Simple template-based drafting.
    Always returns polite, short, and safe text.
    """

    return (
        f"Hello,\n\n"
        f"I am writing regarding {context.lower()}. "
        f"I would like to {purpose.lower()}. "
        f"Please let me know if you need any additional information.\n\n"
        f"Thank you."
    )


# -----------------------------
# Main Inference Function
# -----------------------------
def inference(state: dict):
    """
    Receives environment state.
    Returns an action dictionary.
    """

    task_type = state.get("task_type")

    # --- Task 1: Category ---
    if task_type == "category":
        return {
            "category": predict_category(state["email_text"])
        }

    # --- Task 2: Priority ---
    if task_type == "priority":
        return {
            "priority": predict_priority(state["email_text"])
        }

    # --- Task 3: Drafting ---
    if task_type == "draft":
        return {
            "email_text": generate_draft(
                state["context"],
                state["purpose"],
                state.get("constraints", "")
            )
        }

    # Fallback
    return {}
