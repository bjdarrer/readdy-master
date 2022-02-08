mol delete top
mol load xyz out.h5.xyz
mol delrep 0 top
display resetview
mol representation VDW 0.700000 16.0
mol selection name type_0
mol color ColorID 0
mol addrep top
animate goto 0
color Display Background white
molinfo top set {center_matrix} {{{1 0 0 0}{0 1 0 0}{0 0 1 0}{0 0 0 1}}}
