import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(CWD, "venv/lib/python3.7/site-packages"))

from docxtpl import DocxTemplate


def createStatement(template, context_dict, month, year):
    doc = DocxTemplate(template)
    doc.render(context_dict)

    filename = f"statements/{month}{year}YNAB.docx"
    doc.save(filename)
    return filename

