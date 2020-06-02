import d4rl.locomotion
import d4rl.hand_manipulation_suite
import d4rl.pointmaze
import d4rl.gym_minigrid
import d4rl.gym_mujoco
from d4rl.offline_env import set_dataset_path, download_dataset_from_url, get_keys
import d4rl.infos

try:
    import d4rl.flow
except ImportError:
    print('Warning: Flow failed to import')

try:
    import d4rl.kitchen
except ImportError:
    print('Warning: FrankaKitchen failed to import. Install the adept_envs package.')

try:
    import d4rl.carla
except ImportError:
    print('Warning: Carla failed to import')


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

