from dataset_sh.constants import DEFAULT_COLLECTION_NAME

from download import iterate_processed_fashion_mnist

LABEL_TABLE = {
    0: "T-shirt/top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle boot",
}


def create_main_collection():
    for split, label, image_path, _ in iterate_processed_fashion_mnist():
        label_name = LABEL_TABLE[label]
        yield dict(
            filename=image_path,
            label=label_name,
            split=split,
        )


def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: list(create_main_collection())
    }