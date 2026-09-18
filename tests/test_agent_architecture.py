"""
QA Agent Tests

Tests the QAAgent's ability to analyze a software requirement
and return an LLM-generated QA response.
"""


from app.agent_architecture import QAAgent

def test_agent_analyzes_requirement():
    agent = QAAgent()

    result = agent.analyze_requirement(
        """
        Users should be able to log into the application
        using a valid username and password.
        """
    )
    print("\n AI response")
    print(result)
    assert result