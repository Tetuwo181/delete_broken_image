from PIL import Image
from PIL import UnidentifiedImageError
import os


def is_jfif(file_path: str) -> bool:
    root, ext = os.path.splitext(file_path)
    return (ext == "jfif")


def remove_broken_img(original_path: str) -> None:
    """
    ファイルが壊れているかどうかを確認し、削除する
    :param original_path: ファイルの存在するオリジナルのパス
    :param write_path: 書き出し先　Noneであればオリジナルへ上書き
    :return:
    """
    try:
        original_image = Image.open(original_path)
    except:
        os.remove(original_path)
        print(f"{original_path} has deleted")

