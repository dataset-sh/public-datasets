import sys
from dataset_sh.constants import DEFAULT_COLLECTION_NAME
from fn import generate_product_connotation
import dataset_sh as dsh
import typing

class ProductTaxonomyNode(typing.TypedDict):
    name: str
    children: list["ProductTaxonomyNode"]

def get_tree_all_paths(root_node: ProductTaxonomyNode) -> list[list[str]]:
    """
    Traverse the tree structure starting from the root node and collect the full path
    (as names) from the root to every node, including intermediate and leaf nodes.

    Args:
        root_node (ProductTaxonomyNode): The root node of the taxonomy tree.

    Returns:
        List[List[str]]: A list of paths (each path is a list of node names) to all nodes in the tree.
    """
    all_paths = []

    def traverse(node: ProductTaxonomyNode, current_path: list[str]):
        current_path.append(node["name"])
        all_paths.append(current_path[:])  # Add the current path to all_paths

        for child in node["children"]:  # Continue traversing for children
            traverse(child, current_path)

        current_path.pop()  # Backtrack to explore other paths

    traverse(root_node, [])
    return all_paths


def create_main_collection():
    cats = []
    with dsh.dataset('commerce/product-category').latest().open() as reader:
        for item in reader.coll('main'):
            cats.append(item)
    pathes = []
    for cat in cats:
        leaves = get_tree_all_paths(cat)
        for leave in leaves:
            pathes.append('/'.join(leave))

    batch = generate_product_connotation.batch('generate_product_connotation')

    if batch.can_start_batch():
        for path in pathes:
            batch.add(path)

        batch.start_batch()
        print('Batch started, please wait until it was processed.')
        sys.exit(1)
    else:
        print('batch already started.')
        status = batch.sync_remote()
        print(status)
        if status['status'] == 'finished':
            items = []
            for input_args, output in batch.iter_outputs():
                items.append({
                    'category': input_args['args'][0],
                    "connotations": output.value
                })
            return items
        else:
            print('batch is not finished, exit dataset building process now.')
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
