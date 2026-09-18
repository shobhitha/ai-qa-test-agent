# 20. Interview Preparation

### Question: Why did you introduce a `QAAgent` class?

**Answer:**

> I introduced the QAAgent as an application-level orchestration layer. It contains QA-specific responsibilities such as requirement analysis and prompt construction, while the LLMClient remains responsible for communication with the OpenAI API.

---

### Question: Why separate `QAAgent` and `LLMClient`?

**Answer:**

> I wanted to separate the business or QA logic from the infrastructure logic. LLMClient handles how the application communicates with the LLM, while QAAgent determines what QA task the LLM should perform.

---

### Question: Why not call OpenAI directly from `QAAgent`?

**Answer:**

> Directly calling OpenAI from the agent would couple the QA logic to the API implementation. By using LLMClient as an abstraction layer, the agent remains focused on QA functionality and the communication layer can be changed independently.

---

### Question: Is your Phase 4 implementation an autonomous agent?

**Answer:**

> It is an agent-oriented architecture, but it is not yet a fully autonomous tool-using agent. The current workflow is predetermined. Later phases will introduce tools and more dynamic orchestration.

---

### Question: What is the benefit of this architecture?

**Answer:**

> It provides separation of concerns and makes the system easier to extend. I can add capabilities such as test generation, test review, and Playwright generation without duplicating the LLM communication code.

---