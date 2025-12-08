# Chatbot Application using LangGraph, LangChain, LangSmith & Hugging Face

A production-ready chatbot built using **LangGraph**, **LangChain**, **LangSmith**, **Hugging Face models**, and a **Streamlit UI**. The system supports **tool use**, real-time **streaming responses**, and persistent memory using **SQLiteSaver**.

---

## 🚀 Features

### 🔹 LangGraph Workflow

* Modular graph-based architecture for better control over agent flow.
* Custom nodes for LLM interaction, RAG, memory, and tool execution.

### 🔹 LangChain Integration

* Chains and tools integrated seamlessly.
* SQLiteSaver used for storing conversation history and memory.

### 🔹 Hugging Face Model Support

* Pluggable architecture to use various HF text-generation models.
* Works with both local and API-based models.

### 🔹 Deployment on Hugging Face Spaces

* Deployed on Hugging Face Spaces with Streamlit UI.
* Accessible publicly with full streaming and tool support.
* Ideal for demonstrations and real-time interaction.

### 🔹 Tools Implementation

Includes a variety of tools:

* Search tool (DuckDuckGoSearch)
* Calculator tool
* get_stock_price tool

### 🔹 Real-Time Streaming

* Implemented token-by-token streaming in Streamlit using async callbacks.

### 🔹 Streamlit UI

* Clean, interactive interface for chatting with the model.
* Displays streaming output.
* Supports session persistence.

### 🔹 SQLiteSaver Memory

* Stores previous conversation state.
* Allows agent to maintain context between turns.

---

## 🏗️ Project Structure

```
├── app.py                  # Streamlit frontend
├── langgraph_chatbot.py    # LangGraph workflow
├── chatbot.db              # SQLiteSaver database
└── README.md               # Project documentation
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

Make sure you have the necessary Hugging Face tokens/config if required.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## ⚡ How It Works

### 1. User sends a query from Streamlit.

### 2. Query flows through LangGraph:

* Memory → LLM → Tools → RAG (if needed)
* Uses LangChain wrappers & utilities

### 3. Streaming callback returns tokens to UI.

### 4. SQLiteSaver stores conversation for persistence.

---

## 🛠️ Tools Implemented

* **Search or API tools (optional)**
* **Math/Utility tools**
* **Any custom workflow-specific tools**

---

### 🚀 Deployment on Hugging Face Spaces

* This chatbot is deployed on Hugging Face Spaces using Streamlit for an interactive web-based experience.

* 🔗 Live Demo: https://huggingface.co/spaces/khushbu-basapati/langgraph_chatbot



