# Create and publish dataset

This folder contains a project created by datafact (DATAset FACTory),

You can use this project to build and publish your dataset to [dataset.sh](https://dataset.sh)

## How to modify this project

You will need to modify the following 3 files to create, build, and, publish your own dataset:

* data.py
  This file contains code that generate/gather your dataset.

* type.py
  This file contains [easytype](https://doc.dataset.sh/typing) type annotations for you dataset.

* DATASET_README.md
  This file contains readme document for your dataset.

## Build Dataset

To build your dataset, simply use:

```shell
python project.py build
```

## Publish Dataset

To build your dataset, simply use:

```shell
python project.py publish
```

### Manage publishing target

You can publish your dataset to multiple dataset.sh server. By default, the project is configured to publish to your
local dataset.sh repo.

Use the following command to `add`, `list`, and, `remove` publishing targets:

```shell
python project.py add --help
python project.py list --help
python project.py remove --help
```