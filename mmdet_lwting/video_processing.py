import cv2
import mmcv
import numpy as np
import torch

from mmdet.apis import init_detector, inference_detector

score_thr = 0.8
video_reader = mmcv.VideoReader("./test_video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(
    './Colorful_Balloons.mp4', fourcc, video_reader.fps,
    (video_reader.width, video_reader.height))
print(len(video_reader))

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

model = init_detector('balloon_config.py', 'work_dirs/balloon_config/latest.pth', device=device)

for frame in video_reader:
    result = inference_detector(model, frame)
    mask = None
    masks = result[1][0]
    for i in range(len(masks)):
        if result[0][0][i][-1] >= score_thr:
            if not mask is None:
                mask = mask | masks[i]
            else:
                mask = masks[i]


    masked_b = frame[:, :, 0] * mask
    masked_g = frame[:, :, 1] * mask
    masked_r = frame[:, :, 2] * mask
    masked = np.concatenate([masked_b[:,:,None],masked_g[:,:,None],masked_r[:,:,None]],axis=2)


    un_mask = 1 - mask
    frame_b = frame[:, :, 0] * un_mask
    frame_g = frame[:, :, 1] * un_mask
    frame_r = frame[:, :, 2] * un_mask
    frame = np.concatenate([frame_b[:, :, None], frame_g[:, :, None], frame_r[:, :, None]], axis=2).astype(np.uint8)
    frame = mmcv.bgr2gray(frame, keepdim=True)
    frame = np.concatenate([frame, frame, frame], axis=2)

    frame += masked
    video_writer.write(frame)


video_writer.release()
cv2.destroyAllWindows()