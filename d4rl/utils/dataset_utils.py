import h5py
import numpy as np

class DatasetWriter(object):
    def __init__(self, mujoco=False, goal=False, extra_keys=set()):
        self.mujoco = mujoco
        self.goal = goal
        self.extra_keys = extra_keys
        self.data = self._reset_data()
        self._num_samples = 0

    def _reset_data(self):
        data = {'observations': [],
            'actions': [],
            'terminals': [],
            'rewards': [],
            }
        if self.mujoco:
            data['infos/qpos'] = []
            data['infos/qvel'] = []
        if self.goal:
            data['infos/goal'] = []
        for k in self.extra_keys:
            data['infos/'+k] = []
        return data

    def __len__(self):
        return self._num_samples

    def append_data(self, s, a, r, done, goal=None, mujoco_env_data=None, **extra_keys):
        self._num_samples += 1
        self.data['observations'].append(s)
        self.data['actions'].append(a)
        self.data['rewards'].append(r)
        self.data['terminals'].append(done)
        if self.goal:
            self.data['infos/goal'].append(goal)
        if self.mujoco:
            self.data['infos/qpos'].append(mujoco_env_data.qpos.ravel().copy())
            self.data['infos/qvel'].append(mujoco_env_data.qvel.ravel().copy())
        for k in self.extra_keys:
            self.data['infos/'+k].append(extra_keys[k])

    def write_dataset(self, fname, max_size=None, compression='gzip'):
        np_data = {}
        for k in self.data:
            if k == 'terminals':
                dtype = np.bool_
            else:
                dtype = np.float32
            data = np.array(self.data[k], dtype=dtype)
            if max_size is not None:
                data = data[:max_size]
            np_data[k] = data

        dataset = h5py.File(fname, 'w')
        for k in np_data:
            dataset.create_dataset(k, data=np_data[k], compression=compression)
        dataset.close()

