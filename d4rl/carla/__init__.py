from .carla_env import CarlaObsDictEnv
from .carla_env import CarlaObsEnv
from gym.envs.registration import register

# Smaller dataset with only positive demonstrations.
register(
    id='carla-lane-v0',
    entry_point='d4rl.carla:CarlaObsEnv',
    max_episode_steps=250,
    kwargs={
        'ref_min_score': 7.901258360189125, 
        #147.4916833225875 - random, no perp penalty
        'ref_max_score': 1253.3230534670868, # 250 steps
        # 632.3039350495891 - avg gent [0.33, 0]
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/carla/carla_lane_follow_flat-v0.hdf5',
        'carla_args': dict(
            vision_size=48,
            vision_fov=48,
            weather=False,
            frame_skip=1,
            steps=250,
            multiagent=True,
            lane=0,
            lights=False,
            record_dir="None",
        )
    }
)

register(
    id='carla-lane-dict-v0',
    entry_point='d4rl.carla:CarlaObsDictEnv',
    max_episode_steps=250,
    kwargs={
        'ref_min_score': 147.4916833225875,
        'ref_max_score': 967.3230534670868, # 250 steps
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/carla/carla_lane_follow-v0.hdf5',
        'carla_args': dict(
            vision_size=48,
            vision_fov=48,
            weather=False,
            frame_skip=1,
            steps=250,
            multiagent=True,
            lane=0,
            lights=False,
            record_dir="None",
        )
    }
)

register(
    id='carla-lane-render-v0',
    entry_point='d4rl.carla:CarlaObsDictEnv',
    max_episode_steps=250,
    kwargs={
        'ref_min_score': 367.10279107891745,
        'ref_max_score': 967.3230534670868, # 250 steps
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/carla/carla_lane_follow-v0.hdf5',
        'render_images': True,
        'carla_args': dict(
            vision_size=48,
            vision_fov=48,
            weather=False,
            frame_skip=1,
            steps=250,
            multiagent=True,
            lane=0,
            lights=False,
            record_dir="None",
        )
    }
)
