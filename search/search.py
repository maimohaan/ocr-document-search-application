from fuzzywuzzy import fuzz

def fuzzy_search(query, text):
    """
    Perform a fuzzy search for the query in the extracted text.
    Args:
        query (str): The search query.
        text (str): The extracted text.
    Returns:
        bool: True if a fuzzy match is found, False otherwise.
    """
    # Tokenize the text into words
    text_words = text.split()
    for word in text_words:
        # Calculate the fuzz ratio for each word
        if fuzz.partial_ratio(query, word) >= 80:  # Adjust threshold as needed
            return True
    return False

def boolean_search(query, text):
    """
    Perform a Boolean search for the query in the extracted text.
    Args:
        query (str): The search query.
        text (str): The extracted text.
    Returns:
        bool: True if a match is found, False otherwise.
    """
    # Split the query into terms
    query_terms = query.split()
    # Check if all terms are present in the text
    return all(term.lower() in text.lower() for term in query_terms)
