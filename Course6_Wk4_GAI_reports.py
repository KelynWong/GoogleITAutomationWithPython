#!/usr/bin/env python3

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import datetime

def generate_report(attachment, title, paragraph):
    doc = SimpleDocTemplate(attachment, pagesize=letter)
    report_title = "Processed Update on {}".format(datetime.date.today())
    report = []
    report.append(Spacer(1, 12))
    report.append(Paragraph(report_title, getSampleStyleSheet()["Title"]))
    report.append(Spacer(1, 12))

    for entry in paragraph:
        name, weight = entry
        report.append(Paragraph("name: {}".format(name), getSampleStyleSheet()["Normal"]))
        report.append(Paragraph("weight: {} lbs".format(weight), getSampleStyleSheet()["Normal"]))
        report.append(Spacer(1, 12))

    doc.build(report)
