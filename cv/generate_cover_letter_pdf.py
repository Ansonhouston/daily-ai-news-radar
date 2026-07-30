#!/usr/bin/env python3
"""Render a cover-letter markdown file to a one-page A4 PDF.

Letter layout (date, addressee block, salutation, body, sign-off) rather than
the CV generator's section-and-rule structure.

Markup convention: **bold** and *italic* only — never literal HTML tags, since
T() escapes angle brackets before applying markup.
"""
import glob
import os
import re
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate,
                                Spacer)

TEAL = HexColor("#0f766e")
DARK = HexColor("#1f2937")
GREY = HexColor("#4b5563")

CJK = None
if os.path.exists('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'):
    try:
        pdfmetrics.registerFont(
            TTFont('CJK', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', subfontIndex=0))
        CJK = 'CJK'
    except Exception as exc:  # pragma: no cover
        print('CJK font registration failed:', exc, file=sys.stderr)

CJK_RUN = re.compile(r'([⺀-鿿豈-﫿＀-￯]+)')


def T(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', s)
    if CJK:
        s = CJK_RUN.sub(lambda m: f'<font name="CJK">{m.group(1)}</font>', s)
    return s


S = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=19,
                           leading=23, textColor=DARK, alignment=TA_CENTER),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=11.5,
                           leading=14, textColor=TEAL, alignment=TA_CENTER,
                           spaceBefore=2),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=8.6,
                              leading=11, textColor=GREY, alignment=TA_CENTER,
                              spaceBefore=4),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.6,
                           leading=13.6, textColor=DARK, spaceAfter=6.5),
    'addr': ParagraphStyle('addr', fontName='Helvetica', fontSize=9.4,
                           leading=12.4, textColor=DARK, spaceAfter=1.5),
}


def build(md_path, pdf_path):
    lines = open(md_path).read().splitlines()
    story = []
    i = 0
    header_done = False
    last = None
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            # Blank lines separate the date / addressee / subject / salutation
            # groups. Body paragraphs carry their own spaceAfter already.
            if header_done and last == 'addr':
                story.append(Spacer(1, 5))
                last = None
            i += 1
            continue
        if ln.strip() == '---':
            if not header_done:
                story.append(Spacer(1, 2))
                story.append(HRFlowable(width='100%', thickness=1.2, color=TEAL,
                                        spaceBefore=4, spaceAfter=10))
                header_done = True
            i += 1
            continue
        if ln.startswith('# '):
            story.append(Paragraph(T(ln[2:]), S['name']))
        elif ln.startswith('## '):
            story.append(Paragraph(T(ln[3:]), S['role']))
        elif not header_done:
            story.append(Paragraph(T(ln), S['contact']))
        else:
            # Short standalone lines before the salutation are address block.
            style = 'addr' if (len(ln) < 70 and not ln.endswith(('.', '?'))
                              and 'Dear' not in ln) else 'body'
            if ln.startswith('**Anson Chan**'):
                story.append(Spacer(1, 12))  # room for a signature
            story.append(Paragraph(T(ln), S[style]))
            last = style
        i += 1

    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=14 * mm, bottomMargin=14 * mm,
        title=os.path.basename(pdf_path)[:-4], author='Anson Chan')
    doc.build(story)
    print(f'wrote {os.path.basename(pdf_path)} — {doc.page} page(s)')


if __name__ == '__main__':
    targets = sys.argv[1:] or sorted(
        glob.glob('/home/user/daily-ai-news-radar/cv/*CoverLetter*.md'))
    for md in targets:
        build(md, md[:-3] + '.pdf')
