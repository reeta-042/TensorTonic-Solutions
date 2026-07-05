def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
   
    num_relevant = len(relevant)
    top_recommended = recommended[:k]
    relevant = set(relevant)
    top_recommended = set(top_recommended)
    disjunct = len(list(relevant & top_recommended))
    precision = disjunct / k 
    recall = disjunct / num_relevant
    return [ precision , recall]