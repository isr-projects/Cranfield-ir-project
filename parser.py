import re


def load_documents(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = "<root>" + content + "</root>"

    docs = re.findall(r"<doc>(.*?)</doc>", content, re.DOTALL)

    documents = []

    for d in docs:
        try:
            docno = re.search(r"<docno>(.*?)</docno>", d, re.DOTALL).group(1).strip()
            title = re.search(r"<title>(.*?)</title>", d, re.DOTALL).group(1).strip()
            text = re.search(r"<text>(.*?)</text>", d, re.DOTALL).group(1).strip()

            documents.append({
                "id": docno,
                "title": title,
                "text": text
            })

        except:
            pass

    return documents


def load_queries(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = "<root>" + content + "</root>"

    topics = re.findall(r"<top>(.*?)</top>", content, re.DOTALL)

    queries = []

    for t in topics:
        try:
            qid = re.search(r"<num>(.*?)</num>", t, re.DOTALL).group(1).strip()
            title = re.search(r"<title>(.*?)</title>", t, re.DOTALL).group(1).strip()

            queries.append({
                "id": qid,
                "query": title
            })

        except:
            pass

    return queries


if __name__ == "__main__":
    documents = load_documents("data/cran.all.1400.xml")
    queries = load_queries("data/cran.qry.xml")

    print("Total Documents:", len(documents))
    print("Total Queries:", len(queries))

    print("\nFirst Document:")
    print(documents[0])

    print("\nFirst Query:")
    print(queries[0])
