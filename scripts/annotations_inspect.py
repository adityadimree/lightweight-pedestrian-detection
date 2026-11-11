import json 
with open("bdd100k/labels/train/0a0a0b1a-27d9fc44.json") as f:
    data = json.load(f)
    
frame = data["frames"][0]

#frame["objects"] is a list of objects


for obj in frame["objects"]:
    if obj["category"] == "pedestrian":
        print(obj)
