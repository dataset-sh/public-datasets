from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

CountryCodeInfo = TypeBuilder.create(
    'CountryCodeInfo',
    code=str,
    name=str,
    native=str,
)

data_types = {
    DEFAULT_COLLECTION_NAME: CountryCodeInfo
}