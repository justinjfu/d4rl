import gym
import os
import d4rl
from d4rl import offline_env
from d4rl import infos
#import d4rl.flow
import shutil

ENVS = [
    'maze2d-umaze-v1',
    'maze2d-medium-v1',
    'maze2d-large-v1',
    'pen-human-v0',
    'pen-cloned-v0',
    'pen-expert-v0',
    'hammer-human-v0',
    'hammer-cloned-v0',
    'hammer-expert-v0',
    'relocate-human-v0',
    'relocate-cloned-v0',
    'relocate-expert-v0',
    'door-human-v0',
    'door-cloned-v0',
    'door-expert-v0',
    'halfcheetah-random-v0',
    'halfcheetah-medium-v0',
    'halfcheetah-expert-v0',
    'halfcheetah-medium-replay-v0',
    'halfcheetah-medium-expert-v0',
    'walker2d-random-v0',
    'walker2d-medium-v0',
    'walker2d-expert-v0',
    'walker2d-medium-replay-v0',
    'walker2d-medium-expert-v0',
    'hopper-random-v0',
    'hopper-medium-v0',
    'hopper-expert-v0',
    'hopper-medium-replay-v0',
    'hopper-medium-expert-v0',
    'antmaze-umaze-v0',
    'antmaze-umaze-diverse-v0',
    'antmaze-medium-play-v0',
    'antmaze-medium-diverse-v0',
    'antmaze-large-play-v0',
    'antmaze-large-diverse-v0',
    'kitchen-complete-v0',
    'kitchen-partial-v0',
    'kitchen-mixed-v0',
]

FENVS = [
    'flow-ring-controller-v0',
    'flow-ring-random-v0',
    'flow-merge-controller-v0',
    'flow-merge-random-v0',
]

if __name__ == '__main__':
    for env_name in ENVS:
        print('Preparing', env_name)
        dataset_url = infos.DATASET_URLS[env_name]
        dataset_filepath = offline_env.filepath_from_url(dataset_url)
        #env.get_dataset()
        _, dataset = os.path.split(dataset_filepath)
        dirname, _ = os.path.splitext(dataset)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
            shutil.copyfile(dataset_filepath, os.path.join(dirname, dataset))


