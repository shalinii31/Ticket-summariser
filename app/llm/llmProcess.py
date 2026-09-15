from app.llm.prompt import build_prompt
from app.llm.llm_config import llm
from app.history import add_to_history


def llm_processing(query: str) -> str:
    prompt = build_prompt(query=query)
    response = llm.invoke(prompt)
    add_to_history("user", query)
    add_to_history("assistant", response)
    print("diagnostic: ", response)
    return response.content