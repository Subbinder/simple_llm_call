# 10.	Use GPT-4o to explain Cloud Computing and its types.

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

prompt = PromptTemplate.from_template(
    template="Explain Cloud Computing and its types."
)

response = llm.invoke(prompt.format())
print(response.content)
