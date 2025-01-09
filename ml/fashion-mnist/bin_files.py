import os
from download import iterate_processed_fashion_mnist

has_binary_files = True

def iter_binary_files():
    for split, label, image_path, full_path in iterate_processed_fashion_mnist():
        with open(full_path, 'rb') as fd:
            yield image_path, fd.read()
