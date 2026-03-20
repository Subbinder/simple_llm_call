# 5.	Use Claude 3 Haiku to translate a sentence from English to Spanish.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

llm=ChatOpenAI(model="claude-3-haiku",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

sentence="shivam is very good learner"
response =llm.invoke(f"translate{sentence} form english into Spanish")

print(response.content)
