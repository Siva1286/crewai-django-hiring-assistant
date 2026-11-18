from crewai import Crew, Process
from .agents import build_agents
from .tasks import build_tasks

def generate_hiring_content(job_title, skills, experience_level, additional_details=""):
    context_text = (
        f"Job title: {job_title}\n"
        f"Required skills: {skills}\n"
        f"Experience level: {experience_level}\n"
        f"Additional details: {additional_details or 'Not provided'}"
    )

    analyst, jd_writer, technical_expert, hr_expert = build_agents()
    tasks = build_tasks(analyst, jd_writer, technical_expert, hr_expert, context_text)

    crew = Crew(
        agents=[analyst, jd_writer, technical_expert, hr_expert],
        tasks=tasks,
        process=Process.sequential,
        verbose=False,
    )
    crew.kickoff()

    # Task outputs are available after kickoff. Return plain strings for Django storage.
    return {
        "job_description": str(tasks[1].output.raw if tasks[1].output else ""),
        "technical_questions": str(tasks[2].output.raw if tasks[2].output else ""),
        "hr_questions": str(tasks[3].output.raw if tasks[3].output else ""),
    }
