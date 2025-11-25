from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated,Literal
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
llm = HuggingFaceEndpoint(repo_id = "meta-llama/Llama-3.2-1B-Instruct")
model = ChatHuggingFace(llm = llm)

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]
    
def chat_node(state:ChatState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages":[response]}

# CHECKPOINTER
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)



  