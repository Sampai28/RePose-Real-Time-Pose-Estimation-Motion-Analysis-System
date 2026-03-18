# 🏃 Human Motion Analysis using 3D Pose Estimation

## 📌 Overview

This project builds an end-to-end computer vision pipeline to analyze human motion from video using 3D pose estimation. The system extracts skeletal keypoints from video frames and computes biomechanical features such as joint angles, motion symmetry, and joint velocity.

The goal is to simulate real-world motion analysis systems used in sports performance and biomechanics, where understanding movement patterns is critical for performance optimization and injury prevention.

---

## 🎯 Motivation

Modern sports analytics systems rely heavily on computer vision to track and analyze athlete movements. However, real-world data is often noisy, occluded, and captured in unconstrained environments.

This project demonstrates how to:

* Extract structured motion data from raw video
* Handle noisy pose detections
* Compute meaningful biomechanical features
* Analyze motion patterns over time

---

## ⚙️ Tech Stack

* **Python**
* **OpenCV** – video processing
* **MediaPipe** – 3D pose estimation (33 keypoints)
* **NumPy** – numerical computations
* **Matplotlib** – visualization

---

## 🧠 Methodology

### 1. Video Processing

* Input video is processed frame-by-frame
* Frames are converted to RGB and passed to MediaPipe Pose

### 2. Pose Estimation

* Extract 33 body landmarks per frame (x, y, z)
* Landmarks represent key joints such as hips, knees, ankles, and shoulders

### 3. Feature Extraction

#### 🔹 Knee Joint Angles

* Computed using three points: hip → knee → ankle
* Calculated for both left and right legs

#### 🔹 Motion Symmetry

* Absolute difference between left and right knee angles
* Used to detect imbalance in movement

#### 🔹 Joint Velocity

* Temporal change in joint positions across frames
* Used to estimate motion dynamics

### 4. Noise Handling

* Applied moving average smoothing to reduce jitter in pose signals
* Improved stability of biomechanical measurements

---

## 📊 Results

* Successfully extracted consistent pose landmarks from real-world videos
* Generated time-series plots for:

  * Left & right knee angles
  * Smoothed motion curves
  * Symmetry analysis
  * Joint velocity
* Demonstrated robustness under moderate occlusion and background noise

---

## ⚠️ Challenges & Learnings

* Pose estimation accuracy degrades under occlusion and camera angle variation
* Multi-person scenes can lead to unstable tracking
* Raw pose outputs are noisy and require smoothing
* Data quality significantly impacts downstream analysis

---

## 🚀 Future Improvements

* Multi-person tracking and identity consistency
* Action classification (walk vs run vs jump)
* Real-time inference pipeline
* Integration with deep learning models for performance scoring
* Deployment for edge/mobile devices

---

## 🧪 How to Run

```bash
git clone https://github.com/your-username/human-motion-analysis.git
cd human-motion-analysis
pip install -r requirements.txt
```

Run the main notebook/script to process a sample video and generate plots.

---

## 📂 Project Structure

```
human-motion-analysis/
│
├── data/           
├── outputs/            
├── src/                 
├── notebooks/        
├── requirements.txt
└── README.md
```

---

## 💡 Key Takeaway

This project demonstrates how raw video can be transformed into structured motion data and actionable biomechanical insights using computer vision techniques.

---

## 🔗 Author

Sameer Saxena
[GitHub](https://github.com/Sampai28)
