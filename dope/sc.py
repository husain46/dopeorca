from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, Table, TableStyle)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus.flowables import Flowable

OUTPUT_FILE = "website_development_agreement.pdf"
TODAY = date.today().strftime("%d %B %Y")

PAGE_W, PAGE_H = A4
LM = 22 * mm
RM = 22 * mm
TM = 20 * mm
BM = 20 * mm
CONTENT_W = PAGE_W - LM - RM

DARK     = colors.HexColor("#1a1a2e")
BLUE     = colors.HexColor("#0f3460")
GOLD     = colors.HexColor("#b8962e")
LIGHT_BG = colors.HexColor("#f0f3fa")
GREY     = colors.HexColor("#555555")
BODY_CLR = colors.HexColor("#1e1e1e")
LINE_CLR = colors.HexColor("#cccccc")

doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    leftMargin=LM, rightMargin=RM,
    topMargin=TM, bottomMargin=BM,
)

def mk(name, **kw):
    return ParagraphStyle(name, **kw)

S_AGENCY  = mk("Agency",  fontName="Helvetica-Bold", fontSize=24,
                textColor=DARK, alignment=TA_CENTER, leading=30,
                spaceBefore=0, spaceAfter=0)
S_TAGLINE = mk("Tagline", fontName="Helvetica", fontSize=9,
                textColor=GREY, alignment=TA_CENTER, leading=13,
                spaceBefore=0, spaceAfter=0)
S_TITLE   = mk("Title",   fontName="Helvetica-Bold", fontSize=14,
                textColor=BLUE, alignment=TA_CENTER, leading=18,
                spaceBefore=0, spaceAfter=0)
S_DATE    = mk("Date",    fontName="Helvetica", fontSize=9.5,
                textColor=GREY, alignment=TA_CENTER, leading=14,
                spaceBefore=0, spaceAfter=0)
S_HEAD    = mk("Head",    fontName="Helvetica-Bold", fontSize=10.5,
                textColor=DARK, leading=14,
                spaceBefore=0, spaceAfter=0)
S_BODY    = mk("Body",    fontName="Helvetica", fontSize=9.5,
                textColor=BODY_CLR, alignment=TA_JUSTIFY, leading=15,
                spaceBefore=0, spaceAfter=0)
S_BULLET  = mk("Bul",     fontName="Helvetica", fontSize=9.5,
                textColor=BODY_CLR, leading=15, leftIndent=12,
                spaceBefore=0, spaceAfter=0)
S_TBL_HDR = mk("TH",      fontName="Helvetica-Bold", fontSize=9,
                textColor=DARK, leading=13)
S_TBL_VAL = mk("TV",      fontName="Helvetica", fontSize=9.5,
                textColor=BODY_CLR, leading=14)
S_SIG_HDR = mk("SigH",    fontName="Helvetica-Bold", fontSize=10,
                textColor=BLUE, leading=14, spaceBefore=0, spaceAfter=0)
S_SIG_LBL = mk("SigL",    fontName="Helvetica-Bold", fontSize=9,
                textColor=DARK, leading=13, spaceBefore=0, spaceAfter=0)
S_SIG_VAL = mk("SigV",    fontName="Helvetica", fontSize=9.5,
                textColor=BODY_CLR, leading=14, spaceBefore=0, spaceAfter=0)
S_FOOTER  = mk("Foot",    fontName="Helvetica-Oblique", fontSize=7.5,
                textColor=GREY, alignment=TA_CENTER, leading=11,
                spaceBefore=0, spaceAfter=0)

def sp(h):
    return Spacer(1, h * mm)

def hr(thick=0.7, clr=GOLD, before=0, after=3):
    return HRFlowable(width="100%", thickness=thick, color=clr,
                      spaceBefore=before * mm, spaceAfter=after * mm)

def hr_thin(before=0, after=3):
    return hr(0.4, LINE_CLR, before, after)

def section_head(n, title):
    return Paragraph(f"<b>{n}.&nbsp;&nbsp;{title.upper()}</b>", S_HEAD)

def body(t):
    return Paragraph(t, S_BODY)

def bul(t):
    return Paragraph(f"\u2022&nbsp; {t}", S_BULLET)

# ─── STORY ────────────────────────────────────────────────────────────────────
story = []

# ── HEADER ────────────────────────────────────────────────────────────────────
story.append(sp(2))
story.append(Paragraph("DopeOrca", S_AGENCY))
story.append(sp(2))          # explicit gap so tagline never overlaps
story.append(Paragraph("Web Design &amp; Development Agency", S_TAGLINE))
story.append(sp(4))
story.append(hr(2.0, BLUE, before=0, after=4))
story.append(Paragraph("WEBSITE DEVELOPMENT AGREEMENT", S_TITLE))
story.append(sp(3))
story.append(hr(2.0, BLUE, before=0, after=4))
story.append(sp(1))
story.append(Paragraph(f"<b>Agreement Date:</b>&nbsp; {TODAY}", S_DATE))
story.append(sp(4))

# ── PARTIES TABLE ─────────────────────────────────────────────────────────────
col = (CONTENT_W - 4 * mm) / 2

parties = Table(
    [[Paragraph("<b>SERVICE PROVIDER</b>", S_TBL_HDR),
      Paragraph("<b>CLIENT</b>", S_TBL_HDR)],
     [Paragraph("DopeOrca", S_TBL_VAL),
      Paragraph("Srichand Classes", S_TBL_VAL)],
     [Paragraph("Director: Shahid Khan", S_TBL_VAL),
      Paragraph("Representative: Harsh Sir", S_TBL_VAL)]],
    colWidths=[col, col]
)
parties.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), LIGHT_BG),
    ("LINEBELOW",     (0, 0), (-1, 0), 0.6, LINE_CLR),
    ("BOX",           (0, 0), (-1, -1), 0.6, colors.HexColor("#aaaaaa")),
    ("LINEBEFORE",    (1, 0), (1, -1), 0.6, colors.HexColor("#aaaaaa")),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 10),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
]))
story.append(parties)
story.append(sp(5))
story.append(hr_thin(before=0, after=4))

# ── SECTION 1 ─────────────────────────────────────────────────────────────────
story.append(section_head("1", "Project Scope"))
story.append(sp(2))
story.append(body(
    "DopeOrca agrees to design and develop a complete professional website for "
    "Srichand Classes. The following services are included in this agreement:"))
story.append(sp(2))
for item in [
    "Full website design and development",
    "Responsive and modern design optimised for all screen sizes and devices",
    "Contact / Enquiry form integration",
    "Basic SEO (Search Engine Optimisation) setup",
    "Domain connection (Client already owns the domain)",
    "Website deployment on live server",
]:
    story.append(bul(item))
    story.append(sp(1))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 2 ─────────────────────────────────────────────────────────────────
story.append(section_head("2", "Project Timeline"))
story.append(sp(2))
story.append(body(
    "The completed website will be delivered within <b>5 (five) working days</b> "
    "from the date of confirmation of the advance payment. The timeline commences "
    "only after the advance has been received and all required content, images, "
    "and information have been provided by the Client."))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 3 ─────────────────────────────────────────────────────────────────
story.append(section_head("3", "Payment Terms"))
story.append(sp(2))
story.append(body(
    "The total agreed fee for this project is "
    "<b>Rs. 7,900/- (Rupees Seven Thousand Nine Hundred Only)</b>. "
    "Payment shall be made in two equal instalments:"))
story.append(sp(2))
story.append(bul("<b>Instalment 1 – 50% Advance (Rs. 3,950/-)</b>"
                 " &nbsp;– Payable before commencement of work."))
story.append(sp(1.5))
story.append(bul("<b>Instalment 2 – 50% Balance (Rs. 3,950/-)</b>"
                 " &nbsp;– Payable after completion and before final handover."))
story.append(sp(2))
story.append(body(
    "No final files, credentials, or live deployment shall be handed over "
    "until full payment has been received by DopeOrca."))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 4 ─────────────────────────────────────────────────────────────────
story.append(section_head("4", "Support & Maintenance"))
story.append(sp(2))
story.append(body(
    "DopeOrca will provide post-launch support at no additional cost for a "
    "period of <b>1 (one) year</b> from the date of final handover:"))
story.append(sp(2))
story.append(bul("Any technical errors, bugs, or functional issues will be resolved free of charge."))
story.append(sp(1.5))
story.append(bul("Minor content updates or small adjustments may be accommodated during this support period."))
story.append(sp(1.5))
story.append(bul("Major new features or redesign work outside the original scope may be quoted separately."))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 5 ─────────────────────────────────────────────────────────────────
story.append(section_head("5", "Ownership & Rights Transfer"))
story.append(sp(2))
story.append(body(
    "Upon receipt of full and final payment, complete ownership of the website — "
    "including all design files, source code, and access credentials — shall be "
    "unconditionally transferred to the Client, Srichand Classes. DopeOrca "
    "retains no rights over the website content or intellectual property after the transfer."))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 6 ─────────────────────────────────────────────────────────────────
story.append(section_head("6", "Client Responsibilities"))
story.append(sp(2))
story.append(body("The Client agrees to fulfil the following obligations to ensure timely delivery:"))
story.append(sp(2))
story.append(bul("Provide accurate and complete content, text, images, logos, and any other required materials in a timely manner."))
story.append(sp(1.5))
story.append(bul("Provide prompt review and feedback on design mockups and development milestones."))
story.append(sp(1.5))
story.append(bul("Any delay in providing required information will result in a corresponding extension of the delivery timeline."))
story.append(sp(3))
story.append(hr_thin(before=0, after=4))

# ── SECTION 7 ─────────────────────────────────────────────────────────────────
story.append(section_head("7", "Additional Terms & Conditions"))
story.append(sp(2))
story.append(bul("Major additional features not discussed in this agreement may be quoted and charged separately."))
story.append(sp(1.5))
story.append(bul("This agreement constitutes the entire understanding between DopeOrca and Srichand Classes."))
story.append(sp(1.5))
story.append(bul("Either party may request amendments in writing, subject to mutual written consent."))
story.append(sp(1.5))
story.append(bul("This agreement shall be governed in accordance with applicable laws of India."))
story.append(sp(5))
story.append(hr(2.0, BLUE, before=0, after=5))

# ── SIGNATURE SECTION ─────────────────────────────────────────────────────────
story.append(Paragraph("ACKNOWLEDGEMENT &amp; SIGNATURES", S_TITLE))
story.append(sp(2))
story.append(body(
    "By signing below, both parties confirm they have read, understood, and agreed "
    "to all terms and conditions set forth in this Website Development Agreement."))
story.append(sp(6))

SIG_GAP = 16 * mm   # blank space for actual handwritten signature


def make_sig_col(header, org, name, extra_line=None):
    items = []
    items.append(Paragraph(header, S_SIG_HDR))
    items.append(Spacer(1, 2 * mm))
    items.append(HRFlowable(width="90%", thickness=1, color=BLUE,
                             spaceBefore=0, spaceAfter=5 * mm))
    items.append(Paragraph(f"Organisation:&nbsp; <b>{org}</b>", S_SIG_VAL))
    items.append(Spacer(1, 2 * mm))
    items.append(Paragraph(f"Name:&nbsp; <b>{name}</b>", S_SIG_VAL))
    if extra_line:
        items.append(Spacer(1, 1.5 * mm))
        items.append(Paragraph(extra_line, S_SIG_VAL))
    items.append(Spacer(1, SIG_GAP))
    items.append(Paragraph("Signature: &nbsp;_________________________________", S_SIG_LBL))
    items.append(Spacer(1, SIG_GAP))
    items.append(Paragraph("Date: &nbsp;______________________________________", S_SIG_LBL))
    items.append(Spacer(1, 5 * mm))
    return items


class ColBlock(Flowable):
    def __init__(self, items, width):
        Flowable.__init__(self)
        self._items = items
        self._col_w = width

    def wrap(self, aw, ah):
        h = sum(i.wrap(self._col_w, ah)[1] for i in self._items)
        self.width = self._col_w
        self.height = h
        return self._col_w, h

    def draw(self):
        y = self.height
        for item in self._items:
            iw, ih = item.wrap(self._col_w, self.height)
            y -= ih
            item.drawOn(self.canv, 0, y)


col_w = (CONTENT_W - 8 * mm) / 2

client_col = ColBlock(
    make_sig_col("FOR CLIENT", "Srichand Classes", "Harsh Sir"),
    col_w
)
agency_col = ColBlock(
    make_sig_col("FOR SERVICE PROVIDER", "DopeOrca", "Shahid Khan",
                 extra_line="Designation:&nbsp; Director"),
    col_w
)

sig_tbl = Table([[client_col, agency_col]], colWidths=[col_w, col_w])
sig_tbl.setStyle(TableStyle([
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING",    (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("LEFTPADDING",   (0, 0), (-1, -1), 0),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
    ("LINEAFTER",     (0, 0), (0, -1), 0.5, LINE_CLR),
    ("LEFTPADDING",   (1, 0), (1, -1), 10),
]))
story.append(sig_tbl)
story.append(sp(6))
story.append(hr(2.0, BLUE, before=0, after=3))
story.append(Paragraph(
    f"This agreement was prepared by DopeOrca on {TODAY}. "
    "Both parties have agreed to the terms set out above.", S_FOOTER))

doc.build(story)
print(f"PDF saved: {OUTPUT_FILE}")