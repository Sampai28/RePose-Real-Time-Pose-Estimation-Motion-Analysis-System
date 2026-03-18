from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def plot_signals(
    left_signal: np.ndarray,
    right_signal: np.ndarray,
    title: str,
    ylabel: str,
    output_path: str | None = None,
) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(left_signal, label="Left")
    plt.plot(right_signal, label="Right")
    plt.title(title)
    plt.xlabel("Frame")
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()

    plt.close()


def plot_single_signal(
    signal: np.ndarray,
    title: str,
    ylabel: str,
    output_path: str | None = None,
) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(signal)
    plt.title(title)
    plt.xlabel("Frame")
    plt.ylabel(ylabel)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()

    plt.close()