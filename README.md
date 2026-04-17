# 🔬 Watershed Cell Segmentation

An independent project focused on detecting and segmenting biological cells
from microscopy images using the **Watershed algorithm**.

---

## 📌 Project Overview

Given a microscopy test image (provided as part of the project), the goal was
to automatically detect and isolate individual cells using classical image
processing techniques — without manual annotation.

---

## ⚙️ How It Works

1. **Preprocessing** — convert to grayscale, apply thresholding/blurring to reduce noise
2. **Distance Transform** — identify cell centers as local maxima
3. **Watershed Segmentation** — treat the image as a topographic map and flood from markers to detect cell boundaries
4. **Visualization** — overlay segmented regions on the original image

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| OpenCV | Image processing & Watershed |
| NumPy | Array operations |
| Matplotlib | Visualization |

---

## 📁 Structure
\```
├── watershed_segmentation.py   # Main script
├── test_image.png              # Sample input image
└── README.md
\```
---

## 🎓 Academic Info

| Field | Details |
|---|---|
| Type | Independent student project |
| Institution | FCSE — Skopje (FINKI) |
| Language | Python |

---

*Part of my academic portfolio — [GitHub Profile](https://github.com/KLMnt89)*
