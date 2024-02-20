from remover import data_remover
import sys


original_dir = sys.argv[1]

print("start remove broken images")

data_remover.resize_images_dir(original_dir)

print("removing broken images has resized")