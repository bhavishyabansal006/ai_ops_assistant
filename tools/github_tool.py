import requests

def get_trending_repos():
    url = "https://api.github.com/search/repositories?q=stars:>50000&sort=stars"
    data = requests.get(url).json()
    return [
        {
            "name": r["name"],
            "stars": r["stargazers_count"],
            "url": r["html_url"]
        }
        for r in data["items"][:3]
    ]