# VAT Docs

This repository is a central place for the VAT user documentation available at https://umr-dbs.github.io/vat-docs.

<!-- TODO: change URL to proper subdomain -->

## Develop locally

You can easily develop the documentation locally.
For this, you need to install some Rust and Python dependencies.
Then, you can use simple commands to start a development server.

### Dependencies

- Rust (current stable version)
  - Install Rustup: https://rustup.rs/
  - Install mdBook: `cargo install mdbook`
- Python (current supported version)

  - Most OS come with Python pre-installed: https://www.python.org/
  - Install a virtual environment and some dependencies:

    ```sh
    # create new venv
    python3 -m venv env
    # activate new venv
    source env/bin/activate

    # Dependencies for building the documentation
    pip install -r requirements.txt

    # Dependencies for testing Jupyter notebooks
    pip install -r example-requirements.txt
    ```

### Documentation

Start development server:

```sh
mdbook serve
```

### Converting Jupyter Notebooks

You can convert single notebook to markdown:

```sh
chmod +x notebook_to_md.sh

./notebook_to_md.sh <path-to-notebook> > <path-to-output-md>
```

### Testing Jupyter Notebooks

To test the Jupyter notebooks, you can use the following command:

```sh
chmod +x test_notebook.sh

./test_notebook.sh <path-to-notebook>
```

## Publish

You can create a pull request.
It is tested within our CI.
Once it is merged, changes are automatically deployed.
