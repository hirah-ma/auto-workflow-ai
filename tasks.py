from crewai import Task
from agents import mailer_agent, sheet_agent, scheduler_agent, notion_agent

example_task = Task(
    description="Demo task for coordination.",
    expected_output="Some result from tool interactions.",
    agent=mailer_agent
)