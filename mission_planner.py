# Space Mission Planner

# TODO: Import the functions from space_math.py
from space_math import calculate_fuel, time_to_destination, gravity_force

# Mission parameters
distance = 225000000  # km
speed = 20000  # km/h
planet_mass = 6.39e23  # kg
spacecraft_mass = 15000  # kg

# TODO: Use the imported functions to calculate mission details
fuel_needed = calculate_fuel(distance)
travel_time = time_to_destination(distance, speed)
grav_force = gravity_force(planet_mass, spacecraft_mass, distance)
# TODO: Print the mission details (fuel needed, time to destination, gravitational force)
print("Space Mission Details:", distance)
print("----------------------")
print(f"Fuel needed: {fuel_needed:.2f} liters")
print(f"Time to destination: {travel_time:.2f} hours")
print(f"Gravitational force at destination: {grav_force:.2f} N")
