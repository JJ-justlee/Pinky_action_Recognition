import os
import xml.etree.ElementTree as ET

xml_folder = 'labels' #put your xml path here
image_root = 'images' #puyt your image path here

for subset in ['train', 'val', 'test']:
    label_subset_folder = os.path.join(xml_folder, subset)
    image_subset_folder = os.path.join(image_root, subset)

    for filename in os.listdir(label_subset_folder):
        if filename.endswith('.xml'):
            xml_path = os.path.join(label_subset_folder, filename)

            tree = ET.parse(xml_path)
            root = tree.getroot()

            filename_tag = root.find('filename')
            path_tag = root.find('path')

            if filename_tag is not None and path_tag is not None:
                new_path = os.path.join(image_subset_folder, filename_tag.text)
                path_tag.text = new_path

                tree.write(xml_path)
                print(f"Updated <path> in {filename}")
