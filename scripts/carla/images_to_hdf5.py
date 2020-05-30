import h5py
import numpy as np
import os
from PIL.PngImagePlugin import PngImageFile
from PIL import Image
from d4rl.utils import dataset_utils
import argparse
import tqdm
def write_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir', type=str, help='Data directory.')
    parser.add_argument('--output_file', type=str, default='output', help='Output hdf5 file. Default=output.hdf5')
    args = parser.parse_args()
    print('Getting image list')
    file_list = sorted(os.listdir(args.data_dir))
    total_size = len(file_list)
    print('total size:', total_size)
    
    for sub_idx in range(total_size // 100000):
        writer = dataset_utils.DatasetWriter(extra_keys={'location', 'target', 'velocity', 'reward_collision'})
        sub_file_list = file_list[sub_idx*100000:(sub_idx+1)*100000]
        for idx, file_name in tqdm.tqdm(enumerate(sub_file_list)):
            print(idx, file_name)
            im = PngImageFile(os.path.join(args.data_dir, file_name))

            brake = float(im.text['control_brake'])
            throttle = float(im.text['control_throttle'])
            if brake > 0.0:
                brake_throttle = -brake
            else:
                brake_throttle = throttle
            action = np.array([ brake_throttle, float(im.text['control_steer'])])
            reward = np.array(float(im.text['reward']))
            obs = Image.open(os.path.join(args.data_dir, file_name))
            obs = np.array(obs).astype(np.float32) / 255.0

            location = np.array([float(im.text['location_x']), float(im.text['location_y']), float(im.text['location_z'])])
            #print('loc:', location)
            velocity = np.array([float(im.text['velocity_x']), float(im.text['velocity_y']), float(im.text['velocity_z'])])
            target_location = np.array([float(im.text['target_location_x']), float(im.text['target_location_y']), float(im.text['target_location_z'])])

            writer.append_data(obs, action, reward, False, 
                              location=location,
                              velocity=velocity,
                              target=target_location, 
                              reward_collision=float(im.text['reward_collision']))
        writer.write_dataset(args.output_file+'_%d.hdf5' % sub_idx)
if __name__ == '__main__':
    write_data()
