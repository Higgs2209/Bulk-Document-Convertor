import aspose.words as aw
from datetime import date
from compare_doc import compare_doc
x = 0

docs = ["Trial Division - Civil - affidavit_new.docx", "Trial Division - Civil - affidavit_old.docx", "test_doc_new.docx", "test_doc_old.docx"]
new_docs = []
old_docs = []

# Create two lists of old and new files
for i in docs:
    if "old" in i:
        old_docs.append(i)

    if "new" in i:
        new_docs.append(i)


# Cycle through the documents and convert to document type
for i, j in zip(new_docs, old_docs):
    print(i, j)
    doc = aw.Document(i)
    doc1 = aw.Document(j)
    print(doc)
    print(doc1)

    compare_doc(doc, doc1, x)
    print(x)
    x += 1
    print(x)



