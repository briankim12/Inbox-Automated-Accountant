from docxtpl import DocxTemplate


def createStatement(template, context_dict, month, year):
    doc = DocxTemplate(template)
    doc.render(context_dict)

    doc_name = f"{month}{year}YNAB.docx"
    aws_temp_path = f"/temp/{doc_name}"
    doc.save(aws_temp_path)
    return aws_temp_path

