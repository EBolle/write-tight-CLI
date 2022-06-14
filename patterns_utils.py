

def create_span_dict(words: set, class_name: str) -> dict:
    """
    Wraps the words in <span> elements including the class name and stores
    these elements as values. The words are the keys.
    """
    return {word: f"<span class='{class_name}'>{word}</span>" for word in words}