from app.llm_client import LLMClient

def test_llm_generates_response():
    llm = LLMClient()

    response = llm.generate(
        "Give me 5 negative test cases for a login page."

    )
    print("\nAI Response:")
    print(response)

    assert response
