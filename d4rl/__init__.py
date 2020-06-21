import os
import sys

import d4rl.locomotion
import d4rl.hand_manipulation_suite
import d4rl.pointmaze
import d4rl.gym_minigrid
import d4rl.gym_mujoco
from d4rl.offline_env import set_dataset_path, get_keys

SUPPRESS_MESSAGES = bool(os.environ.get('D4RL_SUPPRESS_IMPORT_ERROR', 0))

_ERROR_MESSAGE = 'Warning: %s failed to import. Set the environment variable D4RL_SUPPRESS_IMPORT_ERROR=1 to suppress this message.'

try:
    import d4rl.flow
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % 'Flow', file=sys.stderr)
        print(e, file=sys.stderr)

try:
    import d4rl.kitchen
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % 'FrankaKitchen', file=sys.stderr)
        print(e, file=sys.stderr)

try:
    import d4rl.carla
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % 'CARLA', file=sys.stderr)
        print(e, file=sys.stderr)


import d4rl.infos
def get_dataset(env_name):
    import h5py
    dataset_url = d4rl.infos.DATASET_URLS[env_name]
    h5path = download_dataset_from_url(dataset_url)
    dataset_file = h5py.File(h5path, 'r')
    data_dict = {k: dataset_file[k][:] for k in get_keys(dataset_file)}
    dataset_file.close()
    return data_dict


def get_dataset_key(env_name, key):
    import h5py
    dataset_url = d4rl.infos.DATASET_URLS[env_name]
    h5path = download_dataset_from_url(dataset_url)
    with h5py.File(h5path, 'r') as h5file:
        data = h5file[key][:]
    return data

def get_normalized_score(env_name, score):
    ref_min_score = d4rl.infos.REF_MIN_SCORE[env_name]
    ref_max_score = d4rl.infos.REF_MAX_SCORE[env_name]
    return (score - ref_min_score) / (ref_max_score - ref_min_score)

