# AI Ops Assistant 🤖

An AI-powered operations assistant built using FastAPI that plans tasks and executes tools (like weather fetching) using an agent-based architecture.

---

## 🚀 Features

- FastAPI backend with `/run` endpoint
- Planner → Executor agent workflow
- Tool-based execution (Weather API)
- Environment variable support using `.env`
- Modular and clean project structure

---

## 🧠 Project Structure

ai_ops_assistant/
├── main.py
├── agents/
│   ├── planner.py
│   └── executor.py
├── tools/
│   └── weather_tool.py
├── .env.example
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
git clone https://github.com/bhavishyabansal006/ai_ops_assistant.git
cd ai_ops_assistant

### 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Setup environment variables
Create a .env file:
WEATHER_API_KEY=your_openweather_api_key

---

## ▶️ Run the application
uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

---

## 🧪 Example Usage
What is the weather in Delhi?

---

## 👤 Author

Bhavishya Bansal  
GitHub: https://github.com/bhavishyabansal006
