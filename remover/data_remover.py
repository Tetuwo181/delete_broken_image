import os
from typing import Callable
from .remove_image import remove_broken_img
import shutil


def is_image(file_path:str) -> bool:
    """
    拡張子から画像ファイルかどうか判定
    :param file_path:
    :return:
    """
    root, ext = os.path.splitext(file_path)
    return (ext == ".jpg") or (ext == ".jpeg") or (ext == ".JPG") or (ext == ".JPEG") or (ext == ".jfif")


def resize_images_dir(resize_dir: str) -> None:
    """
    指定したディレクトリ以下の画像で壊れた画像を削除する
    :param resize_dir: リサイズしたい画像が存在するディレクトリ
    :param size: リサイズ後の長いほうのサイズ
    :return:
    """
    file_name_set = os.listdir(resize_dir)
    for name in file_name_set:
        file_path = os.path.join(resize_dir, name)
        if os.path.isdir(file_path):
            print(file_path, "is dir")
            resize_images_dir(file_path)
        if is_image(file_path):
            remove_broken_img(file_path)

