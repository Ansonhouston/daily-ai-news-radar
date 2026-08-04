#!/usr/bin/env python3
"""Generate ATS-friendly A4 PDFs from the 4 CV markdown files."""
import re, sys, os, glob
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                HRFlowable, Table, TableStyle)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

TEAL = HexColor("#0f766e")
DARK = HexColor("#1f2937")
GREY = HexColor("#4b5563")

# Embed a CJK-capable face so Traditional Chinese (e.g. the FB page name
# "AI 係咁易") renders instead of falling back to Helvetica's missing glyphs.
CJK = None
for path, idx in (('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 0),):
    if os.path.exists(path):
        try:
            pdfmetrics.registerFont(TTFont('CJK', path, subfontIndex=idx))
            CJK = 'CJK'
            break
        except Exception as e:
            print('CJK font registration failed:', e, file=sys.stderr)
if CJK is None:
    print('WARNING: no CJK font found — Chinese text will not render', file=sys.stderr)

# CJK ideographs plus fullwidth punctuation.
CJK_RUN = re.compile(r'([⺀-鿿豈-﫿＀-￯]+)')

def wrap_cjk(s):
    if not CJK:
        return s
    return CJK_RUN.sub(lambda m: f'<font name="CJK">{m.group(1)}</font>', s)

def md_inline(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return wrap_cjk(s)

styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20,
                           leading=24, textColor=DARK, alignment=TA_CENTER),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=12,
                           leading=15, textColor=TEAL, alignment=TA_CENTER,
                           spaceBefore=2),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=8.5,
                              leading=11, textColor=GREY, alignment=TA_CENTER,
                              spaceBefore=4),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.5,
                         leading=13.5, textColor=TEAL, spaceBefore=11, spaceAfter=3),
    'h3': ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10.3,
                         leading=13, textColor=DARK, spaceBefore=8, spaceAfter=1),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.4,
                           leading=12.8, textColor=DARK, spaceAfter=3.5),
    'meta': ParagraphStyle('meta', fontName='Helvetica-Oblique', fontSize=8.8,
                           leading=11.4, textColor=GREY, spaceAfter=2),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.4,
                             leading=12.5, textColor=DARK, leftIndent=10,
                             bulletIndent=2, spaceAfter=2.6),
}

def build(md_path, pdf_path):
    lines = open(md_path).read().splitlines()
    story, i = [], 0
    contact_done = False
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip() or ln.strip() == '---':
            i += 1; continue
        if ln.startswith('# ') and not ln.startswith('## '):
            story.append(Paragraph(md_inline(ln[2:]), styles['name']))
        elif ln.startswith('### '):
            story.append(Paragraph(md_inline(ln[4:]), styles['h3']))
        elif ln.startswith('## '):
            txt = ln[3:]
            if not contact_done:
                story.append(Paragraph(md_inline(txt), styles['role']))
                # next non-empty non --- line is contact
                j = i + 1
                while j < len(lines) and (not lines[j].strip() or lines[j].strip() == '---'):
                    j += 1
                if j < len(lines) and not lines[j].startswith('#'):
                    story.append(Paragraph(md_inline(lines[j].strip()), styles['contact']))
                    i = j
                contact_done = True
                story.append(Spacer(1, 2))
                story.append(HRFlowable(width='100%', thickness=1.2, color=TEAL,
                                        spaceBefore=4, spaceAfter=2))
            else:
                story.append(Paragraph(md_inline(txt).upper(), styles['h2']))
                story.append(HRFlowable(width='100%', thickness=0.7, color=TEAL,
                                        spaceBefore=0, spaceAfter=3))
        elif ln.startswith('|'):
            # collect table
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    if not rows:
                        rows.append([Paragraph(
                            f'<font color="white"><b>{md_inline(c)}</b></font>',
                            styles['body']) for c in cells])
                    else:
                        rows.append([Paragraph(md_inline(c), styles['body']) for c in cells])
                i += 1
            i -= 1
            ncols = max(len(r) for r in rows)
            avail = 178.0
            if ncols == 2:
                widths = [avail * 0.40, avail * 0.60]
            elif ncols == 3:
                widths = [avail * 0.25, avail * 0.27, avail * 0.48]
            else:
                widths = [avail / ncols] * ncols
            t = Table(rows, colWidths=[w * mm for w in widths], repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), TEAL),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#cbd5e1')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 3),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ]))
            # white bold text for header row
            hdr = [Paragraph(f'<font color="white"><b>{md_inline(c.text if hasattr(c,"text") else "")}</b></font>', styles['body']) for c in rows[0]]
            story.append(t)
            story.append(Spacer(1, 3))
        elif ln == '---PAGEBREAK---':
            story.append(PageBreak())
        elif ln.startswith('- '):
            story.append(Paragraph(md_inline(ln[2:]), styles['bullet'], bulletText='•'))
        elif ln.startswith('*') and ln.endswith('*') and not ln.startswith('**'):
            story.append(Paragraph(md_inline(ln), styles['meta']))
        else:
            story.append(Paragraph(md_inline(ln), styles['body']))
        i += 1

    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=16*mm, rightMargin=16*mm,
                            topMargin=13*mm, bottomMargin=13*mm,
                            title=os.path.basename(pdf_path)[:-4],
                            author='Anson Chan')
    doc.build(story)
    pages = doc.page
    print(f'wrote {os.path.basename(pdf_path)} — {pages} pages')

if __name__ == '__main__':
    targets = sys.argv[1:]
    if not targets:
        targets = sorted(glob.glob('/home/user/daily-ai-news-radar/cv/*.md'))
    for md in targets:
        build(md, md[:-3] + '.pdf')
