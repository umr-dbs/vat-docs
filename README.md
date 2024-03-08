# VAT Docs

This repository is a central place for the VAT user documentation available at https://umr-dbs.github.io/vat-docs.

<!-- TODO: change URL to proper subdomain -->

## Develop locally

```sh
cargo install mdbook

mdbook serve
```

## Converting Jupyter Notebooks

Create a virtual Python environment and install the required packages.

```sh
# create new venv
python3 -m venv env
# activate new venv
source env/bin/activate
# install required packages
pip install -r requirements.txt
```

Convert single notebook to markdown.

```sh
./convert_notebook.sh <path-to-notebook>
```

## Publish

You can create a pull request.
It is tested within our CI.
Once it is merged, changes are automatically deployed.
