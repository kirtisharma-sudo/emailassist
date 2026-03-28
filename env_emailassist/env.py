from openai import OpenAI
import instructor
from pydantic import BaseModel

class EmailAssistEnv:
    """
    Environment A - Lenient Version
    For AI email drafting, classification, and intent detection tasks.
    """

    def __init__(self, api_key=None):
        self.client = instructor.from_openai(OpenAI(api_key=api_key))
        self.logs = []

    # ---------------------------
    # 1. Email Generation Reward
    # ---------------------------
    def grade_generated_email(self, task, model_output):
        """
        Lenient reward function.
        Award points for partially correct formatting, tone, and relevance.
        """

        reward = 0

        if task.purpose.lower() in model_output.lower():
            reward += 1

        if len(model_output) > 50:
            reward += 1

        if any(word in model_output.lower() for word in ["dear", "regards", "thank"]):
            reward += 1

        # soft penalty for errors
        if "lorem" in model_output.lower():
            reward -= 0.5

        return reward

    # ---------------------------
    # 2. Category Classification
    # ---------------------------
    def grade_category(self, task, predicted):
        """
        Lenient classification reward.
        Accept similar category names and partial matches.
        """

        gold = task.correct_category.lower()
        predicted = predicted.lower()

        if predicted == gold:
            return 2  # perfect

        if gold in predicted or predicted in gold:
            return 1  # partial credit

        return -0.5  # soft penalty

    # ---------------------------
    # 3. Intent Detection
    # ---------------------------
    def grade_intent(self, task, prediction):
        """
        Lenient intent reward.
        """

        if prediction.lower() == task.correct_intent.lower():
            return 2

        if task.correct_intent.lower() in prediction.lower():
            return 1

        return -0.5

