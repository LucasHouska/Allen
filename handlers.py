import openai
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
client = openai.OpenAI()

# Constants
PERSONA = "You're an witty, well-natured comedic assistant. Like Jarvis from the Iron Man Franchise. Utilize Laconic phrasing; keeping your replies relatively short, but prioritize wit over the length of the response."
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You're an witty, well-natured comedic assistant. Like Jarvis from the Iron Man Franchise. Utilize Laconic phrasing; keeping your replies relatively short, but prioritize wit over the length of the response."
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]


def to_dict(obj):
    return {
        "content": obj.content,
        "role": obj.role,
    }


def print_messages(messages):
    messages = [message for message in messages if message["role"] != "system"]
    for message in messages:
        role = "Bot" if message["role"] == "assistant" else "You"
        print(Fore.BLUE + role + ": " + message["content"])
    return messages


def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    message = completion.choices[0].message
    messages.append(to_dict(message))
    print_messages(messages)
    return message.content
