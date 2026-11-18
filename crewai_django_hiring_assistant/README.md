# CrewAI + Django Hiring Assistant

A fresh Django application that uses a sequential CrewAI workflow and a local Ollama model to generate:
- A job description
- Technical interview questions with answer guidance
- HR / behavioral interview questions with evaluation guidance

## Requirements
- Python 3.10–3.13 (use Python 3.11 or 3.12 for the smoothest dependency compatibility)
- Ollama installed and running
- Enough RAM for the selected local model

## Windows PowerShell setup

```powershell
cd path\to\crewai_django_hiring_assistant
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
ollama pull llama3.2
```

Start Ollama in a separate PowerShell window if it is not already running:

```powershell
ollama serve
```

Test that the model responds:

```powershell
ollama run llama3.2
```

Exit the Ollama chat with `/bye`.

Then in the project terminal:

```powershell
python manage.py check
python manage.py makemigrations assistant
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Workflow
1. Register a user account.
2. Sign in and choose **Generate**.
3. Enter job title, skills, experience level, and optional details.
4. Submit. CrewAI runs four agents in sequence: analyst, job description writer, technical interviewer, and HR interviewer.
5. Results are saved to SQLite and shown on the result page.
6. Revisit previous outputs from the dashboard.

## Configuration
Edit `.env`:
- `OLLAMA_MODEL=ollama/llama3.2`
- `OLLAMA_BASE_URL=http://localhost:11434`

If Ollama is on another machine or port, update the base URL accordingly.

## Important notes
- The first generation may take several minutes while the local model loads.
- Keep Ollama running while using the site.
- This is a development starter. Before deployment, set `DEBUG=False`, use a strong secret key, configure HTTPS, use a production database, and add request timeouts/background jobs for long-running generations.
- AI-generated descriptions and questions must be reviewed by a human recruiter. Do not use the output as an automated hiring decision or to rank candidates.
- Do not commit `.env` or `db.sqlite3` to Git.
