import cv2
import mediapipe as mp
import numpy as np


class PoseExtractor:
    def __init__(self, min_detection_confidence: float = 0.5, min_tracking_confidence: float = 0.5):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def extract_keypoints(self, video_path: str) -> np.ndarray:
        cap = cv2.VideoCapture(video_path)
        keypoints = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(image)

            if results.pose_landmarks:
                frame_keypoints = []
                for lm in results.pose_landmarks.landmark:
                    frame_keypoints.append([lm.x, lm.y, lm.z])
                keypoints.append(frame_keypoints)

        cap.release()

        if not keypoints:
            raise ValueError(f"No pose landmarks detected in video: {video_path}")

        return np.array(keypoints, dtype=np.float32)

    def close(self) -> None:
        self.pose.close()