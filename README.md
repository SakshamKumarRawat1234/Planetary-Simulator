Planetary Motion Simulation
Overview

This project is a simulation of planetary motion created using Python and the Pygame library. It demonstrates how planets move around the Sun due to gravitational forces. The simulation uses Newton’s Law of Universal Gravitation to calculate the attraction between celestial bodies and updates their motion over time.

Objective

The goal of this project is to understand how gravitational forces influence planetary motion and to visualize orbital movement through a computer simulation.

Features
Simulates motion of planets around the Sun
Uses real physical constants such as gravitational constant and planetary masses
Displays planetary orbits visually
Shows the path of each planet as it moves
Technologies Used
Python
Pygame
Mathematical calculations using the math module
How the Simulation Works

The program calculates the gravitational force between planets and the Sun. This force determines the acceleration of each planet. The acceleration changes velocity, and velocity updates the planet’s position over time. By repeating this process continuously, the simulation creates orbital motion.

Structure of the Program

The project uses a Planet class that stores:

Position of the planet
Velocity
Mass
Orbit path

Important functions include:

attraction() – calculates gravitational force between planets
update_position() – updates velocity and position
draw() – displays the planet and its orbit on the screen
Limitations
The simulation works in 2D space only
Numerical approximation can introduce small errors over time
Real planetary systems are more complex than this model
Future Improvements
Add more planets and moons
Improve accuracy of calculations
Enhance visualization and graphics
Conclusion

This project helps visualize how gravity controls planetary motion. It demonstrates how physics concepts can be implemented in programming to simulate real-world systems.
