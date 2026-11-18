import os
from crewai import Agent, LLM

def get_llm():
    model = os.getenv("OLLAMA_MODEL", "ollama/llama3.2")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    return LLM(
        model=model,
        base_url=base_url,
        temperature=0.3,
    )

def build_agents():
    llm = get_llm()
    analyst = Agent(
        role="Job Role Analyst",
        goal="Interpret the role, seniority, skills, and hiring context accurately.",
        backstory="You are an experienced talent acquisition analyst who turns hiring inputs into clear role requirements.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
    jd_writer = Agent(
        role="Job Description Specialist",
        goal="Write a realistic, inclusive, structured job description using only the supplied hiring context.",
        backstory="You are a technical recruiter skilled at writing clear job descriptions for candidates.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
    technical_expert = Agent(
        role="Technical Interview Designer",
        goal="Create relevant technical interview questions with concise expected-answer guidance.",
        backstory="You are a senior technical interviewer who evaluates practical skill, reasoning, and role readiness.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
    hr_expert = Agent(
        role="HR Interview Designer",
        goal="Create fair behavioral and HR interview questions relevant to the role and experience level.",
        backstory="You are an HR professional who designs structured, job-related interviews.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
    return analyst, jd_writer, technical_expert, hr_expert
