from dotenv import load_dotenv
import os

load_dotenv()

print("Gemini Key:", os.getenv("GOOGLE_API_KEY"))
print("Notion Token:", os.getenv("NOTION_TOKEN"))
print("Notion Page ID:", os.getenv("NOTION_PAGE_ID"))