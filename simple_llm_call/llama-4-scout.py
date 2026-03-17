# 3.	Use llama-4-scout to generate a short poem about Artificial Intelligence.

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="meta-llama/llama-4-scout:free ",  
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    max_retries=3, 
    timeout=60    
)

prompt = PromptTemplate.from_template(
    template="Write a short, creative poem about Artificial Intelligence in 4-6 lines"
)


formatted_prompt = prompt.format()  
response = llm.invoke(formatted_prompt)
print(response.content)