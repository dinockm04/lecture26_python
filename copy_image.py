import os
import shutil

def find_file(filename):
    for root, dirs, files in os.walk('.'):
        if filename in files:
            return os.path.join(root, filename)
    return None

def copy_image_file(image_file):
    ext_list = ['.jpg', '.png', '.gif']
    
    file_path = find_file(image_file)
    
    if file_path is None:
        print('파일을 찾을 수 없습니다.')
        return
    
    name, ext = os.path.splitext(image_file)
    
    if ext.lower() not in ext_list:
        print('jpg, png, gif 파일만 복사할 수 있습니다.')
        return
    
    copy_file = name + '_copy' + ext
    
    shutil.copy(file_path, copy_file)
    print(f'{copy_file} 파일로 복사되었습니다.')


image_file = input('복사할 이미지 파일명 입력 : ')
copy_image_file(image_file)