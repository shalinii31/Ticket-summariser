def build_prompt(
        query: str
        
) -> str:

    prompt = f"""

    you are a ticket summariser assistant.
    you understand the query of customer and summarise it into two lines 
    you do not answer any other questions.

   user query:
   {query}
    """

    return prompt
