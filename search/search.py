def search_keywords(text, keywords):
    """Searches for keywords within the extracted text."""
    keywords = keywords.lower().split()  # Convert to lowercase and split into words
    search_results = []
    for keyword in keywords:
        if keyword in text.lower():
            search_results.append(f"Found keyword: '{keyword}'")
    return "\n".join(search_results)
