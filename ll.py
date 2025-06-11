print("✅ This is ll.py being run")
from langchain_google_genai import ChatGoogleGenerativeAI

print("Starting...")  # Debug print

llm = ChatGoogleGenerativeAI(model="gemini-pro")
response = llm.invoke("Say hello.")

print("Response object:", response)
print("Response content:", response.content)
