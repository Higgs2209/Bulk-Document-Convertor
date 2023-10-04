import aspose.words as aw
from datetime import date
#from main import dock_name


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


def compare_doc(doc, doc1, doc_name):
    doc.compare(doc1, "user", date.today(), options)
    x = doc.revisions.count
    print(doc_name)
    #print(x + 'changes count')
    print(x)
   # print(base_doc_name, new_doc_name)
    if x > 0:
        print(x)
        print("TEST")
        doc.save(f"compared {doc_name}.docx")
        print("Saved")


    else:
        print("Documents are equal")
