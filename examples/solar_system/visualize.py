"""Plotting and animation of saved XYZ trajectories."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

AU_IN_METERS = 1.496e11
SECONDS_PER_DAY = 86_400


def read_xyz(filename):
    """Return (names, times, positions) from an XYZ trajectory.

    ``positions`` has shape (frames, bodies, 2) and is in metres.
    """
    names, times, positions = [], [], []
    with open(filename) as file:
        lines = file.read().splitlines()

    i = 0
    while i < len(lines):
        n = int(lines[i])
        times.append(float(lines[i + 1].split("=")[1]))
        rows = [line.split() for line in lines[i + 2 : i + 2 + n]]
        names = [row[0] for row in rows]
        positions.append([[float(row[1]), float(row[2])] for row in rows])
        i += n + 2

    return names, np.array(times), np.array(positions)


def plot_orbits(filename, save_as=None):
    """Static plot of every body's full path.

    Pass ``save_as="orbits.png"`` to save the image instead of showing it.
    """
    names, _, positions = read_xyz(filename)
    positions = positions / AU_IN_METERS

    fig, ax = plt.subplots()
    for j, name in enumerate(names):
        ax.plot(positions[:, j, 0], positions[:, j, 1], label=name)
        ax.plot(*positions[-1, j], "o")

    ax.set_aspect("equal")
    ax.set_xlabel("x (AU)")
    ax.set_ylabel("y (AU)")
    ax.legend()
    if save_as:
        fig.savefig(save_as, dpi=150, bbox_inches="tight")
    else:
        plt.show()


def animate(filename, trail=30, save_as=None):
    """Animate the bodies moving, each with a short trail.

    ``trail`` is the number of past frames drawn behind each body.
    Pass ``save_as="orbit.gif"`` to save the animation instead of showing it.
    """
    names, times, positions = read_xyz(filename)
    positions = positions / AU_IN_METERS

    fig, ax = plt.subplots()
    limit = 1.1 * np.abs(positions).max()
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")
    ax.set_xlabel("x (AU)")
    ax.set_ylabel("y (AU)")

    dots = [ax.plot([], [], "o", label=name)[0] for name in names]
    trails = [ax.plot([], [], "-", alpha=0.5, color=dot.get_color())[0] for dot in dots]
    ax.legend(loc="upper right")

    def update(frame):
        start = max(0, frame - trail)
        for j in range(len(names)):
            dots[j].set_data([positions[frame, j, 0]], [positions[frame, j, 1]])
            trails[j].set_data(
                positions[start : frame + 1, j, 0], positions[start : frame + 1, j, 1]
            )
        ax.set_title(f"t = {times[frame] / SECONDS_PER_DAY:.0f} days")
        return dots + trails

    animation = FuncAnimation(fig, update, frames=len(times), interval=30)
    if save_as:
        animation.save(save_as, writer="pillow", fps=30)
    else:
        plt.show()