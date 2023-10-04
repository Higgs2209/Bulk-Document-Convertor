import aspose.words as aw
from datetime import date


# set additional options
options = aw.comparing.CompareOptions()
options.ignore_formatting = True
options.ignore_headers_and_footers = True
options.ignore_case_changes = True
options.ignore_tables = True
options.ignore_fields = True
options.ignore_comments = True
options.ignore_textboxes = True
options.ignore_footnotes = True

#  date.today(),

def compare_doc(doc, doc1, i):
    doc.compare(doc1, "user", date.today(), options)
    x = doc.revisions.count
    print(x)
    if x > 0:
        print("Test")
        doc.save(f"compared{i}.docx")


    else:
        print("Documents are equal")
