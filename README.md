# VAT Docs

This repository is a central place for the VAT user documentation available at https://<TODO>.

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
```

Convert single notebook to markdown.

```sh
jupyter nbconvert examples/Canis_lupus_meets_Felis_silvestris.ipynb --to=markdown --output=../src/examples/Canis_lupus_meets_Felis_silvestris
```

## Publish

You can create a pull request.
It is tested within our CI.
Once it is merged, changes are automatically deployed.
