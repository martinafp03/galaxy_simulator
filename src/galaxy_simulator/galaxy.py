import numpy as np
from pathlib import Path


class Galaxy:
    # maps integrator name -> method name
    INTEGRATORS = {"velocity_verlet": "_velocity_verlet_step"}

    def __init__(
        self,
        celestial_bodies=None,
        G=6.674e-11,  # gravitational constant, SI units
        time=0.0,
        dt=3600.0,  # time step in seconds (1 hour)
        integrator="velocity_verlet",
    ):
        if integrator not in self.INTEGRATORS:
            raise ValueError(f"Unknown integrator {integrator!r}")
        self.celestial_bodies = list(celestial_bodies) if celestial_bodies else []
        self.G = G
        self.time = time
        self.dt = dt
        self.integrator = integrator

    def add_body(self, celestial_body):
        self.celestial_bodies.append(celestial_body)

    def accelerations(self):
        positions = np.array(
            [celestial_body.position for celestial_body in self.celestial_bodies]
        )
        masses = np.array(
            [celestial_body.mass for celestial_body in self.celestial_bodies]
        )

        separation = positions[np.newaxis, :, :] - positions[:, np.newaxis, :]
        distance = np.linalg.norm(separation, axis=-1)
        np.fill_diagonal(distance, np.inf)  # a body exerts no force on itself

        weights = masses[np.newaxis, :] / distance**3
        return self.G * np.einsum("ij,ijk->ik", weights, separation)

    def _velocity_verlet_step(self):
        dt = self.dt
        acc_old = self.accelerations()
        for celestial_body, a in zip(self.celestial_bodies, acc_old):
            celestial_body.position = (
                celestial_body.position + celestial_body.velocity * dt + 0.5 * a * dt**2
            )

        acc_new = self.accelerations()
        for celestial_body, a_old, a_new in zip(
            self.celestial_bodies, acc_old, acc_new
        ):
            celestial_body.velocity = (
                celestial_body.velocity + 0.5 * (a_old + a_new) * dt
            )

    def step(self):
        if not self.celestial_bodies:
            return
        getattr(self, self.INTEGRATORS[self.integrator])()
        self.time += self.dt

    def run(self, steps):
        for _ in range(steps):
            self.step()

    def run(self, steps, save_every=None, filename="out/trajectory.xyz"):
        if save_every is None:
            for _ in range(steps):
                self.step()
            return

        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "w") as file:
            self.write_xyz_frame(file)
            for i in range(1, steps + 1):
                self.step()
                if i % save_every == 0:
                    self.write_xyz_frame(file)

    def write_xyz_frame(self, file):
        file.write(f"{len(self.celestial_bodies)}\n")
        file.write(f"time={self.time}\n")
        for celestial_body in self.celestial_bodies:
            x, y = celestial_body.position
            file.write(f"{celestial_body.name} {x:.6e} {y:.6e} 0.0\n")
