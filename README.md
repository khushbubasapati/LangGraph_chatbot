# Chatbot Application using LangGraph, LangChain, LangSmith & Hugging Face

A production-ready chatbot built using **LangGraph**, **LangChain**, **LangSmith**, **Hugging Face models**, and a **Streamlit UI**. The system supports **tool use**, including a custom **RAG tool**, real-time **streaming responses**, and persistent memory using **SQLiteSaver**.

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

### 🔹 RAG (Retrieval-Augmented Generation)

* Document ingestion and embedding generation.
* Retrieval using vector database for context-aware responses.

### 🔹 Tools Implementation

Includes a variety of tools:

* RAG tool for knowledge retrieval
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
├── langgraph_chatbot.py       # LangGraph workflow
├── memory/                 # SQLiteSaver setup
├── data/                   # Documents for RAG
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

## 📚 RAG Pipeline

1. Load documents
2. Generate embeddings
3. Store in vector DB
4. Retrieve top-k docs
5. Inject into LLM context

---

## 🛠️ Tools Implemented

* **RAGTool** – retrieves context
* **Search or API tools (optional)**
* **Math/Utility tools**
* **Any custom workflow-specific tools**

---




