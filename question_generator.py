import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Initialize LLM model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def generate_questions(data_summary):
    """
    Generates questions about the dataset using OpenAI's GPT-3.5 model.

    Args:
        data_summary (str): Textual summary of the dataset.

    Returns:
        str: Generated questions.
    """
    # Define the prompt template
    prompt_template = ChatPromptTemplate.from_template(
        "You are a data analyst. Based on the following data summary, "
        "generate meaningful questions to explore this data:\n\n"
        "{summary}\n\n"
        "Output a list of questions."
    )

    # Format the prompt
    prompt = prompt_template.format(summary=data_summary)

    # Get response from the model
    response = llm.generate([prompt])
    
    # Return the text content of the response
    return response.generations[0][0].text.strip()
