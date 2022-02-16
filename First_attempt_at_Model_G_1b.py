#First attempt at Model G using "Simple example" BJD 9.2.2022 ==========================
#16.2.2022 ##############
import readdy

#Step 1: Set up a reaction diffusion system

#In [2]:
system = readdy.ReactionDiffusionSystem([25.,25.,25.], unit_system=None)
#system.add_species("A", 1.0)  # original 9.2.2022

#BJD added 5 lines below 9.2.2022
system.add_species("A", diffusion_constant=1.0)
system.add_species("B", diffusion_constant=1.0)
system.add_species("G", diffusion_constant=1.0)
system.add_species("X", diffusion_constant=1.0)
system.add_species("Y", diffusion_constant=12.0)
system.add_species("Z", diffusion_constant=1.0)
system.add_species("Omega", diffusion_constant=1.0)
#Define reactions

#In [3]:
#system.reactions.add("myfusion: A +(2) A -> A", rate=10.) # original 9.2.2022
#system.reactions.add("myfission: A -> A +(2) A", rate=3.) # original 9.2.2022
system.reactions.add("conv1: A -> G", rate=1.0)
system.reactions.add("conv2: G -> X", rate=1.0)
system.reactions.add("conv3: X -> G", rate=0.1)
#system.reactions.add("fus1: B +(2) X -> Y + Z", rate=1.0)
#system.reactions.add("fus2: 2X +(2) Y-> 3X", rate=1.0)
system.reactions.add("fus1: B +(2) X -> Y + Z", rate=1.0)
system.reactions.add("fus2: 2X +(2) Y-> 3X", rate=1.0)
system.reactions.add("conv4: X -> Omega", rate=0.9)

#Define potentials

#In [4]:
#system.potentials.add_harmonic_repulsion("A", "A", force_constant=10., 
 #                                        interaction_distance=2.)   # BJD commented out 11.2.2022
#Step 2: Create a corresponding simulation

#In [5]:
simulation = system.simulation(kernel="CPU")

simulation.output_file = "model_g_1_out.h5"
#simulation.output_file = "out_bjd_1b.h5"
#simulation.output_file = "out_bjd_2a.txt"
simulation.reaction_handler = "UncontrolledApproximation"

simulation.add_particle("A", [0.,0.,0.])
simulation.add_particle("B", [0.,0.,0.])
simulation.add_particle("G", [0.,0.,0.])
simulation.add_particle("X", [0.,0.,0.])
simulation.add_particle("Y", [0.,0.,0.])
simulation.add_particle("Z", [0.,0.,0.])
simulation.add_particle("Omega", [0.,0.,0.])

simulation.record_trajectory(stride=1)
#simulation.observe.number_of_particles(stride=100, callback=lambda n: print("#A:", n))
simulation.observe.number_of_particles(stride=100, callback=lambda n: print("#A:", n, "#B", n, "#G:", n,
             "#X", n,"#Y:", n, "#Z", n,"#Omega:", n))
#Step 3: Run the simulation
#In [6]:

simulation.run(n_steps=3000, timestep=1e-2)

#Step 4: Look at results

#In [7]:
trajectory = readdy.Trajectory('model_g_1_out.h5')
#trajectory.convert_to_xyz(particle_radii={'A': 1.})
trajectory.convert_to_xyz(particle_radii={'A': 1.,'B': 1., 'G': 1., 'X': 1.,
             'Y': 1., 'Z': 1., 'Omega': 1.})

#Visualize in VMD

#In [8]:
#!vmd -e out.xyz.tcl
#should be:     !vmd -e out.h5.xyz.tcl
"""
import h5py

filename = "vstoxx_data_31032014.h5"

h5 = h5py.File(filename,'r')

futures_data = h5['futures_data']  # VSTOXX futures data
options_data = h5['options_data']  # VSTOXX call option data

h5.close()
"""