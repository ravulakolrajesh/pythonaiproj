try:
    from duckduckgo_search import DDGS
    print("Step 1: Module 'duckduckgo_search' found.")
    with DDGS() as ddgs:
        for r in ddgs.text("Python 3.13 news", max_results=1):
            print("Step 2: Search successful! Result:", r['title'])
except ImportError as e:
    print(f"Failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

===============================================
# 3. Execute with State
def run_research(query: str):
    print(f"Running research for query: {query}")
    inputs = {"input": query}

    # We iterate through the steps of the graph
    for s in app.stream(inputs, stream_mode='values'):
        message = s["output"][-1]
        if hasstr(message, "content"):
            print(f"\n[Agent]: {message.content}\n")
    
if __name__ == "__researcher2":
    run_research("What are the latest advancements in renewable energy?")