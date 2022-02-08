import h5py

filename = "out_bjd_1a.h5"

h5 = h5py.File(filename,'r')

futures_data = h5['futures_data']  # VSTOXX futures data
options_data = h5['options_data']  # VSTOXX call option data

h5.close()