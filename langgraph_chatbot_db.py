from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated,Literal
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = HuggingFaceEndpoint(repo_id = "meta-llama/Llama-3.2-1B-Instruct")
model = ChatHuggingFace(llm = llm)
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]
    
def chat_node(state:ChatState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages":[response]}

conn = sqlite3.connect(database="chatbot_db",check_same_thread=False)
# CHECKPOINTER
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)
graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)

def retreive_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
        return list(all_threads)
  