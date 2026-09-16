import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def test_openai_connection():
    api_key = os.getenv("OPENAI_API_KEY")

    assert api_key, "OPENAI_API_KEY was not found."

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model = "gpt-5.6-luna",
        input = "Say hello and confirm that you are connected to the OpenAI API."

    )
    print(response.output_text)
    assert response.output_text

def test_generate_testcases():
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key, "OPENAI_API_KEY was not found."
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model = "gpt-5.6-luna",
        input = """
        You are a QA engineer.
        Give me 5 negative test cases for a login page.
        Keep each test case concise."""
    )



    assert (response.output_text ,"The API returned empty output.")

    print(response.output_text)



