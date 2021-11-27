from docxtpl import DocxTemplate


def createStatement(template, context_dict, month, year):
    doc = DocxTemplate(template)
    doc.render(context_dict)

    doc.save(f"{month}{year}YNAB.docx")

