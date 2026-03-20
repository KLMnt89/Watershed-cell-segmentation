# Watershed Cell Segmentation

A Python implementation of the **Watershed Algorithm** for automatic cell 
segmentation and counting in microscopy images, completed as an individual 
seminar project during the **Digital Image Processing** course at the Faculty 
of Computer Science and Engineering — Skopje (2024/2025, Summer Semester).

## 📁 Repository Structure
```
watershed-cell-segmentation/
├── src/
│   └── Watershed-236006.py    # Main segmentation script
├── images/
│   ├── input/
│   │   └── img.png            # Input microscopy image
│   └── output/                # Auto-generated result images
└── README.md
```

## 🧠 How It Works

1. **Grayscale conversion** — converts the image to single channel
2. **Gaussian Blur** — removes noise before processing
3. **Otsu Binarization** — automatically thresholds the image
4. **Morphological Closing** — fills small holes and gaps
5. **Distance Transform** — calculates distance from background pixels
6. **Sure Foreground/Background** — identifies certain regions
7. **Watershed Algorithm** — segments and separates touching cells
8. **Cell Counting** — counts unique segmented regions

## 📊 Output

Running the script generates 3 images in `images/output/`:

| File | Description |
|---|---|
| `original.png` | Original input image |
| `watershed_result.png` | Image with red cell boundaries |
| `comparison.png` | Side-by-side comparison |

## 🚀 How to Run

Install dependencies:
```bash
pip install opencv-python numpy matplotlib
```

Run the script:
```bash
cd src
python Watershed-236006.py
```

## 🎓 Academic Info

| Field | Details |
|---|---|
| Project Type | Individual Seminar |
| Course | Digital Image Processing |
| Institution | FCSE — Skopje |
| Semester | Summer 2024/2025 |
| Language | Python |
| Libraries | OpenCV, NumPy, Matplotlib |

---

*Part of my academic portfolio — see other projects on my [GitHub profile](https://github.com/KLMnt89).*
