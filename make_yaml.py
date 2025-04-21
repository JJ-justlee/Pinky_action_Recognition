import os
import yaml
import xml.etree.ElementTree as ET

xml_dir = r'pinky_imageLabel/labels'

output_yaml_path = r'' #path the dataset.yaml file will be saved
output_base_dir = r'' #base directory

class_names = set()

for firstfile in os.listdir(xml_dir):
    firstfile_path = os.path.join(xml_dir, firstfile)
    for secondfile in os.listdir(firstfile_path):
        secondfile_path = os.path.join(firstfile_path, secondfile)
        if secondfile.endswith('.xml'):
            file_path = os.path.join(xml_dir, secondfile_path)
            tree = ET.parse(file_path)
            root = tree.getroot()
            for obj in root.findall('object'):
                name = obj.find('name').text
                class_names.add(name)

class_names = sorted(list(class_names))

dataset_yaml = {
    'train': os.path.join(output_base_dir, 'pinky_imageLabel/images/train'),
    'val': os.path.join(output_base_dir, 'pinky_imageLabel/images/val'),
    'test': os.path.join(output_base_dir, 'pinky_imageLabel/images/test'),
    'nc': len(class_names),
    'names': class_names
}

with open(output_yaml_path, 'w') as f:
    yaml.dump(dataset_yaml, f, sort_keys=False)

print("completed class extraction and dataset.yaml generation")
print(f"number of classes: {len(class_names)}")
print(f"class names: {class_names}")
print(f"location saved: {output_yaml_path}")
