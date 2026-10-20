# GMIU College Helpdesk Rule-Based Chatbot

A beginner-friendly Python assignment project: a Streamlit chat interface backed by keyword matching and predefined responses. It uses ordinary `if`, `elif`, and `else` conditions—no external AI API, machine-learning model, or paid answer-generation service.

> **Accuracy note:** The chatbot does not invent GMIU fees, deadlines, contact numbers, or policies. For information that changes, it directs students to the relevant official GMIU notice, portal, or office.

## Files

- `app.py` — chatbot logic and responsive Streamlit interface.
- `requirements.txt` — the Python package required to run the app.
- `College_Helpdesk_Chatbot_Report.pdf` — assignment report with the explanation, algorithm, sample chats, and test table.
- `generate_report.py` — optional helper to regenerate the PDF report.

## Features

- Answers about admissions, fees, timetables, examinations, results, library, scholarships, holidays, hostel, and contact information.
- Handles greetings, thanks, goodbye, blank input, and unknown questions.
- Uses transparent keyword matching and predefined responses.
- Includes clickable example questions, chat history, and a clear-chat button.
- Displays a reminder to verify current college information through official channels.
- Runs without a database, API key, or external AI service.

## Requirements

- Python 3.11 or newer (matches the current Streamlit package requirement; Community Cloud's documentation currently lists Python 3.12 as its default).
- Internet access for the first-time package installation.

## Install and run

Open a terminal in this folder and run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install dependencies and start Streamlit:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit prints a local address in the terminal (usually `http://localhost:8501`). Open it in a browser. Stop the local server with `Ctrl+C`.

## Test the app

Try each of these:

1. `How do I apply for admission?`
2. `What are the current fees?`
3. `Where can I see the timetable?`
4. `When are the examinations?`
5. `How do I check my result?`
6. `Can I borrow books from the library?`
7. `What scholarship information is available?`
8. `How can I contact the college?`
9. `Thank you`
10. `Tell me something unrelated`

Confirm the bot gives the relevant predefined answer, does not make up official facts, and that **Clear chat** returns the conversation to its welcome message. The report contains a test table and sample conversations that use the same response text as `app.py`.

## Screenshots

Add screenshots of the running application here before submitting. Suggested images:

- `screenshots/chat-home.png` — welcome screen and example questions.
- `screenshots/chat-answer.png` — one question and its response.

To capture them, run the app locally, open it in a browser, and use your operating system's screenshot tool. Do not include real student records in screenshots.

## Upload the files to GitHub

1. Sign in to GitHub and choose **New repository**.
2. Give it a clear name, such as `gmiu-college-helpdesk-chatbot`.
3. Choose **Public** if your instructor needs to open it without signing in; otherwise choose the visibility your instructor requests.
4. Create the repository. Do not add a README if you are uploading this existing folder with its own README.
5. In the new repository, choose **Add file → Upload files**.
6. Upload `app.py`, `requirements.txt`, `README.md`, `College_Helpdesk_Chatbot_Report.pdf`, and `generate_report.py`. Keep the app file at the repository root unless you plan to enter a subfolder as the app path during deployment.
7. Add a clear commit message such as `Add college helpdesk chatbot assignment`.
8. Click **Commit changes**.
9. Open the repository page and copy its address. Put that real address in the report's **GitHub repository URL** field. Do not write a guessed URL.

Alternatively, from a terminal inside this folder:

```bash
git init
git add app.py requirements.txt README.md College_Helpdesk_Chatbot_Report.pdf generate_report.py
git commit -m "Add college helpdesk chatbot assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the two placeholders with your actual GitHub username and repository name. The command is a template; it is not a real repository URL until you create the repository and push successfully.

## Deploy on Streamlit Community Cloud

Streamlit Community Cloud's official deployment guide describes choosing a GitHub repository, branch, and app entrypoint, then deploying it to a `streamlit.app` subdomain. Availability and account requirements can change; check the current service prompts before submitting.

1. Push the project to GitHub as described above.
2. Sign in at [share.streamlit.io](https://share.streamlit.io/) using GitHub and authorize access to the repository if prompted.
3. Choose **Create app**, then select the repository, branch (usually `main`), and entrypoint file (`app.py`).
4. Optionally choose an available app subdomain, then select **Deploy**.
5. Wait for the app to build and open the URL shown by Community Cloud. Copy that exact public URL into the report's **Live chatbot URL** field. A URL is not real until the deployment completes and the app opens.
6. Test the public page in a private/incognito browser window: try an example question, type a question, check the unknown-question response, and clear the chat.
7. If deployment fails, inspect the app's build logs. Confirm `app.py` and `requirements.txt` are in the selected repository path and that the entrypoint is correct.

Official instructions: [Deploy your app on Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).

## Updating the PDF

The report generator is optional. To recreate the PDF after editing its content:

```bash
python -m pip install reportlab
python generate_report.py
```

Review the student details and URLs in the PDF before submitting. They are intentionally left blank.

## Academic note

Read the code and report and adapt them to your instructor's rubric. Be prepared to explain the keyword lists, the `if`/`elif`/`else` flow, and the limits of fixed responses.
