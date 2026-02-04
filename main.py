from fastapi import FastAPI
from pydantic import BaseModel
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

app = FastAPI()

class Task(BaseModel):
    task: str

@app.post("/run")
def run(task: Task):
    plan = planner_agent(task.task)
    result = executor_agent(plan)
    final = verifier_agent(task.task, result)
    return {
        "plan": plan,
        "result": result,
        "final_answer": final
    }