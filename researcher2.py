import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict, Union
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
# from langgraph.prebuilt import create_react_agent

load_dotenv()

# 1. Setup the Agent
model = ChatOpenAI(model="gpt-4o")

search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 2. Create the Agent
agent = create_agent(model=model, tools=tools)

def run_research(query: str):
    print("Running research for query: {query}")
    response = executor.invoke({"input":query})
    print(f"[Final Answer]: {response['output']}")

agent.invoke("What are the latest advancements in renewable energy?")
    # run_research("What are the latest advancements in renewable energy?")