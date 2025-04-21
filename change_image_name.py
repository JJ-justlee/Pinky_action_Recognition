import os
import re

pinky_imageLabel_path = r'pinky_imageLabel' #put your path here

for firstfile in os.listdir(pinky_imageLabel_path):
    firstfile_path = os.path.join(pinky_imageLabel_path, firstfile)
    for secondfile in os.listdir(firstfile_path):
        secondfile_path = os.path.join(firstfile_path, secondfile)
        for image_and_xml in os.listdir(secondfile_path):
            if image_and_xml.startswith('pinky_stand_up_'):
                match = re.match(r"(pinky_stand_up_\d+)_png\.rf\..+\.jpg", image_and_xml)
                if match:
                    new_name = match.group(1) + ".jpg"
                    old_path = os.path.join(secondfile_path, image_and_xml)
                    new_path = os.path.join(secondfile_path, new_name)
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} → {new_name}")
            if image_and_xml.startswith('pinky_stand_up_'):
                match = re.match(r"(pinky_stand_up_\d+)_png\.rf\..+\.xml", image_and_xml)
                if match:
                    new_name = match.group(1) + ".xml"
                    old_path = os.path.join(secondfile_path, image_and_xml)
                    new_path = os.path.join(secondfile_path, new_name)
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} → {new_name}")