from parser import load_documents, load_queries
from indexer import build_index



def tokenize(text):
    return text.lower().split()



def search(query, index):
    scores = {}

    words = tokenize(query)

    for word in words:
        if word in index:
            for doc_id in index[word]:
                scores[doc_id] = scores.get(doc_id, 0) + 1

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked


if __name__ == "__main__":
    documents = load_documents("data/cran.all.1400.xml")
    queries = load_queries("data/cran.qry.xml")

    index = build_index(documents)

    query = queries[0]["query"]

    print("Query:")
    print(query)

    print("\nTop Results:")

    results = search(query, index)

    for doc_id, score in results[:10]:
        print(f"Document {doc_id} | Score: {score}")
