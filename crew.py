# Import Require Library
import streamlit as st
from crewai import Crew,Process
from agents import web_reseacher,blog_writer,LLM_Model
from tasks import reseacher_task,writer_task

# Creating Web Page header
st.subheader("**Multi AI Agent LinkedIn Blog Generator...**")

# Getting Task From Web
with st.form(key='Query',clear_on_submit=True):
    post_content=st.text_input(label='**What Linkedin Blog Post Would you Like me to come up with Today?**')
    submit_button = st.form_submit_button('Submit.')
    if submit_button:
        st.info('Input Details...')
        st.markdown(f'Blog Post Name: {post_content} ...')

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
        result=str(res)
        st.info("Here is a Response..")
        st.markdown(res)
        st.download_button(label='Download Text File',file_name=f'{post_content} blogpost.txt',data=result)
