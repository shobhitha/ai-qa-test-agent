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
