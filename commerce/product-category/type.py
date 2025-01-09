from easytype import TypeBuilder
from easytype.core import TypeReference
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

ProductTaxonomyNode = TypeBuilder.create(
    'ProductTaxonomyNode',
    name= str,
    children=list[TypeReference('ProductTaxonomyNode')],
)

data_types = {
    DEFAULT_COLLECTION_NAME: ProductTaxonomyNode
}