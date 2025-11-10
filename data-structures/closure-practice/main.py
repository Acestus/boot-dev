def new_collection(initial_docs):
    new_docs = initial_docs.copy()
    def new_function(doc=new_docs):
        new_docs.append(doc)
        return new_docs
    return new_function
