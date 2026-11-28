import numpy as np
from galaxy_simulator import Galaxy, CelestialObject

def test_accelerations_follow_newtons_law():
    a = CelestialObject("A", mass=2.0, position=(0, 0), velocity=(0, 0))
    b = CelestialObject("B", mass=3.0, position=(2, 0), velocity=(0, 0))
    acc = Galaxy([a, b], G=1.0).accelerations()
    np.testing.assert_allclose(acc[0], [3 / 4, 0])
    np.testing.assert_allclose(acc[1], [-2 / 4, 0])