#!/usr/bin/env python3
"""One-page A4 cheat sheet for the Activate Talent screening call.

Two-column layout, sized to be scannable mid-call on a laptop screen.
Cantonese labels for fast scanning; English for anything Anson would say aloud.

Markup convention: content strings use **bold** only. Never write literal <b>
tags in content — T() escapes angle brackets before applying markup, so a
literal tag would render as visible text.
Glyphs are restricted to what Helvetica (WinAnsi) plus the CJK face can draw:
no emoji, no U+25AA-style symbols.
"""
import os
import re
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

TEAL = HexColor("#0f766e")
TEAL_D = HexColor("#115e59")
DARK = HexColor("#1f2937")
GREY = HexColor("#4b5563")
RED = HexColor("#b91c1c")
BG = HexColor("#f1f5f9")

CJK = None
if os.path.exists('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'):
    try:
        pdfmetrics.registerFont(
            TTFont('CJK', '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', subfontIndex=0))
        CJK = 'CJK'
    except Exception as exc:  # pragma: no cover
        print('CJK font registration failed:', exc, file=sys.stderr)
if CJK is None:
    print('WARNING: no CJK font — Chinese will not render', file=sys.stderr)

CJK_RUN = re.compile(r'([⺀-鿿豈-﫿＀-￯]+)')
BULLET = '•'  # in WinAnsi; U+25AA is not


def T(s):
    """Markdown-ish inline -> reportlab markup, with CJK runs font-tagged."""
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    if CJK:
        s = CJK_RUN.sub(lambda m: f'<font name="CJK">{m.group(1)}</font>', s)
    return s


S = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=15,
                           leading=17, textColor=white),
    'sub': ParagraphStyle('sub', fontName='Helvetica', fontSize=8.4,
                          leading=10.4, textColor=HexColor('#ccfbf1')),
    'when': ParagraphStyle('when', fontName='Helvetica-Bold', fontSize=9,
                           leading=11.4, textColor=white, alignment=TA_CENTER),
    'h': ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=9.2,
                        leading=11, textColor=TEAL_D, spaceAfter=1.5),
    'b': ParagraphStyle('b', fontName='Helvetica', fontSize=7.9, leading=9.9,
                        textColor=DARK, spaceAfter=1.8),
    'bul': ParagraphStyle('bul', fontName='Helvetica', fontSize=7.9, leading=9.9,
                          textColor=DARK, leftIndent=8, bulletIndent=1,
                          spaceAfter=1.8),
    'say': ParagraphStyle('say', fontName='Helvetica-Oblique', fontSize=7.8,
                          leading=9.8, textColor=TEAL_D, leftIndent=6,
                          spaceAfter=2.0),
    'red': ParagraphStyle('red', fontName='Helvetica-Bold', fontSize=7.6,
                          leading=9.5, textColor=RED, spaceAfter=1.8),
    'redbul': ParagraphStyle('redbul', fontName='Helvetica', fontSize=7.8,
                             leading=9.8, textColor=RED, leftIndent=8,
                             bulletIndent=1, spaceAfter=1.8),
    'tiny': ParagraphStyle('tiny', fontName='Helvetica', fontSize=7.3,
                           leading=9.2, textColor=GREY, spaceAfter=1.5),
}


def head(text):
    return [Paragraph(T(text), S['h']),
            HRFlowable(width='100%', thickness=0.6, color=TEAL,
                       spaceBefore=0, spaceAfter=2.5)]


def p(text, style='b'):
    return Paragraph(T(text), S[style])


def bul(text, style='bul'):
    return Paragraph(T(text), S[style], bulletText=BULLET)


def say(text):
    return Paragraph(T('“' + text + '”'), S['say'])


def gap(h=5.5):
    return Spacer(1, h)


# ---------------------------------------------------------------- left column
left = []

left += head('目標 — 30 分鐘做乜')
left += [
    p('Danny 係 **gatekeeper，唔係客戶**。佢唯一決定：值唔值得將你 present 俾客戶。'),
    bul('易 present（一句講清你係邊個）'),
    bul('記得住你（一個數字）'),
    bul('唔踩雷（唔好令佢覺得你唔穩定）'),
    p('你實際只有 **~10 分鐘** 講嘢 → 揀重點，唔好樣樣講。'),
]

left += [gap()]
left += head('開場 60 秒 — 順序唔可以亂')
left += [
    p('**1. 商業信譽**'),
    say('Eight years in creative and performance marketing for consumer brands '
        'in Hong Kong and Southeast Asia. I ran creative direction and performance '
        'on about HK$500,000 a month of paid spend at Hong Kong\'s number one baby '
        'e-commerce platform, at 3 to 7 times ROAS.'),
    p('**2. 差異化證據**'),
    say('For two years I\'ve run my own AI-education brand, @aieasyjob, solo across '
        'YouTube, Instagram and Facebook. One Facebook Reel hit 76,000 organic views '
        'off a 77-follower page — roughly 990 times follower count, zero paid support.'),
    p('**3. 護城河**'),
    say('I build AI production pipelines. I use Claude daily as infrastructure, not '
        'as a toy — custom skills and multi-step workflows for scripting, briefs, '
        'competitor teardowns, automated carousel production. That\'s the only reason '
        'one person can sustain weekly multi-platform output.'),
    p('佢中途打斷都冇事 — 最重要兩樣已經講咗。', 'tiny'),
]

left += [gap()]
left += head('數字 — 唔好記錯')
_nums = [
    ('累計投放', 'HK$3M+ @ 3–10x ROAS'),
    ('峰值月投放', 'HK$500K+ @ 3–7x ROAS'),
    ('增量 GMV', 'HK$300K / 5 個月'),
    ('A/B 測試', '+200% CVR，峰值 10x+ ROAS'),
    ('救亡案例', 'ROAS 0.3x → 3x / 90 日'),
    ('FB 王牌', '76,000 views（~990x 粉絲、~210x 中位數）'),
    ('FB 第二條', '11,000 views — 證明係結構唔係好運'),
    ('YouTube', '84,000+ views / 57 條片'),
    ('KOL / Email', '200+ KOL；Klaviyo 30,000 訂閱'),
    ('AI 起步', '2022 年（早業界 ~2 年）'),
]
_t = Table([[p('**' + k + '**', 'tiny'), p(v, 'tiny')] for k, v in _nums],
           colWidths=[23 * mm, 64 * mm])
_t.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 1.0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1.0),
    ('LEFTPADDING', (0, 0), (-1, -1), 2.5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 2),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, BG]),
    ('LINEBEFORE', (0, 0), (0, -1), 1.4, TEAL),
]))
left += [_t]

left += [gap()]
left += head('紅旗 — 聽住')
left += [
    bul('一路唔肯講行業／公司類型 → mandate 未 confirm', 'redbul'),
    bul('講 flexible hours 但迴避時區 → 大機會要美東 overlap', 'redbul'),
    bul('只賣 remote 好處、迴避內容 → 用彈性補償薪酬', 'redbul'),
    bul('問 lowest you\'d accept → 唔好答，重申範圍', 'redbul'),
]

left += [gap()]
left += head('Call 前 checklist')
left += [
    bul('測 Google Meet 鏡頭 + 麥 — **佢明確評 communication style**'),
    bul('背景乾淨、光源在前'),
    bul('**開住 76K 條 FB Reel** — 想睇即 share screen，勝過講數字'),
    bul('開住 D 版 CV（熟自己寫過乜）'),
    bul('紙筆記佢答嘅內容 — client interview 要對得上'),
    bul('香港晚 8:00 call → 唔好食得太飽'),
]

# --------------------------------------------------------------- right column
right = []

right += head('佢問 → 你答')
right += [
    p('**「Why are you looking?」** — 最大風險位'),
    say('Freelance and my own channel let me test creative methods across 20-plus '
        'brands without anyone\'s approval. But the ceiling is real — I\'m optimising '
        'short campaigns, or my own channel with no budget. I want to put the method '
        'behind one brand with real scale and compound it over years, not quarters.'),
    p('唔好講：想穩定啲／freelance 難做／想有固定收入', 'red'),

    p('**「How do you use AI?」** 佢一定問 — 講系統，唔好講工具名單'),
    bul('**Claude** = reasoning：script、brief、teardown、custom skills'
        '（chained，唔係逐次 re-prompt）'),
    bul('**Midjourney / Ideogram** = brief-to-visual'),
    bul('**Governance** = template + QC checklist + naming、version control'),
    say('The point isn\'t speed. It\'s 10-plus variants per cycle while still holding '
        'single-variable discipline, so results stay attributable. That drove a 200% '
        'conversion rate lift. I started this in 2022 — about two years before it '
        'became standard.'),

    p('**「Salary expectations?」** 兩段式 — 唔好一次答'),
    p('**第一次問 → 推返俾佢**', 'tiny'),
    say('I\'d rather understand the shape first — employment or contractor, and what '
        'the hours look like — those change the number. What has the client budgeted?'),
    p('**佢再追（大機會）→ 才給範圍**', 'tiny'),
    say('For a full-time Hong Kong-based creative strategy role at my level, '
        'HK$40,000 to 55,000 a month. If it\'s contractor without benefits, that '
        'needs to be higher to be equivalent.'),
    p('絕對唔好講 USD $3,500 / HK$27,000', 'red'),

    p('**「Will you keep running @aieasyjob?」**'),
    say('Yes — but it\'s where I test methods before using them on someone\'s budget. '
        'Everything I\'d bring here gets prototyped there first. Happy to talk through '
        'boundaries if there\'s any concern.'),

    p('**Notice period** → freelance 所以快，主動講，係優勢。'),
]

right += [gap()]
right += head('你問返 — 按次序')
right += [
    p('**1. 時區（最高優先 — 佢答得到）**'),
    say('Is there a required overlap with US hours, or is this work-anywhere within '
        'Hong Kong hours?'),
    p('佢用紐約時間，開放時段 = 香港晚 8:00 – 凌晨 3:30。若要美東 overlap 即夜班。', 'tiny'),
    p('**2. 客戶想解決乜問題**'),
    say('What are they looking to accomplish with this hire — scaling output, '
        'improving creative performance, or building a function that doesn\'t exist yet?'),
    p('**3. 為何我嘅背景突出**'),
    say('You said my background stood out — what specifically? It helps me know what '
        'to emphasise with the client.'),
    p('唔好再追 budget／reporting structure／team composition／exact hours／comp range '
      '— 佢已明確話留到 client interview 階段。', 'red'),
]


def build(path):
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=11 * mm, rightMargin=11 * mm,
        topMargin=9 * mm, bottomMargin=9 * mm,
        title='Activate Talent Screening — Cheat Sheet',
        author='Anson Chan')

    banner = Table([[
        [Paragraph(T('ACTIVATE TALENT — SCREENING CALL'), S['name']),
         Paragraph(T('Creative Strategist (Remote, HK) · Danny Mejia, recruiting '
                     'partner · 30 min · Google Meet'), S['sub'])],
        [Paragraph(T('Thu 30 / Fri 31 Jul'), S['when']),
         Paragraph(T('揀 8:00am EDT'), S['when']),
         Paragraph(T('= 香港 8:00pm'), S['when'])],
    ]], colWidths=[136 * mm, 52 * mm])
    banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TEAL),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LINEBEFORE', (1, 0), (1, 0), 0.8, HexColor('#5eead4')),
    ]))

    body = Table([[left, None, right]], colWidths=[89 * mm, 10 * mm, 89 * mm])
    body.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))

    doc.build([banner, Spacer(1, 6), body])
    print(f'wrote {os.path.basename(path)} — {doc.page} page(s)')


if __name__ == '__main__':
    build('/home/user/daily-ai-news-radar/cv/'
          'Anson_Chan_Screening_CheatSheet_ActivateTalent_2026-07-29.pdf')
