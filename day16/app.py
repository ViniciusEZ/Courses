import os
from PIL import Image


def main(images, new_width=800):
    if not os.path.isdir(images):
        raise NotADirectoryError(f'{images} do not exists.')

    for root, dirs, files in os.walk(images):
        for file in files:
            full_path = os.path.join(root, file)
            file_name, ext = os.path.splitext(file)
            converted_tag = '_CONVERTED'
            new_file = f'{file_name}{converted_tag}{ext}'
            new_file_full_path = os.path.join(root, new_file)



            # if converted_tag in full_path:
            #     os.remove(full_path)
            # continue

            if os.path.isfile(new_file_full_path):
                print(f'File {new_file_full_path} already exists.')
                continue

            if converted_tag in full_path:
                print('Image already converted.')
                continue

            img_pillow = Image.open(full_path)
            width, height = img_pillow.size
            new_height = round(new_width * height / width)

            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70
                # exif=img_pillow.info['exif']
            )
            print(f'{full_path} successfully converted.')
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_path_images = '/home/vinicius/Documents/udemyPython/day16/images'
    main(main_path_images, 1000)
