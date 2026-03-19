# 4. Use nvidia/nemotron-3 to create 5 SQL interview questions for beginners.

from langchain_community.llms import NvidiaAIEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm= NvidiaAIEndpoint(model="nvidia/nemotron-3-nano-30b:free",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

response=llm.invoke("create 5 SQL interview questions for beginners")

print(response.content)
