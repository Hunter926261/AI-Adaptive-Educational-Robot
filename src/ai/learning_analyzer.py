def analyze_strength(stats):
    if not stats:
        return "unknown"

    correct = stats.get("correct", 0)
    incorrect = stats.get("incorrect", 0)

    if incorrect > correct:
        return "weak"

    if correct >= 2 * max(1, incorrect):
        return "strong"

    return "moderate"
