# Define the input and output file names
input_file = "crft.txt"
output_file = "formatted_segments.txt"

# Read the input file and extract the segments
with open(input_file, "r") as f:
    script = f.read()

segments = {}
lines = script.split("\n")
current_speaker = None
current_segment = ""

for line in lines:
    if line.startswith("#"):
        if current_speaker is not None:
            segments[current_speaker] = current_segment.strip()
        current_speaker = line[2:]
        current_segment = ""
    else:
        current_segment += line + "\n"

if current_speaker is not None:
    segments[current_speaker] = current_segment.strip()

# Format the segments into alternating prompts and completions
formatted_segments = []

speakers = list(segments.keys())
num_speakers = len(speakers)
for i in range(num_speakers - 1):
    speaker1 = speakers[i]
    speaker2 = speakers[i+1]
    response1 = segments[speaker1]
    response2 = segments[speaker2]
    prompt = f"{speaker1}: {response1}"
    completion = f"{speaker2}: {response2}"
    formatted_segments.append({"prompt": prompt, "completion": completion})

# Write the formatted segments to the output file
with open(output_file, "w") as f:
    for segment in formatted_segments:
        prompt = segment["prompt"].replace("\n", " ")
        completion = segment["completion"].replace("\n", " ")
        f.write(f"{prompt}\n{completion}\n\n")
