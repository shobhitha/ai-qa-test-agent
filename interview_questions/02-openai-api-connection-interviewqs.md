## 16. Interview Preparation

### What is the OpenAI Python SDK?

> The OpenAI Python SDK is the official Python client library for interacting with the OpenAI API. It provides a Python interface for creating API requests and working with typed API responses.

### Why use an SDK instead of making HTTP requests directly?

> The SDK abstracts much of the lower-level API communication and provides a convenient Python interface, typed request parameters, and structured response objects.

### What is the purpose of the `OpenAI` client?

> The `OpenAI` client provides the interface through which the Python application communicates with OpenAI's API.

### What does this code do?

```python
client = OpenAI(api_key=api_key)
```

> It initializes the OpenAI client using the API credential loaded from the environment.

### What does this do?

```python
client.responses.create(...)
```

> It sends a request to the Responses API with the specified model and input.

### What is `response`?

> It is a structured response object returned by the API. It contains the model output and other response information.

### What is `response.output_text`?

> It is a convenient property provided by the SDK for accessing the generated textual output from the response.

### Is this an AI agent?

> Not yet. At this stage, it is an LLM-powered application that sends an input to a model and receives a response. The agent architecture will be introduced later with decision-making, tools, and workflow orchestration.

---