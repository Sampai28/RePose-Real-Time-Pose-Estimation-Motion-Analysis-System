from pathlib import Path

from pose_extraction import PoseExtractor
from biomechanics import (
    compute_knee_angles,
    smooth_signal,
    compute_symmetry,
    compute_joint_speed,
)
from utils import ensure_dir, plot_signals, plot_single_signal


def main():
    video_path = "data/sample_video.mp4"
    output_dir = "outputs"

    if not Path(video_path).exists():
        raise FileNotFoundError(
            f"Video not found at {video_path}. Put your test video inside the data/ folder."
        )

    ensure_dir(output_dir)

    extractor = PoseExtractor()
    try:
        keypoints = extractor.extract_keypoints(video_path)
    finally:
        extractor.close()

    left_angles, right_angles = compute_knee_angles(keypoints)

    left_smooth = smooth_signal(left_angles)
    right_smooth = smooth_signal(right_angles)

    symmetry = compute_symmetry(left_smooth, right_smooth)
    left_knee_speed = compute_joint_speed(keypoints, joint_index=25)

    plot_signals(
        left_angles,
        right_angles,
        title="Raw Knee Angles Over Time",
        ylabel="Angle (degrees)",
        output_path=f"{output_dir}/raw_knee_angles.png",
    )

    plot_signals(
        left_smooth,
        right_smooth,
        title="Smoothed Knee Angles Over Time",
        ylabel="Angle (degrees)",
        output_path=f"{output_dir}/smoothed_knee_angles.png",
    )

    plot_single_signal(
        symmetry,
        title="Left-Right Knee Symmetry",
        ylabel="Absolute Angle Difference",
        output_path=f"{output_dir}/knee_symmetry.png",
    )

    plot_single_signal(
        left_knee_speed,
        title="Left Knee Speed Over Time",
        ylabel="Speed",
        output_path=f"{output_dir}/left_knee_speed.png",
    )

    print("Processing complete.")
    print(f"Detected frames with pose landmarks: {len(keypoints)}")
    print(f"Saved plots to: {output_dir}/")


if __name__ == "__main__":
    main()