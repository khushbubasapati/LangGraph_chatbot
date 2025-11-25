from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

response = chat.invoke([HumanMessage(content="What is LangChain?")])

print(response.content)
