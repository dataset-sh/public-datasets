from dataset_sh.constants import DEFAULT_COLLECTION_NAME
from acl_anthology import Anthology
from collections import Counter
import json
from tqdm import tqdm

def create_main_collection():
    anthology = Anthology.from_repo()
    for paper in tqdm(anthology.papers()):
        abstract = paper.abstract.as_text() if paper.abstract else ''
        item = dict(
            title=paper.title.as_text(),
            abstract=abstract,
            year=paper.year,
            venues=paper.venue_ids,
            web_url=paper.web_url,
            bibkey=paper.bibkey,
            language=paper.language_name,
            authors=[
                dict(
                    first_name=a.first,
                    last_name=a.last,
                ) for a in paper.authors
            ]
        )
        yield item

def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: list(create_main_collection())
    }