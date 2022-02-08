import readdy

#Step 1: Set up a reaction diffusion system

#In [2]:
system = readdy.ReactionDiffusionSystem([25.,25.,25.], temperature=300.*readdy.units.kelvin)
system.add_species("A", 1.0)

#Define reactions

#In [3]:
system.reactions.add("myfusion: A +(2) A -> A", rate=10.)
system.reactions.add("myfission: A -> A +(2) A", rate=3.)

#Define potentials

#In [4]:
system.potentials.add_harmonic_repulsion("A", "A", force_constant=10., 
                                         interaction_distance=2.)
#Step 2: Create a corresponding simulation

#In [5]:
simulation = system.simulation(kernel="CPU")

simulation.output_file = "out_bjd_1b.h5"
#simulation.output_file = "out_bjd_2a.txt"
simulation.reaction_handler = "UncontrolledApproximation"

simulation.add_particle("A", [0.,0.,0.])

simulation.record_trajectory(stride=1)
simulation.observe.number_of_particles(stride=100, callback=lambda n: print("#A:", n))

#Step 3: Run the simulation

#In [6]:

simulation.run(n_steps=3000, timestep=1e-2)

#Visualize in VMD

#In [8]:
#!vmd -e out.xyz.tcl
#!vmd -e out.xyz.tcl
"""
import h5py

filename = "vstoxx_data_31032014.h5"

h5 = h5py.File(filename,'r')

futures_data = h5['futures_data']  # VSTOXX futures data
options_data = h5['options_data']  # VSTOXX call option data

h5.close()
"""