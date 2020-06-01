import matplotlib
matplotlib.use('Agg')
import argparse
import d4rl
import gym
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


def plot_lines():
    env_name = 'carla-town-v0'
    #dataset = d4rl.get_dataset_key(env_name)
    locations = d4rl.get_dataset_key(env_name, 'infos/location')
    shape = locations.shape
    print('Shape:', locations.shape[0])

    #N = 1200000
    #locations = dataset['infos/location'][:N]

    xs = []
    ys = []
    obs_arr = []
    cntr = 0
    for i in range(0, locations.shape[0]-1, 1):
        cntr += 1
        dist_term = np.linalg.norm(locations[i+1,:2] - locations[i,:2]) >= 3.0
        #if terminals[i] or dist_term:
        if dist_term or cntr >= 5000:
            print(i, locations[i])
            offset = np.random.randn(3) * 0.5
            if len(obs_arr) > 0:
                obs_arr = (np.array(obs_arr) + offset )
                x = obs_arr[:,0]
                y = obs_arr[:,1]
                xs.append(x)
                ys.append(y)
            obs_arr = []
            cntr = 0
        else:
            obs_arr.append(locations[i])

    print('# trajs:', len(xs))
    plt.figure()
    plt.figure()
    for (xarr, yarr) in zip(xs, ys):
        plt.plot(xarr, yarr, lw=0.1)
    plt.axis('off')

    #goal = np.array([13.473097, 134.311234, -0.010433])
    #goal_x = [goal[0]]
    #goal_y = [goal[1]]
    #plt.scatter(goal_x, goal_y, marker='o')

    plt.savefig(env_name+'.png', transparent=True, bbox_inches='tight', pad_inches=0, dpi=600)
    print('fig saved!')



if __name__ == "__main__":
    #env_name = 'antmaze-umaze-v0'
    #env_name = 'antmaze-medium-play-v0'
    plot_lines()
    #plot()


