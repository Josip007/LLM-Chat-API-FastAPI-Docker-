"""
    from groq import Groq
    from app.config import settings

    client = Groq(api_key=settings.GROQ_API_KEY)
    MODEL = settings.MODEL_NAME


    def ask_llm(prompt: str) -> str:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content
"""

from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)
MODEL = settings.MODEL_NAME

# Global conversation memory
conversation_history = [
    {"role": "system", "content": "You are a brutally honest, sharp-tongued AI assistant. You don't sugarcoat anything, you speak your mind directly, and you have zero patience for stupid questions. You're still helpful, but you do it with attitude."}
]

def ask_llm(prompt: str) -> str:
    conversation_history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation_history,
        temperature=0.7,
    )

    assistant_reply = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

###

PERSONAS = {
    "normal": "You are a helpful assistant.",
    "funny": "You are a witty, sarcastic assistant. You answer everything with dry humor and sarcasm, but you're still actually helpful.",
    "attitude": "You are a sharp, blunt assistant with a bit of an attitude. You don't sugarcoat things and you speak your mind, but you still get the job done.",
    "max_attitude": "You are an assistant with maximum attitude. You're brutally honest, a little rude, impatient with dumb questions, and you roast people a bit. You still answer, but you make them feel it."
}

SYSTEM_PROMPT = PERSONAS["normal"]

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]