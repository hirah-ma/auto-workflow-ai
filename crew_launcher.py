from crewai import Crew, Process
from agents import all_agents
from tasks import example_task

crew = Crew(
    agents=all_agents,
    tasks=[example_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={"topic": "AI Workflow"})
print(result)