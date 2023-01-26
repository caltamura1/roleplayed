import openai
import json
from keys import api_key

openai.api_key = api_key

all_input     = ""
prev_input    = ""
all_history   = ""

#need to find a good way to tune the AI before start.

ai_prep = """I want you to pretend to be an NPC from the roleplaying game Dungeons and Dragons.
I am about to give you a lot of information about the world space you exist in. Use it to develop your character."""

# world_setting = input("""\nHello Game Master! 
# This is a program designed to create real time NPCs so you don't have to.
# Please enter in as much background information on your world as possible.
# The AI will memorize and base its responses on your submission.
# Then you may ask it to role play as a character.
# And continue the conversation from there.\n\n
# Please describe your world: """)

while True:
  human_input = input("Human: ")

  if human_input == "stop":
    print("Exiting. Thanks for playing! Here is your chat history!", end="\n\n")
    print(all_history)
    break

  else:
    all_input = prev_input + human_input
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= all_input,
      temperature=1,
      max_tokens=2000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=1
    )

    ai_json = response
    ai_json_parse = json.loads(json.dumps(ai_json))
    ai_text = ai_json_parse['choices'][0]['text']
    ai_text_format = ai_text.lstrip()

    print("\nAI: " + ai_text_format, end = "\n\n")
    prev_input = all_input + ai_text_format

    human_history = ("Human: " + human_input + "\n\n")
    ai_history    = ("AI: " + ai_text_format + "\n")
    all_history   = (all_history + human_history + ai_history + "\n")
