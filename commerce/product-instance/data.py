import sys
from dataset_sh.constants import DEFAULT_COLLECTION_NAME
from fn import generate_product_instances
import dataset_sh as dsh
import typing

class ProductTaxonomyNode(typing.TypedDict):
    name: str
    children: list["ProductTaxonomyNode"]

def get_tree_leaves(root_node: ProductTaxonomyNode):
    """
    Traverse the tree structure starting from the root node and collect the full path
    from the root to each leaf node.

    Args:
        root_node (ProductTaxonomyNode): The root node of the taxonomy tree.

    Returns:
        List[List[str]]: A list of paths (each path is a list of node names) to all leaf nodes in the tree.
    """
    paths = []

    def traverse(node: ProductTaxonomyNode, current_path: list[str]):
        current_path.append(node["name"])

        if not node["children"]:  # If there are no children, this is a leaf node
            paths.append(current_path[:])  # Add a copy of the current path
        else:
            for child in node["children"]:
                traverse(child, current_path)

        current_path.pop()  # Backtrack to explore other paths

    traverse(root_node, [])
    return paths

def create_main_collection():
    cats = []
    with dsh.dataset('commerce/product-category').latest().open() as reader:
        for item in reader.coll('main'):
            cats.append(item)
    pathes = []
    for cat in cats:
        leaves = get_tree_leaves(cat)
        for leave in leaves:
            pathes.append('/'.join(leave))

    batch = generate_product_instances.batch('generate-product-instance-full-path-1')

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
                    "instances": output.value
                })
            return items
        else:
            print('batch is not finished, exit dataset building process now.')
            sys.exit(1)



def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: create_main_collection()
    }

