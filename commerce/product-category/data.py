from dataset_sh.constants import DEFAULT_COLLECTION_NAME
import requests

data_url = 'https://www.google.com/basepages/producttype/taxonomy.en-US.txt'


def parse_hierarchy_to_dict(data: str):
    lines = [line.strip() for line in data.strip().splitlines() if not line.strip().startswith('#')]
    root = {'name': 'root', 'children': []}  # Root node to start the hierarchy
    node_stack = [root]  # Stack to keep track of current hierarchy level

    for line in lines:
        # Split the line into hierarchy levels
        parts = line.split(" > ")
        depth = len(parts)  # Depth of the current node

        # Create a dictionary for the current node
        current_node = {'name': parts[-1], 'children': []}

        # Find the parent node based on depth
        while len(node_stack) > depth:
            node_stack.pop()  # Move up to the correct parent level

        # Add the current node to its parent's children
        parent_node = node_stack[-1]
        parent_node['children'].append(current_node)

        # Push the current node onto the stack
        node_stack.append(current_node)

    return root['children']  # Return children of the root node


def download_collections():
    resp = requests.get(data_url)
    resp.raise_for_status()
    content = resp.content.decode('utf-8')
    tree = parse_hierarchy_to_dict(content)
    return tree


def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: list(download_collections())
    }