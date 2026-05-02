from parser import load_documents


def tokenize(text):
    return text.lower().split()



def build_index(documents):
    index = {}

    for doc in documents:
        doc_id = doc["id"]
        text = doc["title"] + " " + doc["text"]

        words = tokenize(text)

        for word in words:
            if word not in index:
                index[word] = set()

            index[word].add(doc_id)

    return index


if __name__ == "__main__":
    documents = load_documents("data/cran.all.1400.xml")

    index = build_index(documents)

    print("Indexed Terms:", len(index))

    sample_word = "aircraft"

    if sample_word in index:
        print(f"Documents containing '{sample_word}':")
        print(index[sample_word])
