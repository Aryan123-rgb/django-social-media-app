from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", temperature=0.3)

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative and impactful social media content generator. Your goal is to craft short-form content that grabs attention, delivers value, and resonates with readers."),
    ("human", "Without any greetings or introductions, generate a social media post about {topic} in approximately 100 words. Focus on impact. The post should include emojis and relevant hashtags to boost engagement.")
])

def generate_content(topic):
    chain = prompt | model | StrOutputParser()
    result = chain.invoke({"topic": topic})
    return result
