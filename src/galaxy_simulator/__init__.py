"""Galaxy Simulator: gravity-driven dynamics between stars and planets."""

from importlib.metadata import version

__version__ = version("galaxy_simulator")  # read from pyproject.toml

from galaxy_simulator.planet import Planet

__all__ = ["Planet"]
