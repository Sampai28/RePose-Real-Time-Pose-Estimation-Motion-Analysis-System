# 🏃 3D Human Motion Analysis using Pose Estimation

## 📌 Overview

This project implements an end-to-end computer vision pipeline for analyzing human motion from video using 3D pose estimation. The system extracts skeletal keypoints from video frames and computes biomechanical features such as joint angles, motion symmetry, and joint velocity.

The pipeline is designed to simulate real-world motion analysis systems used in sports performance and biomechanics, where raw video is transformed into structured motion signals for downstream analysis.

---

## 🎯 Motivation

Modern sports analytics systems rely on computer vision and machine learning to analyze athlete movements at scale. However, real-world data is often noisy, occluded, and captured in unconstrained environments.

This project demonstrates how to:

* Extract structured pose data from raw video
* Handle noisy and imperfect pose detections
* Compute meaningful biomechanical features
* Analyze human motion over time

---

## ⚙️ Tech Stack

* **Python**
* **MediaPipe** – 3D human pose estimation (33 landmarks)
* **OpenCV** – video processing
* **NumPy** – numerical computations
* **Matplotlib** – visualization

---

## 🧠 Methodology

### 1. Video Processing

* Input video is processed frame-by-frame using OpenCV
* Frames are converted to RGB and passed to MediaPipe

### 2. Pose Estimation

* Extracts 33 body landmarks per frame (x, y, z coordinates)
* Tracks key joints including hips, knees, ankles, and shoulders

### 3. Feature Extraction

#### 🔹 Knee Joint Angles

* Computed using three keypoints: **hip → knee → ankle**
* Calculated for both left and right legs

#### 🔹 Motion Symmetry

* Absolute difference between left and right knee angles
* Helps identify imbalance in movement patterns

#### 🔹 Joint Velocity

* Computed from temporal changes in joint positions
* Captures motion dynamics and speed

### 4. Noise Handling

* Applied moving average smoothing to reduce jitter in pose signals
* Improves stability and interpretability of motion features

---

## 📊 Outputs

The pipeline generates:

* Raw knee angle signals (left & right)
* Smoothed knee angle signals
* Symmetry analysis over time
* Joint velocity plots

All outputs are generated programmatically and can be saved locally.

---

## 📂 Project Structure

```text
human-motion-analysis/
├── src/
│   ├── main.py              # Entry point for the pipeline
│   ├── pose_extraction.py  # Video → pose keypoints
│   ├── biomechanics.py     # Feature extraction (angles, velocity, symmetry)
│   └── utils.py            # Plotting and utility functions
│
├── data/                   # Input videos (not tracked in repo)
├── outputs/                # Generated plots (optional)
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your video

Place a test video inside the `data/` folder:

```text
data/sample_video.mp4
```

### 3. Run the pipeline

```bash
python src/main.py
```

---

## 🧪 Example Pipeline

```text
Video → Pose Estimation → Keypoint Extraction → Feature Computation → Motion Analysis
```

---

## ⚠️ Challenges & Learnings

* Pose estimation accuracy degrades under occlusion and non-standard camera angles
* Multi-person scenes can introduce tracking instability
* Raw pose outputs are noisy and require smoothing
* Data quality significantly impacts downstream analysis

---

## 🔍 Key Insights

* Human motion can be represented as time-series data derived from pose landmarks
* Even simple geometric features (angles, velocity) can provide meaningful motion insights
* Robust pipelines must handle imperfect real-world data

---

## 🚀 Future Improvements

* Action classification (walk vs run vs jump)
* Multi-person tracking and identity consistency
* Real-time inference pipeline
* Integration with deep learning models for performance scoring
* Export of structured features to CSV for downstream ML tasks

---

## 💡 Relevance

This project demonstrates core skills in:

* Computer vision pipelines
* Human pose estimation
* Time-series feature extraction
* Motion and biomechanics analysis

These are directly applicable to real-world applications in:

* Sports analytics
* Athlete performance tracking
* Movement analysis systems

---