from tools.github_tool import get_trending_repos
from tools.weather_tool import get_weather

def executor_agent(plan):
    result = {}
    for step in plan["steps"]:
        if step["tool"] == "github":
            result["github"] = get_trending_repos()
        elif step["tool"] == "weather":
            city = step.get("location", "Delhi")
            result["weather"] = get_weather(city)
    return result