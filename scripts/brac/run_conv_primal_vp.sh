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
VALUE_PENALTY=True
DIVERGENCE=kl
#ENV=carla-lane-v0
ENV=carla-town-v0
DATA=example
#B_CKPT=/hdd/home/justinfu/tmp/offlinerl/learn/carla-lane-v0/train_conv_bc/conv_bc/0/0/agent_behavior
B_CKPT=/hdd/home/justinfu/tmp/offlinerl/learn/carla-town-v0/train_conv_bc/conv_bc/0/0/agent_behavior

python train_offline.py \
  --alsologtostderr --sub_dir=auto \
  --env_name=$ENV \
  --agent_name=conv_brac_primal \
  --total_train_steps=100000 \
  --n_train=10000 \
  --model_arch=1 \
  --opt_params=1 \
  --value_penalty=1 \
  --alpha=0.3 \
  --b_ckpt=$B_CKPT \
  #--gin_bindings="brac_primal_agent.Agent.behavior_ckpt_file='$B_CKPT'" \
  #--gin_bindings="brac_primal_agent.Agent.alpha=$ALPHA" \
  #--gin_bindings="brac_primal_agent.Agent.value_penalty=$VALUE_PENALTY" \
  #--gin_bindings="brac_primal_agent.Agent.divergence_name='$DIVERGENCE'" \
  #--gin_bindings="train_eval_offline.model_params=(((300, 300), (200, 200),), 2)" \
  #--gin_bindings="train_eval_offline.batch_size=256" \
  #--gin_bindings="train_eval_offline.optimizers=(('adam', 1e-3), ('adam', $PLR), ('adam', 1e-3))" \
