Phase 1 - Project Setup

1. Objective

Set up the foundation for the AI QA Test Agent project.

The goals of this phase are to:

Create a public GitHub repository
Set up a Python project
Create an isolated Python virtual environment
Establish a clean project structure
Install the initial dependencies
Configure environment variables
Protect sensitive information such as API keys
Establish Git and GitHub practices for the project

2. Project Repository

Repository name: ai-qa-test-agent

Project description: An AI-powered QA agent that analyzes software requirements, generates test cases, identifies edge cases, and eventually creates Playwright automation tests. 
The repository is public because this project is intended to demonstrate practical AI + QA automation skills as part of a technical portfolio.


3. Initial Project Structure

The initial project structure is:

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

The project will grow as additional functionality is implemented.

4. Python Virtual Environment

A Python virtual environment is used to isolate this project's dependencies from other Python projects and from the system Python installation.

Create the virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

When the environment is active, the terminal displays:

(.venv)

before the command prompt.

Why use a virtual environment?

Different Python projects may require different versions of packages.

For example:

Project A → package version 1.5
Project B → package version 2.0

A virtual environment prevents these dependencies from interfering with each other.

5. Initial Dependencies

The initial Python packages are:

openai
python-dotenv
pydantic

Install them with:

pip install openai python-dotenv pydantic

Save the installed dependencies:

pip freeze > requirements.txt
Purpose of each dependency
OpenAI

Provides the Python SDK used to communicate with the OpenAI API.

python-dotenv

Loads environment variables from a local .env file.

This allows sensitive configuration such as API keys to remain outside the source code.

Pydantic

Provides data validation and structured data models.

It will become more important as the agent starts producing structured QA results.

6. Environment Variables

The application will eventually require an OpenAI API key.

The API key should NOT be written directly into Python source code.

Instead, a local .env file is used.

Example:

OPENAI_API_KEY=your_api_key_here

The actual .env file is intentionally excluded from Git.

A .env.example file is included in the repository:

OPENAI_API_KEY= The purpose of .env.example is to show developers which environment variables are required without exposing sensitive values.

7. Git Security

The .gitignore file contains:

.env
.venv/
__pycache__/
*.pyc
Why?
.env

May contain API keys and other secrets. It must never be committed to a public GitHub repository.

.venv/

Contains the local Python virtual environment. It can be recreated from requirements.txt, so it does not need to be stored in Git.

__pycache__/

Contains Python-generated cache files.These are generated automatically and do not belong in source control.

*.pyc
Python compiled cache files.

8. Git Verification

Before committing, check the repository status:

git status

The actual .env file should NOT appear as an untracked file if .gitignore is configured correctly.

It is safe for the following files to appear:

.env.example
.gitignore
README.md
requirements.txt
app/
tests/
docs/

The real API key must never appear in the Git repository.

9. Documentation Strategy

This project is being built incrementally.

Each major phase will have its own documentation file.

The documentation sequence is:

00-project-overview.md
        ↓
01-project-setup.md
        ↓
02-openai-api-connection.md
        ↓
03-basic-llm-test-generator.md
        ↓
04-agent-architecture.md
        ↓
05-agent-tools.md
        ↓
06-test-reviewer.md
        ↓
07-playwright-generator.md
        ↓
08-web-ui.md
        ↓
09-testing-and-evaluation.md
        ↓
10-github-actions.md
        ↓
11-deployment.md

This allows the project to serve both as a portfolio and as a personal learning record.

10. What I Learned in Phase 1
Python Virtual Environments

A virtual environment provides an isolated environment for Python dependencies.

Command:

python3 -m venv .venv
Python Packages

Python packages provide reusable functionality.

Packages can be installed using:

pip install <package>

The project's dependencies are recorded in:

requirements.txt
Environment Variables

Environment variables allow configuration and sensitive information to be kept outside the source code.

For example:

OPENAI_API_KEY
.env vs .env.example

.env:

Contains actual local values
Should remain private
Should not be committed to GitHub

.env.example:

Contains placeholder values
Can safely be committed
Documents required configuration
.gitignore

.gitignore tells Git which files should not be tracked.

This is particularly important when working with API keys and other secrets.

Git vs GitHub

Git is the version-control system used to track changes locally.

GitHub is the remote platform where the Git repository is hosted.

The basic workflow is:

Make changes
     ↓
git status
     ↓
git add
     ↓
git commit
     ↓
git push
     ↓
GitHub
11. Validation Checklist

Before considering Phase 1 complete, verify:

GitHub repository created

Repository is public

Project cloned locally

Python virtual environment created

Virtual environment activated

app/ directory created

tests/ directory created

docs/ directory created

.gitignore created

.env.example created

Actual .env created locally

openai installed

python-dotenv installed

pydantic installed

requirements.txt generated

API key is NOT present in source code

.env is NOT being tracked by Git

Phase 1 documentation added

12. Git Commit

Once the validation checklist is complete, commit the Phase 1 work.

Check the changes:

git status

Review what will be committed:

git diff

Stage the files:

git add .

Check again:

git status

Commit:

git commit -m "Set up AI QA agent project"

Push to GitHub:

git push origin main
13. What Should Be Committed?

The following should be committed:

README.md
docs/
app/
tests/
.gitignore
.env.example
requirements.txt

The following should NOT be committed:

.env
.venv/
__pycache__/
*.pyc

Most importantly:

Never commit an actual API key.


14. Portfolio Value of Phase 1

Phase 1 by itself is not the main demonstration of AI expertise.

Its purpose is to establish professional engineering practices that will support the later AI functionality.

The more important portfolio progression will be:

Python Project
      ↓
OpenAI API
      ↓
LLM Application
      ↓
AI Agent
      ↓
Agent Tools
      ↓
Evaluation
      ↓
Playwright
      ↓
CI/CD
      ↓
Deployment

The project should demonstrate not only that I can use an AI model, but that I can build, test, document, version, and deploy an AI-powered software system.

15. Phase 1 Completion
Status

Complete when all validation items have been checked and the Git commit has been pushed successfully.

Commit
Set up AI QA agent project
Next Phase

Phase 2 — OpenAI API Connection

The next phase will establish communication between the Python application and the OpenAI API.

The expected flow will be:

Python Application
        ↓
OpenAI Python SDK
        ↓
OpenAI API
        ↓
GPT Model
        ↓
Response
        ↓
Python Application

The goal of Phase 2 is to understand and verify this connection before building the actual QA test-generation functionality.