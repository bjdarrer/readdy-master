#Bimolecular reaction - well mixed - BJD 8.2.2022 
# https://readdy.github.io/validation/bimolecular_reaction

#In [1]:
import os
import numpy as np
import matplotlib.pyplot as plt
import readdy
#In [2]:
#readdy.__version__
#Out[2]:
#'v2.0.3-27'

#Setup ReaDDy system

#In [3]:
system = readdy.ReactionDiffusionSystem([20.,20.,20.], temperature=300.*readdy.units.kelvin)

system.add_species("A", diffusion_constant=1.0)
system.add_species("B", diffusion_constant=1.0)
system.add_species("C", diffusion_constant=1.0)

lambda_on = 1.
system.reactions.add("myfusion: A +(1) B -> C", rate=lambda_on/readdy.units.nanosecond)

#Simulate the system

#In [4]:
simulation = system.simulation(kernel="CPU")
#simulation.output_file = "out.h5"  # original see line below
simulation.output_file = "Bimolecular_out.h5" # BJD 8.2.2022
simulation.reaction_handler = "Gillespie"

n_particles = 2000
initial_positions_a = np.random.random(size=(n_particles, 3)) * 20. - 10.
initial_positions_b = np.random.random(size=(n_particles, 3)) * 20. - 10.
simulation.add_particles("A", initial_positions_a)
simulation.add_particles("B", initial_positions_b)

simulation.observe.number_of_particles(stride=1, types=["A"])

#In [5]:
if os.path.exists(simulation.output_file):
    os.remove(simulation.output_file)

simulation.run(n_steps=5000, timestep=1e-3*readdy.units.nanosecond)
#  0%|          | 2/500 [00:00<00:39, 12.64it/s]

#Configured kernel context with:
"""
--------------------------------
 - kBT = 2.49434
 - periodic b.c. = (true, true, true)
 - box size = (20.0, 20.0, 20.0)
 - particle types:
     *  particle type "C" with D=1.0
     *  particle type "A" with D=1.0
     *  particle type "B" with D=1.0
 - bimolecular reactions:
     * Fusion A + B -> C with a rate of 1.0, an educt distance of 1.0, and weights 0.5 and 0.5

Configured simulation loop with:
--------------------------------
 - timeStep = 0.00100000
 - evaluateObservables = true
 - progressOutputStride = 100
 - context written to file = true
 - Performing actions:
   * Initialize neighbor list? true
   * Update neighbor list? true
   * Clear neighbor list? true
   * Integrate diffusion? true
   * Calculate forces? true
   * Handle reactions? true
   * Handle topology reactions? true
"""

#100%|██████████| 500/500 [00:17<00:00, 28.56it/s]
#In [6]:
traj = readdy.Trajectory(simulation.output_file)
time, counts = traj.read_observable_number_of_particles()

#Analytical solution

#[1]: R. Erban and J. Chapman, “Stochastic modelling of reaction-diffusion processes: algorithms for bimolecular reactions.,” Phys. Biol., vol. 6, no. 4, p. 46001, Jan. 2009.
# https://people.maths.ox.ac.uk/erban/papers/BimolecularReactions.pdf

#In [7]:
kappa = np.sqrt(lambda_on / 2.)
k_on = 4. * np.pi * 2. * 1. * (1. - np.tanh(kappa * 1.) / (kappa * 1.) )

def a(t): 
    return 1. / ((system.box_volume.magnitude / n_particles) + k_on * t)

t_range = np.linspace(0., 5000 * 1e-3, 10000)

#In [8]:
plt.plot(time[::200]*1e-3, counts[::200] / system.box_volume.magnitude, "x", label="ReaDDy")
plt.plot(t_range, a(t_range), label=r"analytical $a(t)$")
plt.legend(loc="best")
plt.xlabel("time in nanoseconds")
plt.ylabel(r"concentration in nm$^{-3}$")
plt.show()

