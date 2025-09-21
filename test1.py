import json
import os

# 加載 COCO 標註文件
with open('C:/computer vision/datasets/coco/annotations/instances_val2017.json', 'r') as f:
    annotations = json.load(f)

# 目標標註目錄
label_output_dir = 'custom_dataset/labels/val/'
os.makedirs(label_output_dir, exist_ok=True)

# 篩選出車輛相關的類別 ID
vehicle_category_ids = [2, 5, 7]  # 車、卡車、巴士

# 建立圖片 ID 與文件名的對應關係
image_id_to_filename = {image['id']: image['file_name'] for image in annotations['images']}

# 處理標註
for ann in annotations['annotations']:
    if ann['category_id'] in vehicle_category_ids:  # 僅處理車輛相關的類別
        image_id = ann['image_id']
        filename = image_id_to_filename[image_id]

        # 計算 YOLO 格式的標註值
        x_center = (ann['bbox'][0] + ann['bbox'][2] / 2) / ann['bbox'][2]
        y_center = (ann['bbox'][1] + ann['bbox'][3] / 2) / ann['bbox'][3]
        width = ann['bbox'][2] / ann['bbox'][2]
        height = ann['bbox'][3] / ann['bbox'][3]
        class_id = vehicle_category_ids.index(ann['category_id'])  # 映射到新的類別 ID

        # 輸出標註到對應的 .txt 文件
        label_file = os.path.join(label_output_dir, f"{filename.split('.')[0]}.txt")
        with open(label_file, 'a') as f:
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

print("標註文件已成功生成！")
