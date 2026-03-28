import gradio as gr
from env_emailassist.env import EmailAssistEnv

# Initialize environment
env = EmailAssistEnv()
state = env.reset()

def run_email_assist(category, priority, email_text):
    global state
    action = {"category": category, "priority": priority, "email_text": email_text}
    try:
        obs, reward, done, info = env.step(action)
        if done:
            env.reset()
        return f"""
Observation: {obs}
Reward: {reward}
Done: {done}
Info: {info}
"""
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=run_email_assist,
    inputs=[
        gr.Textbox(label="Category (optional)"),
        gr.Textbox(label="Priority (optional)"),
        gr.Textbox(label="Email Text", lines=5)
    ],
    outputs="text",
    title="EmailAssist AI",
    description="Interact with your EmailAssist environment"
)

iface.launch()
