def grade_category(predicted: str, correct: str) -> float:
    """
    Lenient grading:
    +1.0  exact match
    +0.5  partial semantic match
    -0.2  wrong
    """
    predicted = predicted.lower().strip()
    correct = correct.lower().strip()

    if predicted == correct:
        return 1.0

    # Partial match lenient check
    if correct in predicted or predicted in correct:
        return 0.5

    return -0.2
