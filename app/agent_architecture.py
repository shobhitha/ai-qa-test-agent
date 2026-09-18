"""
QA Agent

Acts as the QA-specific orchestration layer.
Takes a software requirement, builds a QA-focused prompt,
and uses the LLM client to analyze the requirement.
"""

from app.llm_client import LLMClient

class QAAgent:

    def __init__(self):
        self.llm = LLMClient()

    def analyze_requirement(self,requirement):

        prompt = f"""
            
            You are a senior QA Engineer. Analyse the following software requirement.
            
            Identify:
            1. Positive scenarios
            2. Negative scenarios
            3. Edge cases
            
            Requirement:
            {requirement}
            """
        return self.llm.generate(prompt)