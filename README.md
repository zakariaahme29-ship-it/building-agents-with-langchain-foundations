# 🤖 Building Agents with LangChain Foundations

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Integration-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Advanced-orange)
![Status](https://img.shields.io/badge/Status-Active_Daily_Updates-brightgreen)

## 📖 Overview
Welcome to my technical log and advanced guide on LLM orchestration! This repository serves as a foundational 3-stage curriculum, documenting hands-on experience building complex, production-ready AI agent architectures using **LangGraph** and **LangChain**.

This is not just a collection of working code; it is a deep dive into **real-world implementation, debugging, and advanced state management**. For every concept, I document the common pitfalls, architectural bottlenecks, and the exact debugging steps required to solve them.

## 🗺️ Curriculum & Stages

### 🟢 Stage 1: Agent Foundations & Hierarchies (Current Focus)
**Goal:** Master tool calling and multi-agent delegation.
* **Concepts:** Building a Supervisor agent that delegates tasks to specialized sub-agents.
* **Debugging Focus:** Resolving `coroutine` errors and handling third-party API rate limits.

### 🟡 Stage 2: Memory & State Management (Coming Soon)
**Goal:** Optimize the LLM context window for cost and accuracy.
* **Concepts:** Shared memory, `SummarizationMiddleware`, and message trimming.
* **Debugging Focus:** Preventing LLM context overflow and filtering out raw `ToolMessage` clutter.

### 🔴 Stage 3: Production-Ready Control Flow (Coming Soon)
**Goal:** Implement safe, dynamic, and human-supervised automation.
* **Concepts:** Human-in-the-Loop (HITL), Dynamic Model Routing, and Dynamic Prompt Injection.
* **Debugging Focus:** Managing `thread_id` continuity and resolving `AttributeError` in context schemas.

## 🚀 Getting Started
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/building-agents-with-langchain-foundations.git](https://github.com/YourUsername/building-agents-with-langchain-foundations.git)
   cd building-agents-with-langchain-foundations