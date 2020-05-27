from distutils.core import setup
from setuptools import find_packages

setup(
    name='d4rl',
    version='1.0',
    install_requires=['gym', 
                      'numpy', 
                      'mujoco_py', 
                      'h5py', 
                      #'adept_envs @ git+git://github.com/justinjfu/relay-policy-learning@setup#egg=adept_envs\&subdirectory=adept_envs',
                      'mjrl @ git+git://github.com/aravindr93/mjrl@master#egg=mjrl'],
    packages=find_packages(),
)
