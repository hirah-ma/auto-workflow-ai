from crewai import Agent
from tools.gmail_tools import GmailTool
from tools.sheets_tools import SheetsTool
from tools.calendar_tools import CalendarTool
from tools.notion_tools import NotionTool
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
llm = ChatGoogleGenerativeAI(
    
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

gmail_tool = GmailTool()
sheets_tool = SheetsTool()
calendar_tool = CalendarTool()
notion_tool = NotionTool()

mailer_agent = Agent(
    role="Mailer Agent",
    goal="Send emails based on user input",
    backstory="An expert email assistant using Gmail API.",
    tools=[gmail_tool],
    verbose=True,
    llm=llm
)

sheet_agent = Agent(
    role="Sheet Logger Agent",
    goal="Log updates in Google Sheets",
    backstory="Logs data and tasks in Google Sheets accurately.",
    tools=[sheets_tool],
    verbose=True,
    llm=llm
)

scheduler_agent = Agent(
    role="Scheduler Agent",
    goal="Fetch events and send WhatsApp reminders",
    backstory="Checks calendar and reminds users.",
    tools=[calendar_tool],
    verbose=True,
    llm=llm
)

notion_agent = Agent(
    role="Notion Writer Agent",
    goal="Write structured content in Notion",
    backstory="Keeps structured notes in Notion workspace.",
    tools=[notion_tool],
    verbose=True,
    llm=llm
)

coordinator_agent = Agent(
    role="Coordinator Agent",
    goal="Coordinate task execution from a user prompt",
    backstory="Understands prompts and orchestrates actions.",
    tools=[gmail_tool, sheets_tool, calendar_tool, notion_tool],
    verbose=True,
    llm=llm
)

all_agents = [mailer_agent, sheet_agent, scheduler_agent, notion_agent, coordinator_agent]