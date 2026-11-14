from enum import Enum

class PlanetType(Enum):
    TERRESTRIAL = "Terrestrial"
    JOVIAN = "Jovian"

class Planet:

    bbb = "bbbbb"

    """
    Represents a planet and its main physical characteristics.
    """
    def __init__(
        self,
        name,
        mass_in_kg,
        orbital_velocity,
        mean_temperature,
        length_of_day,
        distance_from_sun,
        planet_type,
        ):


        Planet.bbb = 124
        self.name = name
        self.mass_in_kg = mass_in_kg
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    @staticmethod
    def print_smth():
        print ("smth")

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass_in_kg

    def get_velocity(self):
        return self.orbital_velocity

    def get_temperature(self):
        return self.mean_temperature

    def get_length_of_day(self):
        return self.length_of_day

    def get_distance_from_sun(self):
        return self.distance_from_sun

    def get_planet_type(self):
        return self.planet_type

    

    def __str__(self):
        return (f"Planet: {self.name} | Mass: {self.mass_in_kg} | Orbital Velocity: {self.orbital_velocity} | "
                f"Mean Temperature: {self.mean_temperature} | Length of Day: {self.length_of_day} | Distance from Sun: {self.distance_from_sun} | "
                f"Type: {self.planet_type.value}")

    def __repr__(self):
        return (
            f"Planet(name={self.name!r}, "
            f"mass_in_kg={self.mass_in_kg!r}, "
            f"orbital_velocity={self.orbital_velocity!r}, "
            f"mean_temperature={self.mean_temperature!r}, "
            f"length_of_day={self.length_of_day!r}, "
            f"distance_from_sun={self.distance_from_sun!r}, "
            f"planet_type={self.planet_type!r})"
        )

    def __del__(self):
        print(f"Planet {self.name} had been destroyed.")



class Planetary:
    def __init__(self):
        self.__planets = []

    def add_planet(self, planet):
        self.__planets.append(planet)

    def show_planets(self):
        for planet in self.__planets:
            print(planet)

    def sort_by_day_length(self):
        self.__planets.sort(
            key=lambda planet: planet.length_of_day
        )

    def findAverageMass(self, planets=None):
        if planets is None:
            planets = self.__planets

        if len(planets) == 0:
            return 0

        total_mass = sum(
            planet.mass_in_kg for planet in planets
        )

        return total_mass / len(planets)



def findDistanceBetween(planetA, planetB):
    distance = abs(
        planetA.distance_from_sun - planetB.distance_from_sun
    )
    return distance



def main():
    earth = Planet(
        "Earth",
        5.972e24,
        29.78,
        15,
        23.93,
        149.6,
        PlanetType.TERRESTRIAL
    )

    mars = Planet(
        "Mars",
        6.417e23,
        24.07,
        -65,
        24.62,
        227.9,
        PlanetType.TERRESTRIAL
    )

    jupiter = Planet(
        "Jupiter",
        1.898e27,
        13.07,
        -110,
        9.93,
        778.6,
        PlanetType.JOVIAN
    )

    solar_system = Planetary()

    solar_system.add_planet(mars)
    solar_system.add_planet(earth)
    solar_system.add_planet(jupiter)

    print("Before sorting:")
    solar_system.show_planets()

    solar_system.sort_by_day_length()

    print("\nAfter sorting:")
    solar_system.show_planets()

    print(f"Distance difference: {findDistanceBetween(earth, mars):.2f} million km")

    average_all = solar_system.findAverageMass()
    average_selected = solar_system.findAverageMass([mars, earth])

    print(f"Average mass (all): {average_all:.3e} kg")
    print(f"Average mass (Mars & Earth): {average_selected:.3e} kg")

    print(earth.mass_in_kg)
    print(Planet.bbb)

    Planet.print_smth()

main()