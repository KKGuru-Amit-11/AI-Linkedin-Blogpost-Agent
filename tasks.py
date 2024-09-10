# Import Require Library
from crewai import Task
from agents import web_reseacher,blog_writer

# Creating Task for Agents
reseacher_task = Task(
    description='''Find and summarize the latest and most relevant big trend in {input}, 
    focus on identifying pros and cons and the ovreall narrative. Gather insights from reputable sources, 
    including industry blogs, whitepapers, and expert opinions, to support the LinkedIn blog post your final 
    report should clearly articulate the key points''',
    expected_output='come up with comprehensive report on the latest trend {input}',
    agent=web_reseacher
)

writer_task = Task(
    description='''compose an insightful blog on {input} on the basis of researcher task focus on latest trends and
    how it's impacting the industry. this content should be essy to understand, engaging and positive''',
    expected_output='write the intersting linkedin blog post on {input}.',
    agent=blog_writer
)