from fuzzywuzzy import fuzz

# Fuzzy search allows for minor spelling errors or variations
def fuzzy_search(query, text):
    """
    Perform a fuzzy search to check how closely the query matches the text.

    Args:
        query (str): The search query provided by the user.
        text (str): The extracted text from the image to search within.

    Returns:
        bool: True if the fuzzy ratio is greater than 80%, else False.
    """
    return fuzz.ratio(query.lower(), text.lower()) > 80  # Case-insensitive comparison

# Boolean search with "AND" operator
def boolean_search(query, text):
    """
    Perform a Boolean search for multiple terms connected by 'AND'.

    Args:
        query (str): The search query provided by the user, terms connected by 'AND'.
        text (str): The extracted text from the image to search within.

    Returns:
        bool: True if all terms are found in the text, else False.
    """
    terms = query.split(" AND ")
    return all(term.lower() in text.lower() for term in terms)  # Case-insensitive comparison
