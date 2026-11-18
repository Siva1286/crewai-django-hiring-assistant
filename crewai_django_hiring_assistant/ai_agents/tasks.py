from crewai import Task

def build_tasks(analyst, jd_writer, technical_expert, hr_expert, context_text):
    analysis = Task(
        description=(
            "Analyze this hiring request. Identify the role purpose, seniority, core skills, "
            "reasonable responsibilities, and any missing assumptions. Do not invent company-specific facts.\n\n"
            f"Hiring request:\n{context_text}"
        ),
        expected_output="A concise role analysis with core responsibilities, essential skills, and seniority expectations.",
        agent=analyst,
    )
    jd_task = Task(
        description=(
            "Using the hiring request and role analysis, create a professional job description. "
            "Include role summary, responsibilities, required skills, preferred skills if justified, "
            "and experience expectations. Avoid discriminatory or unrelated criteria. Do not invent salary, "
            "company benefits, or employer details.\n\n"
            f"Hiring request:\n{context_text}"
        ),
        expected_output="A well-formatted job description in plain text with clear headings.",
        agent=jd_writer,
        context=[analysis],
    )
    technical_task = Task(
        description=(
            "Create 10 technical interview questions for this role and experience level. "
            "Mix fundamentals, practical scenarios, and problem-solving. For each question, provide "
            "a short answer guide or evaluation points. Avoid trivia unrelated to the role.\n\n"
            f"Hiring request:\n{context_text}"
        ),
        expected_output="Ten numbered technical questions, each followed by a concise answer guide.",
        agent=technical_expert,
        context=[analysis],
    )
    hr_task = Task(
        description=(
            "Create 8 job-related HR or behavioral interview questions for this role and experience level. "
            "Include what a strong answer should demonstrate. Keep questions fair and professional.\n\n"
            f"Hiring request:\n{context_text}"
        ),
        expected_output="Eight numbered HR/behavioral questions, each followed by evaluation guidance.",
        agent=hr_expert,
        context=[analysis],
    )
    return [analysis, jd_task, technical_task, hr_task]
