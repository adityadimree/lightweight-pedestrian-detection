import json 
import os 

# Original BDD100K annotation folders
TRAIN_JSON_DIR = "bdd100k/labels/train"
VAL_JSON_DIR = "bdd100k/labels/val"

# extracted pedestrian images
TRAIN_IMAGE_DIR = "bdd_pedestrian/images/train"
VAL_IMAGE_DIR = "bdd_pedestrian/images/val"

# YOLO labels output directory
TRAIN_LABEL_DIR = "bdd_pedestrian/labels/train"
VAL_LABEL_DIR = "bdd_pedestrian/labels/val"

os.makedirs(TRAIN_LABEL_DIR, exist_ok=True)
os.makedirs(VAL_LABEL_DIR, exist_ok=True)

def convert_labels(json_dir, image_dir, label_dir):
    
    converted = 0
    skipped = 0
    
    for filename in os.listdir(json_dir):
        print(filename)
        if not filename.endswith(".json"):
            print("not a json file")
            continue
        
        json_path = os.path.join(json_dir, filename)
        
        with open(json_path, "r") as f:
            data = json.load(f)
            
        image_name = data["name"]
        #print(image_name)
        image_path = os.path.join(image_dir, f"{image_name}.jpg")
        
        #check whether the corresponding image file to the current iteration's annotation file was extracted or not. That is, confirm whether pedestrian is present or not.
        if not os.path.exists(image_path):
            print(f"this image does not have pedestrians in it:{image_name}")
            continue 
        #all the lines below will be executed if and only if the corresponding image file was extracted i.e. if the images contain a pedestrian     
        #BDD100K images are 1280x720 which needs to be specified to yolo maybe
        image_width = 1280
        image_height = 720
        
        yolo_lines = []
        
        for frame in data["frames"]:
        
            for obj in frame["objects"]:
            
                # Extract the pedestrian box2d only ignore all else
                if obj["category"] != "person":
                    continue
                    
                print(obj)
                
                box = obj["box2d"]
                
                x1 = box["x1"]
                y1 = box["y1"]
                x2 = box["x2"]
                y2 = box["y2"]
                
                # Convert BDD100K box --> YOLO format
                x_center = ((x1+x2) /2) / image_width # finding center by averaging and then normalizing it 
                y_center = ((y1+y2) /2) / image_height
                
                width = (x2 - x1) / image_width
                height = (y2 - y1) / image_height
                
                # creating YOLO lines and also adding the 0 as a class representation !
                yolo_lines.append(
                    f"0 {x_center:.6f} {y_center:.6f} "
                    f"{width:.6f} {height:.6f}"
                )
                #print(yolo_lines)
                
        #creating the yolo txt file
        if yolo_lines:
        
            txt_filename = f"{image_name}.txt"
            txt_file_path = os.path.join(label_dir, txt_filename)    
             
            with open(txt_file_path, "w") as f:
                f.write("\n".join(yolo_lines))
            converted += 1
            
        else:
            skipped += 1 
    print(f"Converted: {converted}")
    print(f"Skipped: {skipped}")
#______________________________Function ends_____________________#    

print("Converting TRAIN labels...")
convert_labels(
    TRAIN_JSON_DIR,
    TRAIN_IMAGE_DIR,
    TRAIN_LABEL_DIR
)

print("\nConverting VALUATION labels...")
convert_labels(
    VAL_JSON_DIR,
    VAL_IMAGE_DIR,
    VAL_LABEL_DIR
)

print("\nDone !")

