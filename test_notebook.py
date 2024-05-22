#!/usr/bin/env python

'''Convert Jupyter Notebooks to Markdown files.'''

import argparse
import sys
import warnings
from nbconvert import PythonExporter
import nbformat

def eprint(*args, **kwargs):
    '''Print to stderr.'''
    print(*args, file=sys.stderr, **kwargs)

def parse_args() -> str:
    '''Parse command-line arguments.'''

    parser = argparse.ArgumentParser(
        prog='Jupyter to Markdown',
        description='Converts a Jupyter Notebook to a Markdown file.',
    )
    parser.add_argument(
        'filename',
        help='The Jupyter Notebook file to convert.'
    )
    parameters = parser.parse_args()
    return parameters.filename


def convert_to_python(input_file: str) -> str:
    '''Convert the Jupyter Notebook to a Markdown file.'''

    exporter = PythonExporter()

    notebook = nbformat.read(input_file, as_version=4)

    (body, _resources) = exporter.from_notebook_node(notebook)

    return body

def run_script(script: str) -> bool:
    '''Run the script.'''

    try:
        with warnings.catch_warnings(record=True):
            # pylint: disable-next=exec-used
            exec(script, {})

        eprint("SUCCESS")
        return True

    except Exception as error: # pylint: disable=broad-exception-caught
        eprint("ERROR:", error)
        return False

if __name__ != '__main__':
    sys.exit(0)

INPUT_FILE = parse_args()

python_script = convert_to_python(INPUT_FILE)

eprint(f"Running script `{INPUT_FILE}`", end=': ')
if run_script(python_script):
    sys.exit(0)
else:
    sys.exit(1)
