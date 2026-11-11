# Failure-Aware Lightweight Pedestrian Detection

A lightweight pedestrian detection project using **YOLOv8n** and the **BDD100K dataset**, focused on real-world driving scenes and challenging environmental conditions.

## Overview

Pedestrian detection is an important component of intelligent transportation systems and autonomous driving. However, detecting pedestrians in real-world environments can be challenging due to variations in lighting, weather, occlusion, and scene complexity.

This project implements a lightweight pedestrian detection model using YOLOv8n. It uses pedestrian annotations from BDD100K to prepare a single-class detection dataset and train the model.

The project also examines model performance through validation metrics, prediction visualizations, and error analysis.

## Dataset

**BDD100K (Berkeley DeepDrive)**

BDD100K is a large-scale driving dataset containing images and videos captured under diverse driving conditions.

For this project:
- Images containing pedestrians (`person` category) were selected.
- Original JSON annotations were processed.
- Bounding boxes were converted into YOLO format.
- Separate training and validation datasets were prepared.

**Note:** The dataset is not included in this repository. Users must obtain BDD100K separately and follow its applicable access and usage terms.

## Model

| Parameter | Configuration |
|---|---|
| Architecture | YOLOv8n |
| Task | Object Detection |
| Classes | 1 (Person) |
| Image Size | 416 × 416 |
| Epochs | 10 |
| Training Device | CPU |
| Framework | Ultralytics |

## Training Results

The model was trained for 10 epochs and evaluated on the validation dataset.

| Metric | Result |
|---|---:|
| Precision | 57.2% |
| Recall | 41.0% |
| mAP@50 | 43.5% |
| mAP@50–95 | 19.2% |

### Training Visualizations

Training curves, precision-recall curves, confusion matrices, and prediction comparisons are available in the `results/` directory.

## Repository Structure

```text
lightweight-pedestrian-detection/
│
├── README.md
├── .gitignore
│
├── scripts/
│   ├── annotations_inspect.py
│   ├── extract_annotations.py
│   ├── extract_pedestrian.py
│   └── find_pedestrian.py
│
├── data/
│   └── data.yaml
│
├── weights/
│   └── best.pt
│
└── results/
    ├── results.csv
    ├── args.yaml
    ├── plots/
    ├── predictions/
    └── validation/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/adityadimree/lightweight-pedestrian-detection.git
cd lightweight-pedestrian-detection
```

Create a Python virtual environment:

```bash
python3 -m venv yolo_env
source yolo_env/bin/activate
```

Install the required framework:

```bash
pip install ultralytics
```

## Dataset Preparation

After obtaining BDD100K, prepare the dataset using the provided scripts.

The expected YOLO dataset structure is:

```text
bdd_pedestrian/
├── images/
│   ├── train/
│   └── val/
│
└── labels/
    ├── train/
    └── val/
```

Update the paths in `data/data.yaml` to match your local dataset location.

## Running Inference

Use the trained model to perform pedestrian detection:

```bash
yolo detect predict \
    model=weights/best.pt \
    source=path/to/image.jpg \
    imgsz=416 \
    device=cpu
```

For a video:

```bash
yolo detect predict \
    model=weights/best.pt \
    source=path/to/video.mp4 \
    imgsz=416 \
    device=cpu
```

## Limitations

- The model was trained for only 10 epochs.
- Evaluation metrics reported here are from the validation dataset.
- An independent labelled test-set evaluation has not yet been completed.

These limitations provide opportunities for further experimentation and improvement.

## Future Work

- Evaluate performance on an independently annotated test dataset.
- Explore lightweight model improvements for CPU-based inference.

## Acknowledgements

- **BDD100K:** Berkeley DeepDrive dataset.
- **Ultralytics:** YOLOv8 object detection framework.

---

**Project:** Failure-Aware Lightweight Pedestrian Detection under Adverse Weather and Domain Shift  
**Model:** YOLOv8n  
**Task:** Single-class pedestrian detection
