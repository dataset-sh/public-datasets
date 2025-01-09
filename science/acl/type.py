from easytype import TypeBuilder
from dataset_sh.constants import DEFAULT_COLLECTION_NAME

from easytype import TypeBuilder

AuthorInfo = TypeBuilder.create(
    'AuthorInfo',
    first_name=str,
    last_name=str,
)

PublicationInfo = TypeBuilder.create(
    'PublicationInfo',
    title=str,
    abstract=str,
    year=str,
    venues=list[str],
    web_url=str,
    bibkey=str,
    authors=list[AuthorInfo],
    language=str,
)



data_types = {
    DEFAULT_COLLECTION_NAME: PublicationInfo
}