# Galaxy Simulator

A Python library for simulating gravity-driven dynamics between stars
and planets.

## Installation

```bash
git clone <repo-url>
cd galaxy_simulator
conda env create -f environment.yml    # or: pip install -r requirements.txt
```

## Quick start

```python
from galaxy_simulator import Galaxy, CelestialObject

HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365
EARTH_YEAR = DAYS_PER_YEAR * HOURS_PER_DAY  # in hours

sun = CelestialObject("Sun", mass=1.989e30, position=(0, 0), velocity=(0, 0))
earth = CelestialObject("Earth", mass=5.972e24,
               position=(1.496e11, 0), velocity=(0, 29_780))

galaxy = Galaxy([sun, earth])  # default dt is 1 hour
galaxy.run(
    steps=EARTH_YEAR,
    save_every=HOURS_PER_DAY,  # one frame per day
    filename="out/trajectory.xyz",
)
```

## Examples

See [examples/solar_system/](examples/solar_system/README.md) for a
simulation with plots.

## Documentation

https://<username>.gitlab.io/galaxy_simulator

## License

GNU General Public License v3.0. See [LICENSE](LICENSE).

