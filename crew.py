# Import Require Library
import streamlit as st
from crewai import Crew,Process
from agents import web_reseacher,blog_writer,LLM_Model
from tasks import reseacher_task,writer_task

# Creating Web Page header
# st.header("Welcome to Revolutionary Workflows with AI Agents The Future is Now")
st.subheader("Your AI Agents for Linkedin Blog Post...")

# Getting Task From Web
post_content = st.text_area("What Linkedin Blog Post Would you Like me to come up with Today?")

# Creating Crew
crew = Crew(
    agents=[web_reseacher,blog_writer],
    tasks=[reseacher_task,writer_task],
    manager_llm=LLM_Model,
    process=Process.sequential,
    verbose=True
)

# Creating a Dict Input Variable 
inputs={'input':post_content}

# Query Answering
if st.button("Generate"):
    with st.spinner("Generate Response..."):
        res=crew.kickoff(inputs=inputs)
        res1=str(res)
        st.subheader("Here is a Response..")
        st.markdown(res)
        st.download_button(label='Download Text File',file_name=f'{post_content} blogpost.txt',data=res1)