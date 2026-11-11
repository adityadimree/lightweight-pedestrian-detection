import json
import os
import shutil

# Paths
LABEL_DIR = "bdd100k/labels/val"
IMAGE_DIR = "bdd100k/images/100k/val"
OUTPUT_DIR = "bdd_pedestrian/images/val"

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0

for filename in os.listdir(LABEL_DIR):

    if not filename.endswith(".json"):
        continue

    json_path = os.path.join(LABEL_DIR, filename)

    with open(json_path, "r") as f:
        data = json.load(f)

    # Check whether this image contains a person
    has_person = False

    for frame in data["frames"]:
        for obj in frame["objects"]:
            if obj["category"] == "person":
                has_person = True
                break

        if has_person:
            break

    if not has_person:
        continue

    # Get image name
    image_name = data["name"]
    print(image_name)

    # BDD image names normally end in .jpg
    image_path = os.path.join(IMAGE_DIR, f"{image_name}.jpg")

    if os.path.exists(image_path):
        shutil.copy2(
            image_path,
            os.path.join(OUTPUT_DIR, f"{image_name}.jpg")
        )

        count += 1

print("Done!")
print("Images containing pedestrians:", count)
