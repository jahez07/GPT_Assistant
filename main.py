import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts

# load the .env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

model = "gpt-4-0125-preview"
temperature = 0.3
max_tokens = 500

# data about the user
name = "jahez"
reminder_text = ""

# prompts
system_message = prompts.system_message
prompt = prompts.generate_prompt(name, reminder_text)

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompt}
]


# helper function
def personal_assistat():
    completion = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature,
        max_tokens = max_tokens,
    )
    return completion.choices[0].message.content

print(personal_assistat)