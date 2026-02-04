from llm.llm_client import call_llm

def verifier_agent(task, result):
    prompt = f"""
Task: {task}
Result: {result}

Generate a clean, readable final answer.
"""
    return call_llm(prompt)