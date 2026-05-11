def validate_topic(topic: str):
    """
    Validates user research topic.
    """

    if not topic:
        return False, "Research topic cannot be empty."

    if len(topic.strip()) < 3:
        return False, "Topic is too short."

    if len(topic.strip()) > 300:
        return False, "Topic is too long."

    return True, "Valid"
