from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

LABELS = [
    "T-shirt/top",  # 0
    "Trouser",      # 1
    "Pullover",     # 2
    "Dress",        # 3
    "Coat",         # 4
    "Sandal",       # 5
    "Shirt",        # 6
    "Sneaker",      # 7
    "Bag",          # 8
    "Ankle boot",   # 9
]


MNIST_ENTRY = TypeBuilder.create(
    'MNIST_ENTRY',
    filename=str,
    label=LABELS,
    split=['train', 'test'],
)

data_types = {
    DEFAULT_COLLECTION_NAME: MNIST_ENTRY
}