import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(requirement:str) -> str:

    prompt = f"""
You are an experienced software QA engineer.

Analyze the following software requirement:

{requirement}

Generate:

1. Functional test scenarios
2. Negative test scenarios
3. Edge cases
4. Test data considerations

Present the result in a clear, structured format."""

    response = client.responses.create(
        model="gpt-5.6",
        input=prompt
    )

    return response.output_text

if __name__ == "__main__":
    requirement = """
    A user should be able to reset their password
    using their registered email address.
    """

    result = generate_test_cases(requirement)
    print(result)


