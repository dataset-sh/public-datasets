import click
from importlib.metadata import version

from datafact.subcmd.publish import publish_cli
from datafact.subcmd.preview import preview_cli
from datafact.subcmd.build import get_build_command

from type import data_types
from data import create_data_dict

try:
    from bin_files import has_binary_files
except ModuleNotFoundError as e:
    has_binary_files = False
except ImportError as e:
    print(f"value 'has_binary_files' not found in 'bin_files': {e}")
    has_binary_files = False

if has_binary_files:
    from bin_files import iter_binary_files
else:
    iter_binary_files = None

__doc__ = f"""
    Build and publish datasets to dataset.sh
    Read more at https://doc.dataset.sh

    You are currently using dataset.sh version: {version('dataset_sh')}
"""


@click.group(help=__doc__)
def cli():
    pass


build_cli = get_build_command(create_data_dict, data_types, media_files_fn=iter_binary_files)

cli.add_command(build_cli, 'build')
cli.add_command(preview_cli, 'preview')
cli.add_command(publish_cli, 'publish')

if __name__ == '__main__':
    cli()