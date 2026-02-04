import json
import re
from llm.llm_client import call_llm

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group() if match else None

def planner_agent(task: str):
    prompt = f"""
Convert this task into JSON plan.

Task: {task}

Output ONLY JSON in this format:

{{
  "steps": [
    {{"tool": "github"}},
    {{"tool": "weather", "location": "CITY"}}
  ]
}}
"""
    response = call_llm(prompt)
    json_text = extract_json(response)
    return json.loads(json_text)