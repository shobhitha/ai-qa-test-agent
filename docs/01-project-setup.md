# Phase 1 — Project Setup

> **Status:** ✅ Complete
> **Phase:** 1 of 11
> **Previous:** [Project Overview](./00-project-overview.md)
> **Next:** [OpenAI API Connection](./02-openai-api-connection.md)

---

## 📌 Objective

Establish the development foundation for the **AI QA Test Agent**.

In this phase, we:

* Created the GitHub repository
* Set up the Python project
* Created an isolated virtual environment
* Established the project structure
* Installed initial dependencies
* Configured environment variables
* Protected sensitive credentials
* Set up Git version control
* Established the documentation structure for future phases

---

## 🏗️ Initial Project Structure

```text
ai-qa-test-agent/
│
├── app/
│   └── __init__.py
│
├── tests/
│
├── docs/
│   ├── 00-project-overview.md
│   └── 01-project-setup.md
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The project structure will evolve as new capabilities are added.

---

# 1. Python Environment

## Create Virtual Environment

```bash
python3 -m venv .venv
```

## Activate Virtual Environment

```bash
source .venv/bin/activate
```

A successful activation displays `(.venv)` in the terminal prompt.

### Why?

A virtual environment isolates project dependencies from:

* The system Python installation
* Other Python projects
* Different versions of the same package

This helps prevent dependency conflicts and makes the project easier to reproduce.

---

# 2. Project Dependencies

The initial dependencies are:

| Package         | Purpose                                 |
| --------------- | --------------------------------------- |
| `openai`        | Communicate with the OpenAI API         |
| `python-dotenv` | Load environment variables from `.env`  |
| `pydantic`      | Validate and structure application data |

Install them with:

```bash
pip install openai python-dotenv pydantic
```

Save the dependencies:

```bash
pip freeze > requirements.txt
```

### Why `requirements.txt`?

It allows another developer to recreate the project's Python environment without manually determining which packages are required.

---

# 3. Environment Variables

The application will require an OpenAI API key.

The API key should **never be hardcoded in source code**.

Instead, use a local `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

### `.env`

Contains the actual local secret.

```text
.env
```

This file must remain local and must **not** be committed to GitHub.

### `.env.example`

The repository contains:

```text
OPENAI_API_KEY=
```

This provides a safe template showing developers which environment variables are required.

---

# 4. Git Security

The `.gitignore` file contains:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

### Why these files are ignored

| File / Directory | Reason                                 |
| ---------------- | -------------------------------------- |
| `.env`           | May contain API keys and other secrets |
| `.venv/`         | Local Python virtual environment       |
| `__pycache__/`   | Python-generated cache files           |
| `*.pyc`          | Python compiled files                  |

> ⚠️ **Security Rule:** Never commit an API key, password, token, or other secret to GitHub.

---

# 5. Verify Git Status

Before committing:

```bash
git status
```

The actual `.env` file should **not** appear in the files to be committed.

Expected files include:

```text
.env.example
.gitignore
README.md
requirements.txt
app/
tests/
docs/
```

If `.env` appears, stop and fix `.gitignore` before committing.

---

# 6. Git Workflow

The project follows this basic workflow:

```text
        Make Changes
             │
             ▼
        git status
             │
             ▼
         git diff
             │
             ▼
          git add
             │
             ▼
        git commit
             │
             ▼
         git push
             │
             ▼
          GitHub
```

### Check changes

```bash
git status
git diff
```

### Stage changes

```bash
git add .
```

### Commit

```bash
git commit -m "Set up AI QA agent project"
```

### Push

```bash
git push origin main
```

---

# 7. What Gets Committed?

### ✅ Commit

```text
README.md
docs/
app/
tests/
.gitignore
.env.example
requirements.txt
```

### ❌ Do NOT commit

```text
.env
.venv/
__pycache__/
*.pyc
```

---

# 8. Documentation Strategy

Each major development phase has its own documentation.

```text
docs/
│
├── 00-project-overview.md
├── 01-project-setup.md
├── 02-openai-api-connection.md
├── 03-basic-llm-test-generator.md
├── 04-agent-architecture.md
├── 05-agent-tools.md
├── 06-test-reviewer.md
├── 07-playwright-generator.md
├── 08-web-ui.md
├── 09-testing-and-evaluation.md
├── 10-github-actions.md
└── 11-deployment.md
```

This provides a chronological record of how the application evolved.

Each phase will document:

1. **Objective**
2. **Implementation**
3. **Technical concepts**
4. **Design decisions**
5. **Validation**
6. **Git commit**
7. **Interview preparation**
8. **Next phase**

---

# 9. Key Concepts Learned

### Virtual Environment

An isolated Python environment used to manage project-specific dependencies.

```bash
python3 -m venv .venv
```

---

### Python Packages

Reusable libraries that provide functionality without requiring us to implement everything from scratch.

---

### Environment Variables

Configuration values stored outside the application's source code.

Example:

```text
OPENAI_API_KEY
```

---

### `.env`

Local configuration file containing actual environment values.

**Not committed to GitHub.**

---

### `.env.example`

Safe template that documents required environment variables.

**Committed to GitHub.**

---

### `.gitignore`

Specifies files and directories Git should not track.

---

### Git

A version-control system used to track changes to the project.

### GitHub

A remote platform used to host and collaborate on Git repositories.

---

# 10. Validation Checklist

Before marking Phase 1 complete:

* [x] GitHub repository created
* [x] Repository configured as public
* [x] Project cloned locally
* [x] Python virtual environment created
* [x] Virtual environment activated
* [x] `app/` directory created
* [x] `tests/` directory created
* [x] `docs/` directory created
* [x] `.gitignore` created
* [x] `.env.example` created
* [x] Local `.env` created
* [x] `openai` installed
* [x] `python-dotenv` installed
* [x] `pydantic` installed
* [x] `requirements.txt` generated
* [x] API key excluded from source code
* [x] `.env` excluded from Git
* [x] Phase 1 documentation created

---

12. Portfolio Perspective

Phase 1 establishes the engineering foundation rather than demonstrating the final AI capabilities.

The project will progressively demonstrate:

Python
  │
  ▼
OpenAI API
  │
  ▼
LLM Application
  │
  ▼
AI Agent
  │
  ▼
Agent Tools
  │
  ▼
AI Evaluation
  │
  ▼
Playwright Automation
  │
  ▼
Web Interface
  │
  ▼
CI/CD
  │
  ▼
Deployment

The goal is to demonstrate the ability to design, build, test, document, version, and deploy an AI-powered QA application.

13. Phase 1 Git Commit
Commit Message
Set up AI QA agent project
Commit Command
git add .
git commit -m "Set up AI QA agent project"
git push origin main

14. Completion

Phase 1 is complete when:

The project structure exists
Dependencies are installed
Environment variables are configured
Secrets are protected
Documentation is committed
The repository is pushed to GitHub
➡️ Next Phase
Phase 2 — OpenAI API Connection

In the next phase, the Python application will communicate with the OpenAI API.

The initial architecture will be:

Python Application
        │
        ▼
OpenAI Python SDK
        │
        ▼
OpenAI API
        │
        ▼
GPT Model
        │
        ▼
Response
        │
        ▼
Python Application

The goal is to establish and understand this connection before building the AI-powered QA functionality.
