# Computer-Vision
Basic image loading and display with OpenCV in Python.

## Repository Structure

```
Computer Vision/
├── Files/
│   └── images.py
├── Images/
│   ├── sample1.jpg
│   └── sample2.jpg
└── README.md
```

## What `images.py` Does

The script in the `Files` folder does the following:

1. Imports OpenCV (`cv2`).
2. Loads two images from the `Images` folder using `cv2.imread()`.
3. Prints an error if an image fails to load, otherwise prints its shape
   (height, width, number of color channels).
4. Displays each loaded image in its own window with `cv2.imshow()`.
5. Waits for a key press, then closes all windows.

## About the Images Folder

Two sample image files that `images.py`
loads and displays. Any `.jpg` or `.png` files work as long as the
filenames in `IMAGE_PATHS` inside `images.py` match.

## How to Run

1. Install OpenCV:
   ```bash
   pip install opencv-python
   ```
2. From inside the `Files` folder, run:
   ```bash
   python images.py
   ```

## Requirements

- Python 3.x
- opencv-python
