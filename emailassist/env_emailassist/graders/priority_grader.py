def grade_priority(predicted: str, correct: str) -> float:
    """
    Priority levels: High / Medium / Low
    Lenient scoring:
    +1.0 exact match
    +0.5 close match (High↔Medium or Medium↔Low)
    -0.2 wrong
    """

    p = predicted.lower().strip()
    c = correct.lower().strip()

    if p == c:
        return 1.0

    # Close match (adjacent priority levels)
    if (p == "high" and c == "medium") or \
       (p == "medium" and c == "high") or \
       (p == "medium" and c == "low") or \
       (p == "low" and c == "medium"):
        return 0.5

    return -0.2
