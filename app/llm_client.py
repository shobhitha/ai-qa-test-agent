import os

from dotenv import load_dotenv
from openai import OpenAI

from app.agent import client

load_dotenv()

class LLMClient:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt):
            response = self.client.responses.create(
                model = "gpt-5.6-luna",
                input = prompt
            )

            return response.output_text

