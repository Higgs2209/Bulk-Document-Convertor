import aspose.words as aw
from datetime import date
from compare_doc import compare_doc
from directory_scanner import scan_directory

x = 0




# ["Trial Division - Civil - affidavit_new.docx", "Trial Division - Civil - affidavit_old.docx", "test_doc_new.docx", "test_doc_old.docx"]
new_docs = []
old_docs = []
docs = scan_directory('Base Documents')
# file_list = scan_directory('Base Documents')

# Create two lists of old and new files
for i in docs:
    if "old" in i:
        old_docs.append(i)

    if "new" in i:
        new_docs.append(i)


# Cycle through the documents and convert to document type
for i, j in zip(new_docs, old_docs):
    print(i, j)
    global base_doc_name
    global new_doc_name
    base_doc_name = j
    new_doc_name = i
    doc_name = i
    print(doc_name)
    i = "Base Documents/" + i
    j = "Base Documents/" + j
    doc = aw.Document(i)
    doc1 = aw.Document(j)
    print(i)
    print(doc)
    print(doc1)


    compare_doc(doc, doc1, doc_name)
    print(x)
    x += 1
    print(x)



