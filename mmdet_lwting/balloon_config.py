
_base_ = '/HOME/scz0aqk/run/mmdetection_work/mask_rcnn_r50_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

dataset_type = 'CocoDataset'
classes = ('balloon',)
data = dict(
    train=dict(
        ann_file='/HOME/scz0aqk/run/mmdetection_work/data/balloon/annotations/train_coco.json',
        img_prefix='/HOME/scz0aqk/run/mmdetection_work/data/balloon/train/',
        classes=classes),
    val=dict(
        ann_file='/HOME/scz0aqk/run/mmdetection_work/data/balloon/annotations/val_coco.json',
        img_prefix='/HOME/scz0aqk/run/mmdetection_work/data/balloon/val/',
        classes=classes),
    test=dict(
        ann_file='/HOME/scz0aqk/run/mmdetection_work/data/balloon/annotations/val_coco.json',
        img_prefix='/HOME/scz0aqk/run/mmdetection_work/data/balloon/val/',
        classes=classes))

load_from = '/HOME/scz0aqk/run/mmdetection_work/mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth'