import sys
from dataset_sh.constants import DEFAULT_COLLECTION_NAME
from fn import tag_dataset_paper
import dataset_sh as dsh
import typing

import dataset_sh as dsh
import typing
from cmfn import chunk_it

class AuthorInfo(typing.TypedDict):
    first_name: str
    last_name: str

class PublicationInfo(typing.TypedDict):
    title: str
    abstract: str
    year: str
    venues: list[str]
    web_url: str
    bibkey: str
    authors: list["AuthorInfo"]
    has_paper: bool


def create_main_collection():
    papers = []
    with dsh.dataset('science/acl-datasets').latest().open() as reader:
        for item in reader.coll('main'):
            if item['has_dataset']:
                papers.append(item)
    print('amount of acl papers with dataset: ', len(papers))
    # sys.exit(1)

    chunks = [list(x) for x in chunk_it(papers, 40000)]

    results = []
    all_finished = True

    for idx, chunk in enumerate(chunks):
        bn = f'tag_dataset_paper_chunk_{idx}'
        batch = tag_dataset_paper.batch(bn)

        if batch.can_start_batch():
            for paper in chunk:
                batch.add(
                    title=paper['title'],
                    abstract=paper['abstract'],
                    __meta__={
                        'paper': paper
                    },
                )
            batch.start_batch()
            print(f'Batch {idx} started, please wait until it was processed.')
            all_finished = False
        else:
            print('batch already started.')
            status = batch.sync_remote()
            print({
                'batch': bn,
                'status': status
            })
            if status['status'] == 'finished':
                for input_args, output in batch.iter_outputs():
                    paper = input_args['meta']['paper']
                    paper_with_tags = {
                        k:v for k,v in paper.items()
                    }
                    paper_with_tags['tags'] = output.value
                    results.append(paper_with_tags)
            else:
                print(f'batch {idx} is not finished, exit dataset building process now.')
                all_finished = False

    if all_finished:
        # print(results[0])
        # sys.exit(1)
        return results
    else:
        print('some batches are not finished, exit dataset building process now.')
        sys.exit(1)




def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: create_main_collection()
    }
