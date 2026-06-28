import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load the secret key
load_dotenv()
print("Environment variables loaded. Connecting to OpenAI...")

# 2. Initialize the GPT model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 3. Send the prompt
response = llm.invoke("Explain what LangChain is in one short and useful sentence.")

# 4. Print the result
print("\n--- AI Response ---")
print(response.content)
print("-------------------\n")