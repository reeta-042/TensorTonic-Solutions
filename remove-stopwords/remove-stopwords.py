def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)
    for word in stopwords:
        while word in tokens:
            tokens.remove(word)

    return tokens

pass