import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
Agent_LLM = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192",
            temperature = 0
        )