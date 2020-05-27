from .carla_env import CarlaObsDictEnv
from gym.envs.registration import register

# Smaller dataset with only positive demonstrations.
register(
    id='carla-lane-v0',
    entry_point='d4rl.carla:CarlaObsDictEnv',
    max_episode_steps=1000,
    kwargs={
        'ref_min_score': 367.10279107891745,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/carla/carla_lane_follow-v0.hdf5',
        'carla_args': dict(
            vision_size=48,
            vision_fov=48,
            weather=False,
            frame_skip=1,
            steps=100000,
            multiagent=True,
            lane=0,
            lights=False,
            record_dir="None",
        )
    }
)


