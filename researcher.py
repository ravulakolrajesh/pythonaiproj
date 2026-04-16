import os
from dotenv import load_dotenv
from typing import Annotated, TypeDict, Union
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent


load_dotenv()

#1. The Brain (LLM)
llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# 2. The Tool (Search)
search = DuckDuckGoSearchRun()
tools = [search]

# 3. The Prompt Template
prompt = hub.pull("hwchase17/react")

# 4. Construct the Agent
agent = create_react_agent(llm, tools, prompt=prompt)

# 5. Create the Executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# 6. Run it
# agent_executor.invoke("What is the latest research on AI in healthcare?")

# from langchain_community.tools import DuckDuckGoSearchRun

# search = DuckDuckGoSearchRun()
# try:
#     result = search.run("Current CEO of NVIDIA")
#     print("Success! Search result:", result)
# except Exception as e:
#     print("Still failing. Error:", e)