# Solar system example

Simulates the Sun and Earth with `galaxy_simulator` and plots the orbit.

## Run

With the environment installed:

```bash
cd examples/solar_system
python main.py
```

## How it works

- `main.py` creates the Sun and Earth, simulates two years in one-hour
  steps and saves one frame per day to `out/trajectory.xyz`.
- `visualise.py` reads that file and plots each body's orbit to
  `out/orbits.png`.

To add a planet, create a `CelestialObject` in `main.py` and call
`solar_system.add_body(...)`.