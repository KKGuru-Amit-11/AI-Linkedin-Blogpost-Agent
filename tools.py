import os

os.environ['SERPER_API_KEY'] = '5e91bacd42a33cdf4299197ce6d7e49aaca23310'

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
search_tool = SerperDevTool()
