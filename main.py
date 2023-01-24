import openai
import json
from keys import api_key


openai.api_key = api_key

# start_sequence = "\nAI:"
# restart_sequence = "\nHuman: "
human_input = input("Human: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= human_input,
  temperature=1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=1,
  stop=[" Human:", " AI:"]
)

ai_json = response
ai_json_parse = json.loads(json.dumps(ai_json))
ai_text = ai_json_parse['choices'][0]['text']
ai_text_form = ai_text.lstrip()

print("AI: " + ai_text_form)