# 🟡 Stage 2: Memory & State Management

Welcome to Stage 2! As our agents grow more complex, managing the conversation history (state) becomes critical. LLMs have finite context windows, and passing raw, unfiltered conversation logs (especially massive tool outputs) will quickly lead to API errors, hallucinations, and high costs.

In this module, we move beyond simple prompt-response loops and implement robust memory management architectures using LangGraph.

## 🗂️ Notebooks in this Stage
*(Notebooks will be added here as we progress through the module)*

## 🧠 Key Concepts Covered

### 1. StateGraphs & Shared Memory
* **Concept:** Transitioning from stateless agents to `StateGraph` architectures where the agent can persistently read and write to a shared memory object across multiple invocations.

### 2. Message Trimming
* **Concept:** Implementing techniques to strategically drop older or less relevant messages from the context window to prevent context overflow.

### 3. Summarization Middleware
* **Concept:** Instead of dropping messages entirely, we use a lightweight LLM to summarize past interactions, retaining the core context while freeing up valuable token space.

## 🐛 Bug Log & Resolutions

### 1. Context Window Overflow & Memory Pollution
**The Problem:** Unfiltered `ToolMessage` outputs (like raw HTML from a web search or massive JSON payloads) flood the LLM's context window.
**The Fix:** Implementing programmatic filters and summarization nodes to clean and compress tool outputs *before* they are appended to the graph's main state.