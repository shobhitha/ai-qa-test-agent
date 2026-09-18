# Phase 3 — Basic LLM Test Generator

**Status:** Complete
**Previous Phase:** [Phase 2 — OpenAI API Connection](./02-openai-api-connection.md)
**Next Phase:** Phase 4 — Agent Architecture

---

## 1. Objective

In Phase 2, the project successfully connected Python to the OpenAI API and verified that an LLM could generate a response.

In Phase 3, the goal is to turn that API connection into a **reusable application component** that can be used to generate QA-related content.

The application will take a software requirement and use an LLM to generate test cases.

### Example

**Input requirement:**

```text
The user should be able to log into the application
using a valid username and password.
```

**Expected type of output:**

```text
1. Verify login with a valid username and password.
2. Verify login with an invalid username.
3. Verify login with an invalid password.
4. Verify login with an empty username.
5. Verify login with an empty password.
6. Verify login with both username and password empty.
```

The purpose of this phase is not to build a sophisticated AI agent yet.

The purpose is to learn how to build a simple, reusable **LLM-powered application**.

---

# 2. Architecture

### Phase 2

The API call was directly inside the test:

```text
Test
 │
 ▼
OpenAI API
 │
 ▼
LLM
```

This was sufficient for proving that the API connection worked.

However, application logic should not live inside test files.

### Phase 3

We introduce an application layer:

```text
                 APPLICATION
                      │
                      ▼
              ┌───────────────┐
              │ llm_client.py │
              └───────┬───────┘
                      │
                      ▼
                 OpenAI API
                      │
                      ▼
                    LLM
                      │
                      ▼
                  Response


                    TESTS
                      │
                      ▼
             test_llm_client.py
```

The important change is **separation of responsibilities**.

---

# 3. Project Structure

After Phase 3, the relevant project structure is:

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
│   └── test_llm_client.py
│
├── docs/
│   ├── 00-project-overview.md
│   ├── 01-project-setup.md
│   ├── 02-openai-api-connection.md
│   └── 03-basic-llm-test-generator.md
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 4. Why Create `llm_client.py`?

In Phase 2, the test itself handled several responsibilities:

* Reading the API key
* Creating the OpenAI client
* Sending the API request
* Reading the response
* Validating the response

That approach does not scale well.

For example, later our application may have:

```text
Requirement Analyzer
Test Generator
Test Reviewer
Playwright Generator
```

All of these components may need to communicate with an LLM.

We don't want each component to contain its own OpenAI API setup.

Instead, we create one reusable component:

```text
LLMClient
```

Its responsibility is:

> Communicate with the LLM and return the generated response.

---

# 5. Implementing `LLMClient`

File:

```text
app/llm_client.py
```

Implementation:

```python
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLMClient:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY was not found.")

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt):
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return response.output_text
```

---

# 6. Understanding the Code

## Import dependencies

```python
import os

from dotenv import load_dotenv
from openai import OpenAI
```

We use:

* `os` to access environment variables
* `python-dotenv` to load values from `.env`
* `OpenAI` from the OpenAI Python SDK to communicate with the API

---

## Load environment variables

```python
load_dotenv()
```

This loads values from the project's `.env` file.

For example:

```text
OPENAI_API_KEY=your_actual_key
```

The API key is therefore kept outside the Python source code.

---

# 7. Creating the `LLMClient` Class

```python
class LLMClient:
```

The class provides a reusable interface for communicating with the LLM.

Instead of writing:

```python
client = OpenAI(...)
```

throughout the application, other components can simply use:

```python
llm = LLMClient()
```

and then:

```python
llm.generate(prompt)
```

This is an example of **abstraction**.

The application does not need to know all the details of how the OpenAI client is configured.

---

# 8. API Key Validation

Inside the constructor:

```python
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY was not found.")
```

This provides an early and clear failure if the API key is missing.

Instead of receiving an unclear API error later, the application immediately tells us what is wrong.

---

# 9. Creating the OpenAI Client

```python
self.client = OpenAI(api_key=api_key)
```

The OpenAI Python SDK client is created once when the `LLMClient` object is initialized.

The client is then stored as:

```python
self.client
```

so it can be reused by the `generate()` method.

---

# 10. Generating an LLM Response

The main method is:

```python
def generate(self, prompt):
```

It accepts a prompt from the application.

The API request is then made:

```python
response = self.client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)
```

The generated text is returned:

```python
return response.output_text
```

Therefore, the application can interact with the LLM using a simple interface:

```python
response = llm.generate(prompt)
```

---

# 11. Why Return `response.output_text`?

The OpenAI API returns a structured response object.

We are interested in the generated text, so we use:

```python
response.output_text
```

This keeps the rest of our application simple.

Instead of requiring every component to understand the structure of the API response, `LLMClient` handles that detail.

The flow becomes:

```text
OpenAI API
     ↓
Structured Response
     ↓
LLMClient
     ↓
response.output_text
     ↓
Application
```

---

# 12. Testing the LLM Client

Create:

```text
tests/test_llm_client.py
```

Test code:

```python
from app.llm_client import LLMClient


def test_llm_generates_response():

    llm = LLMClient()

    response = llm.generate(
        "Give me 5 negative test cases for a login page."
    )

    assert response
```

We can optionally print the response while learning:

```python
print("\nAI Response:")
print(response)
```

---

# 13. Running the Test

Run:

```bash
pytest -v -s tests/test_llm_client.py
```

Expected result:

```text
============================= test session starts =============================

tests/test_llm_client.py::test_llm_generates_response PASSED

============================== 1 passed ==============================
```

The `-s` option allows us to see the generated response printed by the test.

---

# 14. What Happens During the Test?

The complete flow is:

```text
pytest
  │
  ▼
test_llm_generates_response()
  │
  ▼
LLMClient()
  │
  ├── Load API key
  │
  └── Create OpenAI client
  │
  ▼
llm.generate(prompt)
  │
  ▼
OpenAI Responses API
  │
  ▼
LLM
  │
  ▼
Generated response
  │
  ▼
response.output_text
  │
  ▼
assert response
```

This is our first reusable LLM application component.

---

# 15. Separation of Responsibilities

One of the most important concepts learned in this phase is **separation of concerns**.

### `LLMClient`

Responsible for:

```text
API authentication
API communication
LLM request
LLM response extraction
```

### Test

Responsible for:

```text
Calling the application
Validating the result
```

### Future `TestGenerator`

Will be responsible for:

```text
QA-specific prompt
Requirement processing
Test case generation
```

This gives us a cleaner architecture:

```text
Requirement
     │
     ▼
TestGenerator
     │
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
Generated Test Cases
```

---

# 16. Important Design Decision

We intentionally do **not** put QA-specific logic inside `LLMClient`.

For example, we don't want:

```python
class LLMClient:

    def generate_login_test_cases(self, requirement):
        ...
```

because the LLM client should not be responsible for knowing about login testing, API testing, checkout testing, etc.

Instead, it should remain generic:

```python
llm.generate(prompt)
```

This means the same client can eventually support:

```text
Test Case Generation
Requirement Analysis
Test Review
Bug Analysis
Playwright Code Generation
```

---

# 17. Concepts Learned

### 1. Abstraction

We hide the OpenAI API implementation behind:

```python
LLMClient
```

The rest of the application only needs:

```python
llm.generate(prompt)
```

---

### 2. Separation of Concerns

Different components have different responsibilities.

```text
LLMClient → LLM communication

TestGenerator → QA logic

Tests → Validation
```

---

### 3. Reusable Components

Instead of creating an OpenAI client repeatedly throughout the application, we created a reusable class.

---

### 4. Application vs. Test Code

Phase 2 used the test to prove connectivity.

Phase 3 moves reusable functionality into:

```text
app/
```

while keeping validation inside:

```text
tests/
```

---

### 5. Prompt as Input

The LLM receives a prompt as an input:

```python
llm.generate(prompt)
```

This allows our application to dynamically construct prompts later.

---

# 18. Why This Is Not an AI Agent Yet

It is important to understand this distinction for interviews.

At this stage, the application is essentially:

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output
```

There is no:

* planning
* tool selection
* iterative reasoning loop
* state management
* multi-step execution

Therefore, this is an **LLM-powered application**, not yet an AI agent.

The agent architecture will be introduced in a later phase.

---

# 19. Validation Checklist

Before moving to Phase 4, verify:

* [ ] `app/llm_client.py` exists
* [ ] `.env` contains the API key
* [ ] `.env` is ignored by Git
* [ ] `LLMClient` successfully initializes
* [ ] OpenAI API request succeeds
* [ ] `response.output_text` contains text
* [ ] `test_llm_client.py` passes
* [ ] No API key is hard-coded
* [ ] No API key is committed to GitHub

Run:

```bash
git status
```

Make sure `.env` is **not** listed as a file to commit.

---

# 20. Interview Preparation

### Question: Why did you create an `LLMClient` class?

**Answer:**

> I created an abstraction layer around the OpenAI Python SDK so that LLM communication is separated from the QA-specific application logic. This makes the LLM functionality reusable across components such as test generation, test review, and automation generation.

---

### Question: Why shouldn't the OpenAI API call be inside the test?

**Answer:**

> The test should validate application behavior rather than contain the application's implementation. I moved the reusable API communication into `LLMClient` and kept the test responsible for invoking and validating that component.

---

### Question: What is the responsibility of `LLMClient`?

**Answer:**

> `LLMClient` is responsible for loading the API configuration, creating the OpenAI client, sending prompts through the Responses API, and returning the generated text to the application.

---

### Question: Is this an AI agent?

**Answer:**

> Not yet. At this stage it is an LLM-powered application. It accepts a prompt and returns an LLM response. In the next stages, I will introduce agent behavior such as task decomposition, tool usage, and multi-step execution.

---

### Question: Why separate `LLMClient` from `TestGenerator`?

**Answer:**

> `LLMClient` handles how we communicate with the LLM, while `TestGenerator` handles what we ask the LLM to do from a QA perspective. This separation keeps the architecture modular and makes it easier to add other LLM-powered capabilities later.

---

# 21. Portfolio Perspective

At the end of Phase 3, the project has progressed from simply testing an API connection to having a reusable LLM application component.

The progression is:

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
Agent Architecture
```

This progression demonstrates an important engineering principle:

> Start with a simple working component, understand it, and then progressively add architecture and intelligence.

---

# 22. Git Commit

Once the Phase 3 implementation and tests are working:

```bash
git status
```

Then:

```bash
git add .
```

Commit:

```bash
git commit -m "Build basic LLM test generator"
```

Push:

```bash
git push origin main
```

Verify the commit appears on GitHub.

---

# 23. Next Phase

## Phase 4 — Agent Architecture

In the next phase, we will move beyond a simple:

```text
Prompt → LLM → Response
```

and start designing the application as an **AI QA agent**.

The architecture will begin evolving toward:

```text
Requirement
     ↓
Requirement Analysis
     ↓
Scenario Generation
     ↓
Test Case Generation
     ↓
Review
     ↓
Automation
```

We will first understand **what makes an application an agent** before implementing the more advanced architecture.

---

**Phase 3 Complete → Phase 4 Next**
