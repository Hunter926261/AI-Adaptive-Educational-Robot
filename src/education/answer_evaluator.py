def evaluate_answer(user_answer, expected_keywords, language="en"):
    user_answer = user_answer.lower()

    for keyword in expected_keywords:
        if keyword.lower() in user_answer:
            return True

    return False
