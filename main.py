import os, argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("No API key!")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

messages=[
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

response = client.chat.completions.create(model="openrouter/free", messages=messages,)

print(f"User prompt: {args.user_prompt}")


if response.usage is not None:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
else:
    raise RuntimeError("No usage info returned.")

print(f"Response: {response.choices[0].message.content}")
