def grade_draft(draft: str, context: str, purpose: str) -> float:
    """
    Lenient grading for drafting:
    +1.0 covers both context & purpose clearly
    +0.7 covers purpose clearly but context weak
    +0.5 understandable & polite but incomplete
    -0.2 irrelevant or extremely short
    """

    if not draft or len(draft.strip()) < 20:
        return -0.2

    draft_l = draft.lower()

    score = 0.0

    # Check purpose relevance
    if purpose.lower().split()[0] in draft_l:
        score += 0.4

    # Check context relevance
    key_context_word = context.lower().split()[0]
    if key_context_word in draft_l:
        score += 0.4

    # Politeness check (lenient)
    polite_words = ["please", "sorry", "thank", "regret", "kindly"]
    if any(w in draft_l for w in polite_words):
        score += 0.2

    # Cap score at 1.0
    return min(score, 1.0)
