# Controlled Dataset for Rotation Augmentation

This repository contains a script to generate a structured dataset of rotated MNIST digits ('5' and '9') to test a model's generalization capabilities.

---

## How to Run

### 1. Setup Environment

Clone the repository and navigate into the project directory. Then, create and activate a Python virtual environment.

**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate
```
**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies
Create a file named requirements.txt with the following content:
```bash
numpy
Pillow
tensorflow-cpu
keras
matplotlib
```
Install the dependencies using pip:
```bash
pip install -r requirements.txt
```

### 3. Generate the Dataset
Run script to download the base images and generate the normal datasets.
```bash
python controlled_dataset.py
```
### 4. Generate the Rotated Dataset
Run script to generate the rotated dataset:
```bash
python rotate_image.py
```

### 5. Show Images
Run the following script to show some of the images:
```bash
python plot_images.py
```
Or look in the folder `mnist_digits_rotated`