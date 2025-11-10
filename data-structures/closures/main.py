def word_count_aggregator():
    count = 0

    def add_count(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return add_count
