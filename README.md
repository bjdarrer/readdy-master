# ![ReaDDy](https://readdy.github.io/assets/readdy_black_150px.png "ReaDDy logo") #

[![Build Status](https://dev.azure.com/clonker/readdy/_apis/build/status/readdy.readdy?branchName=master)](https://dev.azure.com/clonker/readdy/_build/latest?definitionId=5&branchName=master)

ReaDDy (**Rea**ction **D**iffusion **Dy**namics) is an open source particle based reaction-diffusion simulator that can be configured and run via Python.
Currently supported platforms are Mac and Linux.

# Installation
The preferred way of installing the software is by using the conda package manager:
```bash
# optional: create environment for readdy, switch to that environment
conda create -n readdy
conda activate readdy

# add conda-forge channel
conda config --env --add channels conda-forge

# install readdy with a specified Python version
conda install python=3.9 readdy
```

# Documentation
A documentation and a few examples are provided at [https://readdy.github.io/](https://readdy.github.io/).

# Core features
- particle based simulation of reaction-diffusion systems in 3D
- particles diffuse via Brownian dynamics
- reactions between single instances of particles (unimolecularly and bimolecularly)
- particle interaction potentials for modeling
  - space exclusion
  - molecular crowding
  - aggregation
- particle complexes via harmonic bonds, angles, and cosine dihedrals for modeling, e.g.,
  - domain structure
  - polymer chains
- spatially and temporally triggered changes in the particle complexes
- simulation output in a compact hdf5 file
- single-threaded and pthread-parallelized implementations available
