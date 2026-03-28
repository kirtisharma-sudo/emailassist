from fastapi import FastAPI
from pydantic import BaseModel
from env_emailassist.env import EmailAssistEnv

app = FastAPI(title="EmailAssist Environment API")

# Initialize environment
env = EmailAssistEnv()
state = env.reset()


# -------------------------
# Request Schema
# -------------------------
class Action(BaseModel):
    category: str | None = None
    priority: str | None = None
    email_text: str | None = None


# -------------------------
# API ROUTES
# -------------------------

@app.get("/")
def root():
    return {"message": "EmailAssist Environment is running!"}


@app.get("/state")
def get_state():
    """Return the current state to the client."""
    return state


@app.post("/run")
def run_action(action: Action):
    """
    Take one step in environment.
    Accepts any of the 3 possible actions.
    """
    global state

    obs, reward, done, info = env.step(action.dict())

    if done:
        env.reset()

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }
