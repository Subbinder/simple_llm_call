# 1.	Use Gemini gpt-3.5-turbo and explain Machine Learning in simple terms.

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
load_dotenv()

prompt = PromptTemplate.from_template(template="explain {topic} in simple terms") 


llm=ChatOpenAI(model="gpt-3.5-turbo",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

response = llm.invoke(prompt.format(topic="Machine Learning"))

print(response.content)
