import json 
import os 
from collections import Counter 

LABEL_DIR = "bdd100k/labels/train"

categories = Counter()
json_count = 0 

for filename in os.listdir(LABEL_DIR):
    if not filename.endswith(".json"):
        continue

    json_count += 1

    with open(os.path.join(LABEL_DIR, filename), "r") as f:
        data = json.load(f)

    for frame in data["frames"]:
        for obj in frame["objects"]:
            categories[obj["category"]] += 1

print("JSON files:", json_count)
print("\nCategories found:")
for category, count in categories.most_common():
    print(f"{category}: {count}")

