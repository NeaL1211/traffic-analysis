import json
import os
from shutil import copyfile

# 加載 COCO 標籤文件
with open('C:/computer vision/datasets/coco/annotations/instances_val2017.json', 'r') as f:
    annotations = json.load(f)

# 篩選出車輛相關的圖片 ID
car_ids = [a['image_id'] for a in annotations['annotations'] if a['category_id'] in [2, 5, 7]]  # 車、卡車、巴士

# 確保目標目錄存在
output_dir = 'custom_dataset/images/val/'
os.makedirs(output_dir, exist_ok=True)

# 複製相關圖片到新目錄
for image in annotations['images']:
    if image['id'] in car_ids:
        src_path = f"C:/computer vision/datasets/coco/images/val2017/{image['file_name']}"
        dest_path = f"{output_dir}/{image['file_name']}"
        copyfile(src_path, dest_path)

print("車輛圖片已成功篩選並複製！")
