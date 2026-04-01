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

attraction() – calculates gravitational force between planets,

update_position() – updates velocity and position,

draw() – displays the planet and its orbit on the screen,


Limitations:

1.The simulation works in 2D space only

2.Numerical approximation can introduce small errors over time

3.Real planetary systems are more complex than this model


Future Improvements:

1.Add more planets and moons

2.Improve accuracy of calculations

3.Enhance visualization and graphics


What I learned from this project:

While building this simulation, I realized that using the correct formulas is not always enough to get correct results.

At first, I expected the system to behave perfectly if I applied Newton’s law correctly. But over time, I noticed small inaccuracies in the motion, especially when the simulation ran for longer periods.

This made me understand that the way calculations are implemented (step-by-step updates) also affects the outcome. Even small numerical errors can accumulate and change the behavior of the system.

This project helped me move beyond just using formulas to actually thinking about how physical systems are modeled in code.


Conclusion:

This project helps visualize how gravity controls planetary motion. It demonstrates how physics concepts can be implemented in programming to simulate real-world systems.
