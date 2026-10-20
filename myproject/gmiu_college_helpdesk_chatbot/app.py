"""
College Helpdesk Rule-Based Chatbot

A beginner-friendly Streamlit app that answers common college helpdesk
questions with keyword matching and predefined responses. It does not use
machine learning or an external AI service.
"""

import re

import streamlit as st


# The opening message is also restored whenever the user clears the chat.
WELCOME_MESSAGE = (
    "Hello! I'm the GMIU College Helpdesk Bot. Ask me about admissions, fees, "
    "timetables, examinations, results, the library, scholarships, holidays, "
    "hostel, or contact information."
)

# All answers are deliberately general. Current fees, dates, phone numbers,
# and rules should be verified with official college sources.
RESPONSES = {
    "admissions": (
        "Admissions dates and eligibility can change by program and academic "
        "year. Please confirm the latest notice with GMIU's official admissions "
        "portal or admissions office."
    ),
    "fees": (
        "Fee amounts and payment deadlines vary by program and academic year. "
        "For the current fee structure, check the official GMIU fee notice or "
        "contact the accounts office. I don't have verified current figures."
    ),
    "timetable": (
        "Timetables can differ by department, semester, and section. Check your "
        "department's official timetable notice or student portal for the "
        "current schedule."
    ),
    "examinations": (
        "Exam dates and instructions may change. Please check the latest "
        "examination notice on GMIU's official student portal or contact the "
        "examination office."
    ),
    "results": (
        "Results are published through the official student or examination "
        "portal. Please verify there; I can't access personal result records."
    ),
    "library": (
        "For library hours, catalogue access, borrowing limits, and renewals, "
        "check the library notice or contact GMIU's library staff."
    ),
    "scholarships": (
        "Scholarship eligibility, deadlines, and available schemes vary. Check "
        "the latest official scholarship notice and confirm details with the "
        "scholarship or financial aid office."
    ),
    "holidays": (
        "Holiday schedules are set by the university and may change. Refer to "
        "the current academic calendar or an official college notice."
    ),
    "hostel": (
        "Hostel availability, fees, rules, and application dates can change. "
        "Confirm current details directly with the hostel or administration "
        "office."
    ),
    "contact": (
        "For verified phone numbers and email addresses, use the contact "
        "information listed on GMIU's official website or contact your "
        "department office. I don't want to guess an official number."
    ),
}


def normalize_text(text):
    """Lowercase text and remove punctuation to make matching predictable."""
    text = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return " ".join(text.split())


def has_keyword(text, keywords):
    """Match whole words and multi-word phrases from a keyword list."""
    for keyword in keywords:
        if " " in keyword:
            if keyword in text:
                return True
        elif re.search(r"\b" + re.escape(keyword) + r"\b", text):
            return True
    return False


def answer_question(question):
    """
    Return a predefined answer using if/elif/else rules.

    The order matters: known helpdesk topics are checked before greetings so
    that a message such as "Hi, what are the fees?" gets a useful answer.
    """
    text = normalize_text(question or "")

    if not text:
        return "Please type a question, and I'll try to help."
    elif has_keyword(text, ("admission", "admissions", "application", "enroll", "enrollment")):
        return RESPONSES["admissions"]
    elif has_keyword(text, ("fee", "fees", "tuition", "payment", "cost", "charge", "charges")):
        return RESPONSES["fees"]
    elif has_keyword(text, ("timetable", "schedule", "class timing", "lecture")):
        return RESPONSES["timetable"]
    elif has_keyword(text, ("exam", "exams", "examination", "examinations", "test", "assessment")):
        return RESPONSES["examinations"]
    elif has_keyword(text, ("result", "results", "marks", "grade", "grades", "score", "scores")):
        return RESPONSES["results"]
    elif has_keyword(text, ("library", "book", "books", "borrow", "renewal", "catalogue", "catalog")):
        return RESPONSES["library"]
    elif has_keyword(text, ("scholarship", "scholarships", "financial aid", "financial assistance")):
        return RESPONSES["scholarships"]
    elif has_keyword(text, ("holiday", "holidays", "vacation", "academic calendar")):
        return RESPONSES["holidays"]
    elif has_keyword(text, ("hostel", "dormitory", "accommodation", "residence")):
        return RESPONSES["hostel"]
    elif has_keyword(text, ("contact", "phone", "telephone", "email", "address", "office number")):
        return RESPONSES["contact"]
    elif has_keyword(text, ("hello", "hi", "hey", "good morning", "good afternoon", "good evening")):
        return "Hello! What would you like to know about GMIU?"
    elif has_keyword(text, ("thank you", "thanks", "thank")):
        return "You're welcome! Let me know if you have another college helpdesk question."
    elif has_keyword(text, ("goodbye", "bye", "see you", "good night")):
        return "Goodbye! I hope you find the information you need."
    else:
        return (
            "I'm not sure about that question yet. Please rephrase it or contact "
            "the relevant GMIU department through an official college channel."
        )


EXAMPLE_QUESTIONS = (
    "How do I apply for admission?",
    "What are the current fees?",
    "Where can I see the timetable?",
    "When are the examinations?",
    "How do I check my result?",
    "Can I borrow books from the library?",
    "What scholarship information is available?",
    "How can I contact the college?",
)


def choose_example(question):
    """Save an example question so it is handled like a typed chat message."""
    st.session_state.pending_prompt = question


def main():
    """Build and run the Streamlit chat interface."""
    st.set_page_config(
        page_title="GMIU College Helpdesk",
        page_icon="🎓",
        layout="centered",
    )

    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(180deg, #f5f8ff 0%, #ffffff 42%);
        }
        .main .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }
        [data-testid="stChatMessage"] {
            border: 1px solid #e6eaf2;
            border-radius: 16px;
            padding: 0.75rem 1rem;
            margin-bottom: 0.6rem;
            background-color: rgba(255, 255, 255, 0.92);
        }
        [data-testid="stChatInput"] {
            border-radius: 14px;
        }
        .helpdesk-note {
            color: #566176;
            font-size: 0.95rem;
            margin-top: -0.4rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🎓 GMIU College Helpdesk")
    st.markdown(
        '<p class="helpdesk-note">A simple rule-based assistant for common '
        "college questions. Please confirm changing information through "
        "official GMIU channels.</p>",
        unsafe_allow_html=True,
    )

    # Store the conversation in Streamlit's session state so it remains
    # visible while the user continues chatting.
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": WELCOME_MESSAGE}
        ]

    with st.sidebar:
        st.subheader("Chat options")
        if st.button("Clear chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": WELCOME_MESSAGE}
            ]
            st.session_state.pop("pending_prompt", None)
            st.rerun()

        st.divider()
        st.subheader("Example questions")
        for index, example in enumerate(EXAMPLE_QUESTIONS):
            st.button(
                example,
                key=f"example_{index}",
                use_container_width=True,
                on_click=choose_example,
                args=(example,),
            )

        st.caption(
            "This demo uses fixed keyword rules. It does not provide official "
            "records or personal student data."
        )

    # Show existing messages in order.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # A clicked example takes priority over a newly typed message on that run.
    typed_prompt = st.chat_input("Type your question here…")
    if typed_prompt is not None:
        prompt = typed_prompt
    else:
        prompt = st.session_state.pop("pending_prompt", None)

    if prompt is not None:
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = answer_question(prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()


if __name__ == "__main__":
    main()
