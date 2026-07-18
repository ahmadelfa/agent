import os, argparse, json
from dotenv import load_dotenv
from openai import OpenAI
from openai.resources.realtime.realtime import BaseRealtimeConnectionResource
from prompts import system_prompt
from config import MODEL
from call_function import available_functions, call_function

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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

for _ in range(20):
    response = client.chat.completions.create(model=MODEL, messages=messages, tools=available_functions,)
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage is not None:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        else:
            raise RuntimeError("No usage info returned.")
    
    message = response.choices[0].message
    messages.append(message)
    
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            if result_message["content"] == None or "":
                raise Exception("Tool call returned empty content")
            if args.verbose:
                print(f"-> {result_message['content']}")
            messages.append(result_message)
    else:
        print(f"Response: {message.content}")
        break
else:
    print("Error: Maximum iterations reached without a final response.")
    exit(1)
