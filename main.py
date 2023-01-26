import openai
import json
from keys import api_key
from dialogue import ai_prep

openai.api_key = api_key

all_input    = ""
all_history, prev_input = ai_prep, ai_prep

start_sequence = "\nPlayer: "
restart_sequence = "\n\nDM: "

while True:
  human_input = input("Player: ")

  if human_input == "stop":
    print("Exiting. Thanks for playing! Here is your chat history!", end="\n\n")
    # Commenting out to reduce clutter during debug
    # print(all_history)
    break

  else:
    fhuman_input = human_input
    all_input = prev_input + fhuman_input
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= all_input,
      temperature=.9,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=1
    )

    ai_json = response
    ai_json_parse = json.loads(json.dumps(ai_json))
    ai_text = ai_json_parse['choices'][0]['text']
    ai_text_format = ai_text.lstrip()

    print("\nNPC: " + ai_text_format, end = "\n\n")
    prev_input = all_input + ai_text_format

    ### Debug Code ###
    print("\n\n\n" + prev_input)

    human_history = ("Player: " + fhuman_input + "\n\n")
    ai_history    = ("NPC: " + ai_text_format + "\n")
    all_history   = (all_history + human_history + ai_history + "\n")
