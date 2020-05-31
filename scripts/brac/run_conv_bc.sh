# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/bin/bash
#ENV=walker2d-medium-v0
ENV=carla-town-v0

#num samples=number of samples
#total_train_steps=
python train_offline.py \
    --alsologtostderr \
    --save_freq=1000 \
    --sub_dir=0 \
    --env_name=$ENV \
    --identifier="train_conv_bc" \
    --agent_name=conv_bc \
    --total_train_steps=100000 \
    --n_train=10000 \ 
    --model_arch=0 \
    --opt_params=0

