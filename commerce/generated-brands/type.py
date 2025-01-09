from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

HelloWorldTranslation = TypeBuilder.create(
    'HelloWorldTranslation',
    language=str,
    value=str
)

data_types = {
    DEFAULT_COLLECTION_NAME: HelloWorldTranslation
}