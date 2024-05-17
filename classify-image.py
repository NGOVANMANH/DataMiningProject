import os
import shutil

source_dir = './data'
cat_dest_dir = './data_classified/cat'
dog_dest_dir = './data_classified/dog'

cat_images = []
dog_images = []

for dir in os.listdir('./data'):
    if(dir.split('.')[0] == 'cat'):
        cat_images.append(dir)
    else: 
        dog_images.append(dir)

def copy_images(image_list, dest_dir):
    for image in image_list:
        source_path = os.path.join(source_dir, image)
        dest_path = os.path.join(dest_dir, image)
        shutil.copy(source_path, dest_path)

copy_images(cat_images, cat_dest_dir)

copy_images(dog_images, dog_dest_dir)