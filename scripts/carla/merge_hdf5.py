import h5py
import os
import numpy as np
from d4rl.offline_env import get_keys

FILES = ['output_%d.hdf5' % i for i in range(12)]

output_file = h5py.File('carla_town-v0.hdf5', 'w')
input_files = [h5py.File(fname, 'r') for fname in FILES]

keys = get_keys(input_files[0])

"""
for k in keys:
    data = [input_file[k] for input_file in input_files]
    data = np.concatenate(data)
    print(k, data.shape)
    output_file.create_dataset(k, data=data, compression='gzip')
"""

for k in keys:
    total_size = sum([input_file[k].shape[0] for input_file in input_files])
    shape = input_files[0][k].shape[1:]
    total_shape = (total_size,)+shape
    print(k, total_shape)

    layout = h5py.VirtualLayout(shape=total_shape, dtype=np.float32)

    sources = []
    offset = 0
    for i, input_f in enumerate(input_files):
        virtual_k = 'virtual/%d/%s' % (i, k)
        output_file.create_dataset(virtual_k, data=input_f[k], compression='gzip')
        #vsource = h5py.VirtualSource(input_f[k])
        vsource = h5py.VirtualSource(output_file[virtual_k])
        length = vsource.shape[0]
        layout[offset : offset + length] = vsource
        offset += length

    output_file.create_virtual_dataset(k, layout, fillvalue=0)

