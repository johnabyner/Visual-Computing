# Visual-Computing

A study repository focused on **visual computing and computer vision** using Python.

The project contains exercises and experiments with **OpenCV, image processing, object detection, object tracking, face detection, and YOLO**.

---

## Features

* Image manipulation with OpenCV
* Color segmentation using HSV
* Image masks and filters
* Morphological operations
* Contour detection
* Shape detection and object counting
* Face, eye, and smile detection
* Video processing
* Object detection with YOLO
* Person tracking and counting
* Custom YOLO model training
* License plate detection experiments
* Model evaluation using detection metrics

---

## Project Goal

The main goal of this repository is **learning and practicing computer vision concepts through small experiments**.

The studies progress from basic image processing to more advanced object detection and tracking techniques.

Some of the concepts explored include:

* Image and video processing
* Color spaces
* Masks
* Contours
* Morphology
* Haar Cascades
* Object detection
* Object tracking
* Bounding boxes
* Confidence scores
* Precision and recall
* mAP
* Dataset preparation
* YOLO model training

---

## Technologies

* Python
* OpenCV
* NumPy
* Ultralytics YOLO
* PyTorch
* Pillow
* Matplotlib
* Polars

---

## Installation

### Prerequisites

You will need:

* **Python**
* **pip**

A recent version of Python is recommended.

### Clone the repository

```bash
git clone https://github.com/johnabyner/Visual-Computing
cd Visual-Computing
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Studies

### OpenCV

The `opencv` directory contains the initial computer vision experiments:

```bash
python opencv/module1.py
```

```bash
python opencv/module1_2.py
```

```bash
python opencv/module2.py
```

```bash
python opencv/module3.py
```

```bash
python opencv/module4.py
```

These modules cover image manipulation, color tracking, video processing, shape detection, object counting, and Haar Cascade detection.

### YOLO

The `yolo` directory contains experiments with object detection and tracking:

```bash
python yolo/module1.py
```

```bash
python yolo/module2.py
```

The repository also contains a custom training experiment for **license plate detection**:

```bash
python yolo/datasets/licensePlate/train.py
```

---

## Examples

### Color Tracking

Detect specific colors using HSV masks and draw bounding boxes around the detected regions.

### Shape Detection

Use contours and polygon approximation to identify shapes such as:

```text
Triangle
Square
Rectangle
Pentagon
Circle
```

### Face Detection

Use Haar Cascade classifiers to detect:

```text
Faces
Eyes
Smiles
```

### YOLO Object Detection

Run YOLO inference and extract:

```text
Class
Confidence
Bounding Box
```

### Person Tracking

Track people across video frames and assign unique IDs to detected individuals.

### License Plate Detection

Train and evaluate a custom YOLO model using a dataset containing license plate annotations.

---

## Project Structure

```text
Visual-Computing/
├── opencv/
│   ├── haarcascades/
│   ├── photos/
│   ├── results/
│   ├── videos/
│   ├── module1.py
│   ├── module1_2.py
│   ├── module2.py
│   ├── module3.py
│   └── module4.py
│
├── yolo/
│   ├── datasets/
│   │   └── licensePlate/
│   ├── photos/
│   ├── videos/
│   ├── module1.py
│   └── module2.py
│
├── runs/
│   └── detect/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Note

This is primarily a **learning and experimentation repository**.

The focus is on understanding computer vision concepts by implementing small projects and progressively moving from traditional OpenCV techniques to modern **YOLO-based detection and tracking**.
