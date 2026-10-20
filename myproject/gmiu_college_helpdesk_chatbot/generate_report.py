"""Create the assignment PDF report with ReportLab."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "College_Helpdesk_Chatbot_Report.pdf"

INK = colors.HexColor("#17243a")
BLUE = colors.HexColor("#1d4ed8")
PALE_BLUE = colors.HexColor("#eef4ff")
PALE_GRAY = colors.HexColor("#f4f6fa")
MID_GRAY = colors.HexColor("#64748b")
GREEN = colors.HexColor("#166534")

WELCOME = (
    "Hello! I'm the GMIU College Helpdesk Bot. Ask me about admissions, fees, "
    "timetables, examinations, results, the library, scholarships, holidays, "
    "hostel, or contact information."
)

ADMISSIONS = (
    "Admissions dates and eligibility can change by program and academic year. "
    "Please confirm the latest notice with GMIU's official admissions portal "
    "or admissions office."
)
FEES = (
    "Fee amounts and payment deadlines vary by program and academic year. For "
    "the current fee structure, check the official GMIU fee notice or contact "
    "the accounts office. I don't have verified current figures."
)
TIMETABLE = (
    "Timetables can differ by department, semester, and section. Check your "
    "department's official timetable notice or student portal for the current "
    "schedule."
)
EXAMS = (
    "Exam dates and instructions may change. Please check the latest "
    "examination notice on GMIU's official student portal or contact the "
    "examination office."
)
RESULTS = (
    "Results are published through the official student or examination "
    "portal. Please verify there; I can't access personal result records."
)
LIBRARY = (
    "For library hours, catalogue access, borrowing limits, and renewals, "
    "check the library notice or contact GMIU's library staff."
)
SCHOLARSHIP = (
    "Scholarship eligibility, deadlines, and available schemes vary. Check "
    "the latest official scholarship notice and confirm details with the "
    "scholarship or financial aid office."
)
HOLIDAYS = (
    "Holiday schedules are set by the university and may change. Refer to the "
    "current academic calendar or an official college notice."
)
HOSTEL = (
    "Hostel availability, fees, rules, and application dates can change. "
    "Confirm current details directly with the hostel or administration "
    "office."
)
CONTACT = (
    "For verified phone numbers and email addresses, use the contact "
    "information listed on GMIU's official website or contact your department "
    "office. I don't want to guess an official number."
)
GREETING = "Hello! What would you like to know about GMIU?"
THANKS = "You're welcome! Let me know if you have another college helpdesk question."
GOODBYE = "Goodbye! I hope you find the information you need."
UNKNOWN = (
    "I'm not sure about that question yet. Please rephrase it or contact the "
    "relevant GMIU department through an official college channel."
)

SAMPLES = [
    ("Hello", GREETING),
    ("How do I apply for admission?", ADMISSIONS),
    ("What are the current fees?", FEES),
    ("Where can I see the timetable?", TIMETABLE),
    ("When are the examinations?", EXAMS),
    ("How do I check my result?", RESULTS),
    ("Can I borrow books from the library?", LIBRARY),
    ("What scholarship information is available?", SCHOLARSHIP),
    ("How do I apply for a hostel?", HOSTEL),
    ("When are holidays?", HOLIDAYS),
    ("How can I contact the college?", CONTACT),
    ("Thank you", THANKS),
]

TESTS = [
    ("How do I apply for admission?", "Admissions guidance; verify current dates/eligibility.", "PASS"),
    ("What are the current fees?", "Official fee notice/accounts office; no unverified amount.", "PASS"),
    ("Where can I see the timetable?", "Check the department notice or student portal.", "PASS"),
    ("When are the examinations?", "Check the official examination notice/office.", "PASS"),
    ("How do I check my result?", "Use the official portal; no personal result access.", "PASS"),
    ("Can I borrow books from the library?", "Check library notice/staff for current rules.", "PASS"),
    ("What scholarship information is available?", "Check official scholarship notice/office.", "PASS"),
    ("How do I apply for a hostel?", "Confirm current details with hostel/administration office.", "PASS"),
    ("When are holidays?", "Check the current academic calendar or official notice.", "PASS"),
    ("How can I contact the college?", "Use verified official website/department contact details.", "PASS"),
    ("", "Ask the user to type a question.", "PASS"),
    ("What is the moon made of?", "Unknown-question response; rephrase or contact the relevant office.", "PASS"),
]


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=31,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=9 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=12,
            leading=18,
            alignment=TA_CENTER,
            textColor=MID_GRAY,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeadingCustom",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=BLUE,
            spaceBefore=5 * mm,
            spaceAfter=2.5 * mm,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubHeadingCustom",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=14,
            textColor=INK,
            spaceBefore=3 * mm,
            spaceAfter=1.5 * mm,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=13.5,
            textColor=INK,
            spaceAfter=2.3 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.5,
            leading=10.5,
            textColor=INK,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeCustom",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=7.3,
            leading=10,
            leftIndent=2 * mm,
            rightIndent=2 * mm,
            borderColor=colors.HexColor("#d8e1ef"),
            borderWidth=0.5,
            borderPadding=5,
            backColor=PALE_GRAY,
            spaceBefore=1.5 * mm,
            spaceAfter=3 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeadCustom",
            parent=styles["SmallCustom"],
            fontName="Helvetica-Bold",
            textColor=colors.white,
        )
    )
    return styles


def P(text, style):
    """Create a paragraph and escape XML-sensitive user-facing text."""
    from xml.sax.saxutils import escape

    return Paragraph(escape(text).replace("\n", "<br/>"), style)


def bullet(text, style):
    return Paragraph("•&nbsp;&nbsp;" + text, style)


def make_table(rows, widths, header=True, font_size=7.5):
    table = Table(rows, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8e1ef")),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
    ]
    if header:
        commands.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), INK),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ]
        )
    if len(rows) > (1 if header else 0):
        start = 1 if header else 0
        for row_index in range(start, len(rows)):
            if (row_index - start) % 2 == 1:
                commands.append(("BACKGROUND", (0, row_index), (-1, row_index), PALE_GRAY))
    table.setStyle(TableStyle(commands))
    return table


def footer(canvas, doc):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(colors.HexColor("#d8e1ef"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 15 * mm, width - 18 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MID_GRAY)
    canvas.drawString(18 * mm, 10 * mm, "College Helpdesk Rule-Based Chatbot")
    canvas.drawRightString(width - 18 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def make_report():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=21 * mm,
        title="College Helpdesk Rule-Based Chatbot",
        author="Student assignment",
    )
    story = []

    # Cover page
    story.extend([Spacer(1, 20 * mm), P("GYANMANJRI INNOVATIVE UNIVERSITY", styles["CoverSubtitle"])])
    story.extend(
        [
            Spacer(1, 12 * mm),
            P("College Helpdesk<br/>Rule-Based Chatbot", styles["CoverTitle"]),
            P("Python and Streamlit Assignment Report", styles["CoverSubtitle"]),
            Spacer(1, 17 * mm),
        ]
    )
    details = [
        [P("Student name", styles["BodyCustom"]), P("________________________________________", styles["BodyCustom"])],
        [P("Enrollment number", styles["BodyCustom"]), P("________________________________________", styles["BodyCustom"])],
        [P("Subject", styles["BodyCustom"]), P("________________________________________", styles["BodyCustom"])],
        [P("College", styles["BodyCustom"]), P("Gyanmanjri Innovative University (GMIU)", styles["BodyCustom"])],
        [P("GitHub repository URL", styles["BodyCustom"]), P("________________________________________", styles["BodyCustom"])],
        [P("Live chatbot URL", styles["BodyCustom"]), P("________________________________________", styles["BodyCustom"])],
    ]
    cover_table = Table(details, colWidths=[48 * mm, 112 * mm], hAlign="CENTER")
    cover_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#cbd5e1")),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8e1ef")),
                ("BACKGROUND", (0, 0), (0, -1), PALE_BLUE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    story.extend([cover_table, Spacer(1, 20 * mm)])
    story.append(
        P(
            "Submitted as an academic project demonstrating a transparent, "
            "rule-based conversational interface.",
            styles["CoverSubtitle"],
        )
    )
    story.append(PageBreak())

    # 1. Introduction and objectives
    story.append(P("1. Introduction", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "A college helpdesk chatbot can guide students toward information "
            "about common administrative and academic topics. This project "
            "implements a small, explainable chatbot in Python. It identifies "
            "keywords in a student's message and returns a predefined response "
            "using conditional statements. A Streamlit interface displays the "
            "conversation in a browser.",
            styles["BodyCustom"],
        )
    )
    story.append(
        P(
            "The chatbot is an educational demonstration, not an official "
            "GMIU information system. It does not have access to student "
            "records and avoids making up current fees, dates, phone numbers, "
            "or policies.",
            styles["BodyCustom"],
        )
    )
    story.append(P("2. Objectives", styles["SectionHeadingCustom"]))
    for text in [
        "Build a working rule-based chatbot in Python.",
        "Use keyword matching and explicit if, elif, and else conditions.",
        "Provide fixed answers for ten college helpdesk topic groups and common social messages.",
        "Create a clear, responsive chat interface with examples and a clear-chat option.",
        "Direct students to official college sources when a fact may change or is not verified.",
    ]:
        story.append(bullet(text, styles["BodyCustom"]))

    # 3. Tools and technologies
    story.append(P("3. Tools and Technologies", styles["SectionHeadingCustom"]))
    tech_rows = [
        [P("Tool", styles["TableHeadCustom"]), P("Use in this project", styles["TableHeadCustom"])],
        [P("Python", styles["SmallCustom"]), P("Implements keyword matching and response selection.", styles["SmallCustom"])],
        [P("Streamlit", styles["SmallCustom"]), P("Creates the interactive browser-based chat interface.", styles["SmallCustom"])],
        [P("Regular expressions (re)", styles["SmallCustom"]), P("Normalizes text and matches complete keywords.", styles["SmallCustom"])],
        [P("ReportLab", styles["SmallCustom"]), P("Generates this PDF assignment report.", styles["SmallCustom"])],
    ]
    story.append(make_table(tech_rows, [44 * mm, 116 * mm]))
    story.append(
        P(
            "The chatbot's answer logic runs locally in the application process. "
            "It does not call an external AI API or machine-learning model.",
            styles["BodyCustom"],
        )
    )

    # 4. Logic and algorithm
    story.append(P("4. Rule-Based Chatbot Logic", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "The program first normalizes the message by converting it to "
            "lowercase, removing punctuation, and collapsing repeated spaces. "
            "It then checks the normalized message against keyword groups. "
            "Each branch is an if or elif condition; the first matching branch "
            "returns its fixed response. The final else branch handles "
            "questions that do not match any known pattern. Empty text has its "
            "own first condition.",
            styles["BodyCustom"],
        )
    )
    story.append(
        P(
            "The matching order puts helpdesk topics before greetings. For "
            "example, “Hi, what are the fees?” should reach the fee rule rather "
            "than stop at a greeting rule.",
            styles["BodyCustom"],
        )
    )
    story.append(P("Algorithm", styles["SubHeadingCustom"]))
    algorithm = (
        "START\n"
        "  Read the user's message\n"
        "  Normalize text (lowercase; remove punctuation)\n"
        "  IF message is empty: ask for a question\n"
        "  ELIF admission keywords match: show admissions guidance\n"
        "  ELIF fee keywords match: direct to official fee notice/accounts office\n"
        "  ELIF another supported topic matches: show its fixed response\n"
        "  ELIF greeting / thanks / goodbye matches: show social response\n"
        "  ELSE: show the unknown-question response\n"
        "  Display response in the chat\n"
        "END"
    )
    story.append(P(algorithm, styles["CodeCustom"]))
    story.append(P("Simplified decision flow", styles["SubHeadingCustom"]))
    flow_rows = [
        [P("User message", styles["TableHeadCustom"]), P("Normalize", styles["TableHeadCustom"]), P("Keyword branch", styles["TableHeadCustom"]), P("Fixed answer", styles["TableHeadCustom"])],
        [P("Typed or clicked example", styles["SmallCustom"]), P("Lowercase + punctuation removed", styles["SmallCustom"]), P("First matching if/elif rule", styles["SmallCustom"]), P("Displayed in chat", styles["SmallCustom"])],
    ]
    story.append(make_table(flow_rows, [36 * mm, 38 * mm, 44 * mm, 42 * mm]))

    # 5. Important source code
    story.append(P("5. Important Parts of the Source Code", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "The actual project contains the complete matching rules and interface. "
            "This short excerpt demonstrates the main conditional structure:",
            styles["BodyCustom"],
        )
    )
    snippet = (
        "if not text:\n"
        "    return \"Please type a question, and I'll try to help.\"\n"
        "elif has_keyword(text, (\"admission\", \"admissions\", \"application\", \"enroll\")):\n"
        "    return RESPONSES[\"admissions\"]\n"
        "elif has_keyword(text, (\"fee\", \"fees\", \"tuition\", \"payment\")):\n"
        "    return RESPONSES[\"fees\"]\n"
        "else:\n"
        "    return (\n"
        "        \"I'm not sure about that question yet. Please rephrase it or contact \"\n"
        "        \"the relevant GMIU department through an official college channel.\"\n"
        "    )"
    )
    story.append(P(snippet, styles["CodeCustom"]))
    story.append(
        P(
            "The helper function has_keyword checks for a complete word or "
            "phrase, reducing accidental matches such as finding “hi” inside "
            "a longer unrelated word. Streamlit stores conversation messages "
            "in session state so they remain visible across interface reruns.",
            styles["BodyCustom"],
        )
    )

    # 6. Sample conversations
    story.append(P("6. Sample Conversations", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "The following bot messages match the predefined response strings "
            "in app.py. The sample includes more than the required seven "
            "conversations.",
            styles["BodyCustom"],
        )
    )
    sample_rows = [
        [P("User question", styles["TableHeadCustom"]), P("Chatbot response", styles["TableHeadCustom"])]
    ]
    for question, response in SAMPLES:
        sample_rows.append([P(question, styles["SmallCustom"]), P(response, styles["SmallCustom"])])
    story.append(make_table(sample_rows, [50 * mm, 110 * mm]))

    # 7. Test table
    story.append(P("7. Testing", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "The rule function was checked against representative prompts, "
            "including blank and unrecognized input. PASS means the returned "
            "answer matched the intended response category and avoided "
            "fabricating official information.",
            styles["BodyCustom"],
        )
    )
    test_rows = [
        [P("Test input", styles["TableHeadCustom"]), P("Expected response", styles["TableHeadCustom"]), P("Result", styles["TableHeadCustom"])]
    ]
    for question, expected, result in TESTS:
        test_rows.append(
            [
                P(question if question else "(blank input)", styles["SmallCustom"]),
                P(expected, styles["SmallCustom"]),
                P(result, styles["SmallCustom"]),
            ]
        )
    story.append(make_table(test_rows, [43 * mm, 95 * mm, 22 * mm]))

    # 8. Pros, limitations and next steps
    story.append(P("8. Advantages", styles["SectionHeadingCustom"]))
    for text in [
        "Simple and explainable: each response is linked to a visible keyword rule.",
        "Fast and lightweight: no model, database, API key, or paid AI service is required.",
        "Predictable: the same normalized question follows the same matching order.",
        "Safer handling of changing college details: uncertain facts are referred to official sources.",
    ]:
        story.append(bullet(text, styles["BodyCustom"]))

    story.append(P("9. Limitations", styles["SectionHeadingCustom"]))
    for text in [
        "The chatbot recognizes only keywords and phrases included in its rules.",
        "It cannot understand context, paraphrases it has not been taught, or follow-up intent like a conversational AI model.",
        "Its fixed answers do not contain live schedules, fee amounts, admissions status, or personal student results.",
        "A message containing multiple topics follows the first matching topic according to the rule order.",
    ]:
        story.append(bullet(text, styles["BodyCustom"]))

    story.append(P("10. Future Improvements", styles["SectionHeadingCustom"]))
    for text in [
        "Add more tested keywords and alternate phrasings based on common student questions.",
        "Use a reviewed, versioned FAQ dataset with an administrator update process.",
        "Add multilingual responses and accessible interface improvements.",
        "Add optional feedback controls and report which questions were not recognized, without collecting private student information.",
    ]:
        story.append(bullet(text, styles["BodyCustom"]))

    # 11. Conclusion
    story.append(P("11. Conclusion", styles["SectionHeadingCustom"]))
    story.append(
        P(
            "This project demonstrates how a basic rule-based chatbot can "
            "answer common college helpdesk questions through keyword matching "
            "and if/elif/else conditions. The Streamlit interface makes the "
            "program easy to try in a browser. Since college information can "
            "change, the chatbot avoids unsupported official claims and directs "
            "students to GMIU's official notices and offices for verification.",
            styles["BodyCustom"],
        )
    )
    story.append(P("12. Repository and Live App", styles["SectionHeadingCustom"]))
    links_rows = [
        [P("GitHub repository URL", styles["SmallCustom"]), P("_______________________________________________________________", styles["SmallCustom"])],
        [P("Live chatbot URL", styles["SmallCustom"]), P("_______________________________________________________________", styles["SmallCustom"])],
    ]
    story.append(make_table(links_rows, [50 * mm, 110 * mm], header=False))
    story.append(Spacer(1, 4 * mm))
    story.append(
        P(
            "Fill in these fields only after creating the repository and "
            "successfully deploying the application. Do not submit example or "
            "guessed URLs as real links.",
            styles["SmallCustom"],
        )
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    make_report()
