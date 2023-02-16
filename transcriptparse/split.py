#import json

with open('transcript.txt', 'r') as file:
    text = file.read()

text = text.replace("â†’", "")
sections = text.split('#')

print(sections)

# for section in sections:
#     print(section.strip())