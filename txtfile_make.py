import os
import xml.etree.ElementTree as ET

class_names = [
    'fall', 'standing'
]

input_base_dir = 'pinky_imageLabel/labels'
output_base_dir = 'pinky_imageLabel/labelsfortxt'

def convert_voc_to_yolo(split):
    input_dir = os.path.join(input_base_dir, split)
    output_dir = os.path.join(output_base_dir, split)
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if not file.endswith('.xml'):
            continue

        xml_path = os.path.join(input_dir, file)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        image_width = int(root.find('size/width').text)
        image_height = int(root.find('size/height').text)

        yolo_lines = []

        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name not in class_names:
                print(f"❌ Unknown class: {class_name} in {file}")
                continue

            class_id = class_names.index(class_name)

            bbox = obj.find('bndbox')
            xmin = float(bbox.find('xmin').text)
            ymin = float(bbox.find('ymin').text)
            xmax = float(bbox.find('xmax').text)
            ymax = float(bbox.find('ymax').text)

            cx = (xmin + xmax) / 2.0 / image_width
            cy = (ymin + ymax) / 2.0 / image_height
            w = (xmax - xmin) / image_width
            h = (ymax - ymin) / image_height

            yolo_lines.append(f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

        if yolo_lines:
            txt_filename = os.path.splitext(file)[0] + '.txt'
            txt_path = os.path.join(output_dir, txt_filename)
            with open(txt_path, 'w') as f:
                f.write('\n'.join(yolo_lines))

for split in ['train', 'val', 'test']:
    convert_voc_to_yolo(split)

print("XML → YOLO format conversion completed.")