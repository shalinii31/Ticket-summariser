from app.llm.prompt import build_prompt
from app.llm.llm_config import llm


def llm_processing(query: str) -> str:
    prompt = build_prompt(query=query)
    response = llm.invoke(prompt)
    print("diagnostic: ", response)
    return response.content