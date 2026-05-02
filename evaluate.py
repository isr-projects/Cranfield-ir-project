from parser import load_queries
from search import search
from parser import load_documents
from indexer import build_index



def load_qrels(filepath):
    qrels = {}

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.split()

            if len(parts) != 4:
                continue

            topic, iteration, docno, relevance = parts

            if relevance == "1":
                if topic not in qrels:
                    qrels[topic] = set()

                qrels[topic].add(docno)

    return qrels



def precision(retrieved, relevant):
    if len(retrieved) == 0:
        return 0

    retrieved_relevant = len(set(retrieved) & relevant)

    return retrieved_relevant / len(retrieved)



def recall(retrieved, relevant):
    if len(relevant) == 0:
        return 0

    retrieved_relevant = len(set(retrieved) & relevant)

    return retrieved_relevant / len(relevant)


if __name__ == "__main__":
    documents = load_documents("data/cran.all.1400.xml")
    queries = load_queries("data/cran.qry.xml")
    qrels = load_qrels("data/cranqrel.trec.txt")

    index = build_index(documents)

    total_precision = 0
    total_recall = 0

    evaluated_queries = 0

    for q in queries[:10]:
        qid = q["id"]
        query_text = q["query"]

        results = search(query_text, index)

        retrieved_docs = [doc_id for doc_id, score in results[:10]]

        relevant_docs = qrels.get(qid, set())

        p = precision(retrieved_docs, relevant_docs)
        r = recall(retrieved_docs, relevant_docs)

        total_precision += p
        total_recall += r

        evaluated_queries += 1

        print("=" * 50)
        print(f"Query ID: {qid}")
        print(f"Query: {query_text}")
        print(f"Precision: {p:.2f}")
        print(f"Recall: {r:.2f}")

    avg_precision = total_precision / evaluated_queries
    avg_recall = total_recall / evaluated_queries

    print("\nAverage Precision:", round(avg_precision, 2))
    print("Average Recall:", round(avg_recall, 2))
