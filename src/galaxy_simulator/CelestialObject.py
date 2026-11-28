import numpy as np



class CelestialObject:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.asarray(position, dtype=float)
        self.velocity = np.asarray(velocity, dtype=float)

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * float(self.velocity @ self.velocity)

    def __str__(self):
        return (
            f"CelestialObject(name={self.name!r}, mass={self.mass}, "
            f"position={self.position.tolist()}, velocity={self.velocity.tolist()})"
        )
