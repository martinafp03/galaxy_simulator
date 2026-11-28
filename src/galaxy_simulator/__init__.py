"""Galaxy Simulator: gravity-driven dynamics between stars and planets."""

from importlib.metadata import version

__version__ = version("galaxy_simulator")  # read from pyproject.toml

from galaxy_simulator.CelestialObject import CelestialObject
from galaxy_simulator.galaxy import Galaxy

__all__ = ["CelestialObject", "Galaxy"]


