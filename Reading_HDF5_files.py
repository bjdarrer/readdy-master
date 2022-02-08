import numpy as np
import h5py

#Reading HDF5 files
#To open and read data we use the same File method in read mode, r.
hf = h5py.File('out_bjd_1a.h5', 'r')

#To see what data is in this file, we can call the keys() method on the file object.

hf.keys()
[u'group1']

#We can then grab each dataset we created above using the get method, specifying the name.
n1 = hf.get('dataset_1')
n1

#This returns a HDF5 dataset object. To convert this to an array, just call numpy’s array method.
n1 = np.array(n1)
n1.shape
(1000, 20)
hf.close()