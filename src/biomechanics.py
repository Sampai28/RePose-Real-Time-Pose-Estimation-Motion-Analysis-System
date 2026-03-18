import numpy as np


LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28


def calculate_angle(a, b, c) -> float:
    a = np.array(a, dtype=np.float32)
    b = np.array(b, dtype=np.float32)
    c = np.array(c, dtype=np.float32)

    ba = a - b
    bc = c - b

    denominator = np.linalg.norm(ba) * np.linalg.norm(bc)
    if denominator == 0:
        return np.nan

    cosine_angle = np.dot(ba, bc) / denominator
    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)

    angle = np.arccos(cosine_angle)
    return float(np.degrees(angle))


def compute_knee_angles(keypoints: np.ndarray):
    left_angles = []
    right_angles = []

    for frame in keypoints:
        left_angle = calculate_angle(
            frame[LEFT_HIP], frame[LEFT_KNEE], frame[LEFT_ANKLE]
        )
        right_angle = calculate_angle(
            frame[RIGHT_HIP], frame[RIGHT_KNEE], frame[RIGHT_ANKLE]
        )

        left_angles.append(left_angle)
        right_angles.append(right_angle)

    return np.array(left_angles), np.array(right_angles)


def smooth_signal(signal: np.ndarray, window: int = 7) -> np.ndarray:
    if len(signal) < window:
        return signal
    kernel = np.ones(window) / window
    return np.convolve(signal, kernel, mode="valid")


def compute_symmetry(left_signal: np.ndarray, right_signal: np.ndarray) -> np.ndarray:
    min_len = min(len(left_signal), len(right_signal))
    return np.abs(left_signal[:min_len] - right_signal[:min_len])


def compute_joint_speed(keypoints: np.ndarray, joint_index: int = LEFT_KNEE) -> np.ndarray:
    joint_positions = keypoints[:, joint_index, :]
    velocity = np.diff(joint_positions, axis=0)
    speed = np.linalg.norm(velocity, axis=1)
    return speed