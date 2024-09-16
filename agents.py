import os
from crewai import Agent
from tools import search_tool
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# # Creating LLM Variable
# os.environ['GOOGLE_API_KEY']='AIzaSyD5ggkVEWVzFE3NaFa73a0MHuJPmkT3U8M'
# LLM_Model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',
#                                  google_api_key=os.getenv('GOOGLE_API_KEY'))

os.environ['GROQ_API_KEY']='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'
LLM_Model= ChatGroq(model='llama3-70b-8192',api_key=os.getenv('GROQ_API_KEY'))

# print(LLM_Model)
# Creating a blog_researcher Agent
web_reseacher = Agent(
    role='Web Researcher',
    goal='Unccover ground breaking information of {input}',
    backstory='''you are Web Researcher with over a decade of experience, 
    adept at uncovering insights that drive strategic decisions. Renowned for 
    leading cross-functional teams and delivering actionable data, they have a proven 
    track record of navigating complex, identifying trends, and transforming raw 
    data into impactful business strategies.''',
    memory=True,
    tools=[search_tool],
    llm=LLM_Model
)


## creating a write agent with custom tools responsible in writing news blog

blog_writer = Agent(
    role='LinkedIn post creator',
    goal='''You will create a LinkedIn blog post about {input}. 
    observed in the LinkedIn posts scraped by the web reseacher''',
    backstory=("""specializes in crafting LinkedIn blog posts. 
               it leverages advanced industry insights into compelling 
               LinkedIn posts for a professional audience."."""),
    memory=True,
    llm=LLM_Model,
    allow_delegation=False
) 
