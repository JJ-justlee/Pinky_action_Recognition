import os

folder_path = 'pinky_abnormal' #put your image path here

file_list = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

# 이름 바꾸기
for idx, filename in enumerate(file_list, 1):
    new_name = f"pinky_stand_up_{idx:03d}.png"  # 001, 002, ...
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)

print("completed renaming files.")