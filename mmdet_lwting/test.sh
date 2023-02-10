#!/bin/bash
# 加载模块
module load anaconda/2021.05
module load cuda/11.1
module load gcc/7.3

# 激活环境
source activate mmdetection

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1

# 训练模型
mim test mmdet balloon_config.py --checkpoint  work_dirs/balloon_config/latest.pth  --show-dir work_dirs/balloon_test_img/
