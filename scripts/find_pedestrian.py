import json
import os

LABEL_DIR = "bdd100k/labels/val"

person_count = 0
files_with_person = 0

for filename in os.listdir(LABEL_DIR):
    print("working on :", filename)

    if not filename.endswith(".json"):
        continue

    filepath = os.path.join(LABEL_DIR, filename)

    with open(filepath, "r") as f:
        data = json.load(f)

    found_in_file = False

    for frame in data["frames"]:

        for obj in frame["objects"]:

            if obj["category"] == "person":

                person_count += 1
                found_in_file = True

                print("File:", filename)
                print("person:", obj)
                print()

    if found_in_file:
        files_with_person += 1

print("--------------------------------")
print("Total person annotations:", person_count)
print("Files containing persons:", files_with_person)

#credits to chat-gpt for this script
