# Cranfield-ir-project# Cranfield Information Retrieval System

## ISR Group Assignment Section 2

# Group Members
Nahom Meki UGR/9179/17
Tewodros Beshah UGR/4345/17
Temesgen Yohannes UGR/4291/17
Feyisa Gezahegn UGR/4624/17
Abel Tilahun UGR/9357/15

This project demonstrates a simple Information Retrieval (IR) system using the Cranfield dataset.

The project parses Cranfield XML files, indexes the documents, performs keyword-based retrieval, and evaluates retrieval performance using Precision and Recall.

---

# Objectives

- Understand the Cranfield dataset
- Understand Information Retrieval concepts
- Parse XML-like document collections
- Build an inverted index
- Perform document retrieval
- Evaluate search performance

---

# Dataset Files

| File | Description |
|---|---|
| cran.all.1400.xml | Contains 1400 documents |
| cran.qry.xml | Contains 225 search queries |
| cranqrel.trec.txt | Contains relevance judgments |

---

# Information Retrieval Workflow

1. Load documents
2. Build inverted index
3. Read queries
4. Search documents
5. Rank results
6. Compare with qrels
7. Compute Precision and Recall

---

# Technologies Used

- Python
- XML Parsing
- Regular Expressions
- Information Retrieval Concepts

---

# Project Files

| File | Purpose |
|---|---|
| parser.py | Reads documents and queries |
| indexer.py | Builds inverted index |
| search.py | Searches documents |
| evaluate.py | Computes Precision and Recall |

---

# How to Run

## 1. Run Parser

```bash
python parser.py
