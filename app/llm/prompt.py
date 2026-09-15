from app.history import get_history


def build_prompt(query: str) -> str:

    history = get_history()

    prompt = f"""
You are a ticket summariser assistant.

You understand the customer's query and summarise it into one line
in such a way that it can be used to create a ticket in the ticketing system.

You do not answer any other questions.

Conversation history:
{history}

Current user query:
{query}

Return only the one-line ticket summary.
"""

    return prompt