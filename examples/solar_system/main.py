from galaxy_simulator import Galaxy, CelestialObject
from visualize import animate, plot_orbits

HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365
EARTH_YEAR = DAYS_PER_YEAR * HOURS_PER_DAY  # in hours

trajectory = "out/trajectory.xyz"
orbits_image = "out/orbits.png"


def main():
    sun = CelestialObject("Sun", mass=1.989e30, position=(0, 0), velocity=(0, 0))
    earth = CelestialObject("Earth", mass=5.972e24,
                   position=(1.496e11, 0), velocity=(0, 29_780))

    solar_system = Galaxy([sun, earth], dt=3600.0)  # 1-hour steps
    solar_system.run(
        steps=2 * EARTH_YEAR,  # two years
        save_every=HOURS_PER_DAY,  # one frame per day
        filename=trajectory,
    )
    plot_orbits(trajectory, save_as=orbits_image)
    # animate(trajectory)  # uncomment to watch the bodies move


if __name__ == "__main__":
    main()