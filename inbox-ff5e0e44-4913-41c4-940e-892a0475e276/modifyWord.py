from docxtpl import DocxTemplate


def createStatement(template, context_dict, month, year):
    doc = DocxTemplate(template)
    doc.render(context_dict)

    filename = f"statements/{month}{year}YNAB.docx"
    doc.save(filename)
    return filename

