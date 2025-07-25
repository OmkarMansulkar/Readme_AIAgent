# Readme_AIAgent
Here’s a sample `README.md` for your Agentic AI project:

---

#  Agentic AI for Auto-README Generation

This project implements an **Agentic AI system** that autonomously reads all Python files in a given project directory and generates a summarized `README.md` file using a powerful LLM (e.g., Meta LLaMA 4 Scout 17B via Groq API).

##  Features

*  **Autonomous Agent Loop**: Uses an LLM to reason, plan, and act in iterative cycles.
*  **File Listing & Reading**: Automatically detects and reads all `.py` files.
*  **README Generation**: Summarizes the project structure, purpose, and functionality into a clean, readable README.
*  **Tool-Driven Execution**: Modular tools for listing files, reading contents, writing README, and termination.

## Tools Implemented

* `list_project_files()` – Lists all Python files.
* `read_project_file(name)` – Reads contents of a given `.py` file.
* `write_readme(content)` – Writes the final `README.md`.
* `terminate(message)` – Stops the agent loop with a message.

## Tech Stack

* **Python 3.10+**
* **Meta LLaMA 4 Scout (17B)** via **Groq API**
* **LiteLLM** for API routing and abstraction
* **Agent Loop** and prompt-chaining logic

## Setup

```bash
pip install lite_llm
export GROQ_API_KEY=your_key_here
python run_agent.py
```

##  How It Works

1. The user gives a high-level goal: *“Write a README for this project.”*
2. The AI agent decides on actions like:

   * Listing `.py` files
   * Reading key scripts
   * Writing a summarized README
3. The agent runs tools autonomously in a loop until the task is complete.

##  Output

* A clean and contextually accurate `README.md` summarizing:

  * Project purpose
  * Modules and features
  * Setup and usage

## Future Improvements

* Code summarization per file
* Class/function-level documentation
* UI for uploading repos
