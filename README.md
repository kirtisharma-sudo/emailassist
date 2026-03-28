---
title: EmailAssist
emoji: ✉️
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: app.py
pinned: false
---
# 📧 EmailAssist — A Real-World OpenEnv Environment for AI Agents

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Enabled-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![OpenEnv](https://img.shields.io/badge/OpenEnv-Compliant-purple)
![HuggingFace Spaces](https://img.shields.io/badge/Deploy-HF%20Spaces-yellow)

---

## 📝 About EmailAssist

**EmailAssist** is a real-world OpenEnv environment that simulates  
**professional email triage**, **priority assignment**, and **email drafting** —  
a task domain commonly used in:

- Customer support  
- Operations workflows  
- Corporate communication  
- Personal productivity tools  

It is **not a toy**: these actions reflect real human workflows.

EmailAssist provides **3 tasks** with increasing difficulty:

1. **Task 1: Email Intent Classification (Easy)**  
2. **Task 2: Email Priority Ranking (Medium)**  
3. **Task 3: Drafting Email Replies (Hard)**  

Each task includes **programmatic graders** outputting scores **0.0–1.0**.

---

# 🧠 Observation & Action Spaces

## 🎯 Observation (Pydantic Model)

```python
class EmailObservation(BaseModel):
    email_text: str
    task_type: str         # task1, task2, task3
    context: Optional[str] # provided for drafting
````

The agent receives only the email text and optional context.

---

## 🎮 Action Space (Pydantic Model)

```python
class EmailAction(BaseModel):
    category: Optional[str] = None      # Task 1
    priority: Optional[str] = None      # Task 2
    email_text: Optional[str] = None    # Task 3
```

Agents must choose the correct field based on the task type.

---

# 🧩 Tasks & Graders

## ✔ **Task 1 — Email Intent Classification (Easy)**

Goal: classify an email into one of:

```
["complaint", "request", "spam", "follow_up", "other"]
```

### Scoring

```
1.0  → correct category  
0.0  → incorrect  
```

---

## ✔ **Task 2 — Email Priority Ranking (Medium)**

Goal: assign email priority:

```
["low", "medium", "high"]
```

### Scoring

* Follows exact-match + partial match rules:

```
1.0 → correct  
0.5 → close (high vs medium)  
0.0 → wrong  
```

---

## ✔ **Task 3 — Drafting Email Replies (Hard)**

Goal: write a professional reply based on the incoming email.

### Grader scoring

Uses cosine similarity + template scoring:

```
1.0 → strong structure + polite + relevant  
0.5 → partially relevant  
0.0 → irrelevant or missing  
```

---

# 🏆 Reward Shaping

Each step returns a structured reward:

```
+1.0  → perfectly correct action  
+0.5  → partial correctness  
0.0   → no progress  
-0.2  → wrong action for the task  
```

The agent receives feedback at every step — **not just at the end**.

---

# 🗂 Directory Structure

```
emailassist/
│
├── env_emailassist/
│   ├── env.py
│   ├── models.py
│   ├── openenv.yaml
│   ├── tasks/
│   │   ├── task1_classify.py
│   │   ├── task2_priority.py
│   │   └── task3_drafting.py
│   └── graders/
│       ├── classify_grader.py
│       ├── priority_grader.py
│       └── drafting_grader.py
│
├── app.py
├── inference.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🚀 Running the Environment Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Launch FastAPI server

```
uvicorn app:app --reload --host 0.0.0.0 --port 7860
```

Server will run at:

```
http://localhost:7860
```

---

# 🧪 Baseline Inference (Mandatory)

Run:

```
python inference.py
```

Environment variables required:

```
export API_BASE_URL="https://router.huggingface.co/v1"
export MODEL_NAME="meta-llama/Llama-3.1-8B-Instruct"
export HF_TOKEN="your_hf_token"
```

This script:

* Connects to your FastAPI server
* Calls the model
* Steps through tasks 1 → 2 → 3
* Prints baseline scores

---

# 📦 Docker Build & Run

Build:

```
docker build -t emailassist .
```

Run:

```
docker run -p 7860:7860 emailassist
```

---

# 🤗 HuggingFace Spaces Deployment

1. Create a new Space → **Type: Docker**
2. Upload entire `emailassist/` project
3. Push via Git
4. HF will automatically build using your Dockerfile
5. On success, your Space will display:

```
EmailAssist Environment is running!
```

---

# 🏁 Submission Requirements Status

| Requirement           | Status |
| --------------------- | ------ |
| Real-world task       | ✅      |
| 3 tasks + graders     | ✅      |
| OpenEnv spec          | ✅      |
| Reward shaping        | ✅      |
| Baseline inference.py | ✅      |
| Dockerfile            | ✅      |
| HF Space-ready        | ✅      |
| README complete       | ✅      |

---

# 🥇 Author

Solo participant: **Kirti Sharma**
Built for **Meta x HuggingFace OpenEnv Hackathon 2026**.

---
