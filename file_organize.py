import os
import shutil

path = r'pinky_imageLabel'
image_test_path = r'pinky_imageLabel/images/test'
image_val_path = r'pinky_imageLabel/images/val'
image_train_path = r'pinky_imageLabel/images/train'

labelsFolder_path = r'pinky_imageLabel/labels'
label_test_path = r'pinky_imageLabel/labels/test'
label_val_path = r'pinky_imageLabel/labels/val'
label_train_path = r'pinky_imageLabel/labels/train'

makeLabelFolder = os.path.join(path, 'labels')
os.makedirs(makeLabelFolder, exist_ok=True)

makeimageFolder = os.path.join(path, 'images')
os.makedirs(makeimageFolder, exist_ok=True)

split_image = [image_val_path, image_test_path, image_train_path]
split_label = [label_val_path, label_test_path, label_train_path]

for image_dir, label_dir in zip(split_image, split_label):
    for file in os.listdir(image_dir):
        if file.endswith('.xml'):
            src_path = os.path.join(image_dir, file)
            dst_path = os.path.join(label_dir, file)

            if not os.path.exists(dst_path):
                shutil.move(src_path, dst_path)
                print(f"Moved: {file}")
            else:
                print(f"Skipped (already exists): {file}")
