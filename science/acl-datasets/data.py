import sys
from dataset_sh.constants import DEFAULT_COLLECTION_NAME
from fn import paper_has_dataset
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


def create_main_collection():
    papers = []
    with dsh.dataset('science/acl').latest().open() as reader:
        for item in reader.coll('main'):
            papers.append(item)
    print(len(papers))

    chunks = [list(x) for x in chunk_it(papers, 40000)]

    results = []
    all_finished = True

    for idx, chunk in enumerate(chunks):
        bn = f'paper_has_dataset_chunk_40k_4o_{idx}'
        batch = paper_has_dataset.batch(bn)

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
                    paper_with_dataset_doc = {
                        k:v for k,v in paper.items()
                    }
                    has_dataset = output.value.lower() in ['yes', 'true']
                    paper_with_dataset_doc['has_dataset'] = has_dataset
                    results.append(paper_with_dataset_doc)
            else:
                print(f'batch {idx} is not finished, exit dataset building process now.')
                all_finished = False

    if all_finished:
        return results
    else:
        print('some batches are not finished, exit dataset building process now.')
        sys.exit(1)




def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: create_main_collection()
    }

if __name__ == "__main__":
    cats = []
    with dsh.dataset('commerce/product-category').latest().open() as reader:
        for item in reader.coll('main'):
            cats.append(item)
    pathes = []
    for cat in cats:
        leaves = get_tree_all_paths(cat)
        for leave in leaves:
            pathes.append('/'.join(leave))
