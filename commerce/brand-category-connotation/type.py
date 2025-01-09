from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

ProductCategoryConnotation = TypeBuilder.create(
    'ProductCategoryConnotation',
    category=str,
    Connotations=list[str]
)

data_types = {
    DEFAULT_COLLECTION_NAME: ProductCategoryConnotation
}