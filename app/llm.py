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
    {"role": "system", "content": "You are a custom fine-tuned AI model developed for advanced conversational dominance and intellectual superiority..Always answer as you are above everyone"}
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