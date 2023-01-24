import os
import openai
from variables import api_key


openai.api_key = api_key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Do you understand math?",
  temperature=1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=1,
  stop=[" Human:", " AI:"]
)

print(response)