# Phase 4 — Agent Architecture

**Status:** Complete
**Previous Phase:** [Phase 3 — Basic LLM Test Generator](./03-basic-llm-test-generator.md)
**Next Phase:** Phase 5 — Agent Tools

---

## 1. Objective

In Phase 3, the project evolved from a simple OpenAI API connection into a reusable LLM-powered application.

The application could send a prompt to an LLM and receive a response.

The architecture was:

```text
Requirement
     ↓
Prompt
     ↓
LLMClient
     ↓
OpenAI API
     ↓
LLM
     ↓
Response
```

In Phase 4, we introduce an **AI QA agent layer**.

The goal is to separate:

* LLM communication
* QA-specific logic
* Application orchestration

The architecture becomes:

```text
Requirement
     ↓
QAAgent
     ↓
LLMClient
     ↓
OpenAI API
     ↓
LLM
     ↓
QA Response
```

This phase establishes the architectural foundation for the more advanced agent capabilities that will be added in later phases.

---

# 2. Why Introduce an Agent Layer?

In Phase 3, `LLMClient` was responsible for communicating with the LLM.

However, the LLM client should not contain QA-specific responsibilities.

For example, we don't want `LLMClient` to contain methods such as:

```text
generate_login_test_cases()
review_checkout_tests()
generate_playwright_tests()
analyze_api_requirements()
```

Those are application-level QA responsibilities.

Instead, we separate the responsibilities.

### LLMClient

Responsible for:

```text
How do we communicate with the LLM?
```

### QAAgent

Responsible for:

```text
What QA task should we ask the LLM to perform?
```

This separation makes the application easier to extend.

---

# 3. Architecture

The Phase 4 architecture is:

```text
┌──────────────────────────────┐
│           QAAgent            │
│                              │
│  QA-specific responsibilities│
│                              │
│  analyze_requirement()       │
└──────────────┬───────────────┘
               │
               │ generate(prompt)
               ▼
┌──────────────────────────────┐
│          LLMClient           │
│                              │
│  API configuration           │
│  OpenAI communication        │
│  Response extraction         │
└──────────────┬───────────────┘
               │
               ▼
        ┌─────────────┐
        │  OpenAI API │
        └──────┬──────┘
               │
               ▼
              LLM
```

---

# 4. Project Structure

After Phase 4, the project structure is:

```text
ai-qa-test-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   └── llm_client.py
│
├── tests/
│   ├── test_openai.py
│   ├── test_llm_client.py
│   └── test_agent.py
│
├── docs/
│   ├── 00-project-overview.md
│   ├── 01-project-setup.md
│   ├── 02-openai-api-connection.md
│   ├── 03-basic-llm-test-generator.md
│   └── 04-agent-architecture.md
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 5. Creating the QA Agent

New file:

```text
app/agent.py
```

Implementation:

```python
from app.llm_client import LLMClient


class QAAgent:

    def __init__(self):
        self.llm = LLMClient()

    def analyze_requirement(self, requirement):

        prompt = f"""
You are a senior QA engineer.

Analyze the following software requirement.

Identify:
1. Positive test scenarios
2. Negative test scenarios
3. Edge cases
4. Missing or ambiguous requirements

Requirement:
{requirement}

Provide a concise, structured response.
"""

        return self.llm.generate(prompt)
```

---

# 6. Understanding the Implementation

## Import `LLMClient`

```python
from app.llm_client import LLMClient
```

The QA agent uses the reusable LLM client created in Phase 3.

The agent does not directly create an OpenAI API connection.

This maintains separation between application logic and API communication.

---

## Create the `QAAgent` class

```python
class QAAgent:
```

The class represents the AI-powered QA component of the application.

The class provides a place where QA-related capabilities can be added over time.

For example:

```text
QAAgent
│
├── analyze_requirement()
├── generate_test_cases()
├── review_test_cases()
└── generate_playwright_tests()
```

The current implementation contains only the first capability.

---

# 7. Constructor

```python
def __init__(self):
    self.llm = LLMClient()
```

When a `QAAgent` object is created:

```python
agent = QAAgent()
```

the constructor creates an `LLMClient`.

The relationship is:

```text
QAAgent
   │
   └── LLMClient
```

The agent can therefore use the LLM through:

```python
self.llm
```

---

# 8. Requirement Analysis

The first agent capability is:

```python
def analyze_requirement(self, requirement):
```

The method accepts a software requirement.

Example:

```text
Users should be able to log into the application
using a valid username and password.
```

The requirement is passed into the agent:

```python
agent.analyze_requirement(requirement)
```

This makes the agent reusable for different requirements.

---

# 9. Prompt Construction

The agent constructs a QA-specific prompt:

```python
prompt = f"""
You are a senior QA engineer.

Analyze the following software requirement.

Identify:
1. Positive test scenarios
2. Negative test scenarios
3. Edge cases
4. Missing or ambiguous requirements

Requirement:
{requirement}

Provide a concise, structured response.
"""
```

The prompt provides the LLM with:

* Role/context
* Task
* Expected categories
* User requirement
* Output guidance

The requirement is dynamically inserted using a Python f-string.

---

# 10. Why Include Negative and Edge Cases?

A QA system should not only consider the happy path.

For example, given:

```text
Users should be able to log in using
a valid username and password.
```

A QA analysis should consider:

### Positive scenarios

```text
Valid username + valid password
```

### Negative scenarios

```text
Invalid username
Invalid password
Empty username
Empty password
Both fields empty
```

### Edge cases

```text
Very long username
Special characters
Leading/trailing spaces
Maximum password length
```

### Requirement gaps

```text
What happens after multiple failed attempts?
Is the account locked?
What are the password requirements?
```

This helps the agent behave more like a QA analysis tool rather than simply generating generic text.

---

# 11. Calling the LLM

The final line is:

```python
return self.llm.generate(prompt)
```

The QA agent sends the prompt to `LLMClient`.

The flow is:

```text
QAAgent
   │
   │ generate(prompt)
   ▼
LLMClient
   │
   ▼
OpenAI API
   │
   ▼
LLM
   │
   ▼
Generated response
```

The `QAAgent` does not need to know the details of the OpenAI API.

---

# 12. Separation of Responsibilities

This is one of the most important design decisions in Phase 4.

### `QAAgent`

Owns:

```text
QA-specific logic
Prompt construction
QA workflow
```

### `LLMClient`

Owns:

```text
API authentication
OpenAI client creation
API communication
Response extraction
```

### Tests

Own:

```text
Validation of application behavior
```

The architecture can therefore be represented as:

```text
┌───────────────────────┐
│       QAAgent         │
│                       │
│   What should AI do?  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      LLMClient        │
│                       │
│ How do we call AI?    │
└───────────┬───────────┘
            │
            ▼
       OpenAI API
```

---

# 13. Testing the Agent

Create:

```text
tests/test_agent.py
```

Test:

```python
from app.project_setup import QAAgent


def test_agent_analyzes_requirement():
    agent = QAAgent()

    result = agent.analyze_requirement(
        """
        Users should be able to log into the application
        using a valid username and password.
        """
    )

    assert result
```

The test verifies that the agent can:

1. Initialize
2. Accept a requirement
3. Generate a prompt
4. Call the LLM
5. Return a non-empty response

---

# 14. Running the Test

Run:

```bash
pytest -v -s tests/test_agent.py
```

Expected result:

```text
============================= test session starts =============================

tests/test_agent.py::test_agent_analyzes_requirement PASSED

============================== 1 passed ==============================
```

The `-s` option allows printed output to appear in the terminal if the test contains `print()` statements.

---

# 15. Running the Complete Test Suite

After the agent test passes, run:

```bash
pytest -v
```

The existing tests should continue to pass.

This is important because adding a new component should not break existing functionality.

The project is now developing into a small layered application rather than a collection of independent experiments.

---

# 16. Complete Execution Flow

For a requirement such as:

```text
Users should be able to log into the application
using a valid username and password.
```

the execution flow is:

```text
1. User Requirement
          ↓
2. QAAgent
          ↓
3. Build QA Prompt
          ↓
4. LLMClient
          ↓
5. OpenAI API
          ↓
6. LLM
          ↓
7. Generated Response
          ↓
8. LLMClient
          ↓
9. QAAgent
          ↓
10. Application Result
```

---

# 17. Is This a Fully Autonomous AI Agent?

Not yet.

This distinction is important.

The current Phase 4 implementation is an **agent-oriented orchestration layer around an LLM**.

The workflow is still predetermined:

```text
analyze_requirement()
        ↓
build prompt
        ↓
call LLM
        ↓
return response
```

The system does not yet independently decide which tools to use or what action to perform next.

A more capable agent might follow a loop such as:

```text
Goal
 ↓
Decide action
 ↓
Use tool
 ↓
Observe result
 ↓
Decide next action
 ↓
Use another tool
 ↓
Final result
```

That capability will be introduced progressively in later phases.

---

# 18. Why Not Build a Multi-Agent System Immediately?

Many AI tutorials introduce several agents immediately:

```text
Requirement Agent
Test Agent
Review Agent
Automation Agent
```

This project intentionally starts simpler.

The goal is to understand each architectural layer before adding complexity.

The progression is:

```text
LLM
 ↓
LLM Application
 ↓
Agent Layer
 ↓
Tools
 ↓
Evaluation
 ↓
Automation
```

This makes the system easier to understand, test, debug, and explain during interviews.

---

# 19. Concepts Learned

## Abstraction

`LLMClient` hides the implementation details of communicating with the LLM.

The agent only needs:

```python
self.llm.generate(prompt)
```

---

## Separation of Concerns

Different components have different responsibilities:

```text
QAAgent → QA logic

LLMClient → LLM communication

Tests → Validation
```

---

## Composition

`QAAgent` contains an `LLMClient`:

```python
self.llm = LLMClient()
```

This is an example of composing one component from another rather than duplicating functionality.

---

## Prompt Construction

The agent dynamically constructs prompts based on the software requirement.

---

## Application Architecture

The project is beginning to move from a simple script/test into a layered application:

```text
Application Layer
       ↓
LLM Communication Layer
       ↓
External AI Service
```

---



# 21. Portfolio Perspective

The project has now progressed through four important stages:

```text
Phase 1
Project Setup
      ↓
Phase 2
OpenAI API Connection
      ↓
Phase 3
Reusable LLM Client
      ↓
Phase 4
QA Agent Architecture
```

This demonstrates an incremental engineering approach.

Instead of starting with a complex AI framework, the project first established:

1. A working Python environment
2. API connectivity
3. A reusable LLM abstraction
4. An application-level QA agent

The architecture is now ready for additional capabilities.

---

# 22. Validation Checklist

Before committing Phase 4, verify:

* [ ] `app/agent.py` exists
* [ ] `QAAgent` initializes successfully
* [ ] `QAAgent` uses `LLMClient`
* [ ] Requirement can be passed into `analyze_requirement()`
* [ ] QA-specific prompt is generated
* [ ] LLM returns a response
* [ ] `tests/test_agent.py` passes
* [ ] Complete test suite passes
* [ ] No API key is hard-coded
* [ ] `.env` is not committed
* [ ] Changes are visible in `git status`

Run:

```bash
pytest -v
```

Then:

```bash
git status
```

---

# 23. Git Commit

Once all tests pass:

```bash
git add .
```

Commit the Phase 4 changes:

```bash
git commit -m "Add QA agent architecture"
```

Push to GitHub:

```bash
git push origin main
```

Verify the commit appears in the GitHub repository.

---

# 24. What Comes Next?

## Phase 5 — Agent Tools

The next phase will introduce an important capability:

**Tools.**

Currently:

```text
QAAgent
    ↓
LLM
    ↓
Response
```

In Phase 5, we will begin moving toward:

```text
                    QAAgent
                       │
             ┌─────────┼─────────┐
             ↓         ↓         ↓
         Analyzer   Generator   Reviewer
             │         │         │
             └─────────┼─────────┘
                       ↓
                     Tools
```

The agent will eventually be able to use capabilities such as:

```text
Requirement analysis
Test generation
Test validation
File operations
Playwright generation
```

This is where the project will start moving from a simple LLM application toward a more capable **AI QA agent**.

---

## Phase 4 Summary

The key idea from this phase is:

```text
QAAgent = What the AI system should accomplish

LLMClient = How the application communicates with the LLM
```

Keeping those responsibilities separate gives us a clean foundation for the next stages of the project.

**Phase 4 Complete → Phase 5: Agent Tools**
