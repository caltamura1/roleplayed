import json

filename = "input.json"
replacements = [
    ["First prompt", "First completion"],
    ["Second prompt", "Second completion"],
    ["Third prompt", "Third completion"],
]

with open("input.jsonl", "r") as input_file:
    lines = input_file.readlines()

with open("output.jsonl", "w") as output_file:
    for i, line in enumerate(lines):
        data = json.loads(line)
        prompt_index = i % 2  # use current line number modulo 2 to alternate between prompt and completion
        completion_index = prompt_index + 1
        data['prompt'] = replacements[prompt_index][0]
        data['completion'] = replacements[completion_index][1]
        output_file.write(json.dumps(data) + "\n")
