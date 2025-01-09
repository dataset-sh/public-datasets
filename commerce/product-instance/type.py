from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

ProductCategoryInstance = TypeBuilder.create(
    'ProductCategoryInstance',
    category=str,
    instances=list[str]
)

data_types = {
    DEFAULT_COLLECTION_NAME: ProductCategoryInstance
}