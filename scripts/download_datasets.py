from d4rl import infos
from d4rl.offline_env import DATASET_PATH
import urllib.request
import os


for k in infos.DATASET_URLS:
    dataset_url = infos.DATASET_URLS[k]
    _, dataset_name = os.path.split(dataset_url)
    dataset_filepath = os.path.join(DATASET_PATH, dataset_name)

    if not os.path.exists(dataset_filepath):
        print('Downloading dataset:', dataset_url, 'to', dataset_filepath)
        urllib.request.urlretrieve(dataset_url, dataset_filepath)

