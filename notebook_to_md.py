#!/usr/bin/env python

'''Convert Jupyter Notebooks to Markdown files.'''

import os
import sys
import argparse
from dataclasses import dataclass
from typing import List, Tuple
import base64
from nbconvert import MarkdownExporter
import nbformat

def eprint(*args, **kwargs):
    '''Print to stderr.'''
    print(*args, file=sys.stderr, **kwargs)

def parse_args() -> Tuple[str, str]:
    '''Parse command-line arguments.'''

    parser = argparse.ArgumentParser(
        prog='Jupyter to Markdown',
        description='Converts a Jupyter Notebook to a Markdown file.',
    )
    parser.add_argument(
        'filename',
        help='The Jupyter Notebook file to convert.'
    )
    parser.add_argument(
        '-o', '--output-dir',
        required=False,
        help='The output directory for supporting image files.'
    )
    parameters = parser.parse_args()
    return parameters.filename, parameters.output_dir

def create_images_directory(output_directory: str, input_file: str) -> str:
    '''Create the directory for supporting image files.'''

    input_file_name, _ = os.path.splitext(input_file)
    image_directory_name = input_file_name + '_images'

    os.makedirs(os.path.join(output_directory, image_directory_name), exist_ok=True)

    return image_directory_name

@dataclass
class Output:
    """Image output to store separately."""
    name: str
    content: bytes

def png_to_data_uri(output: Output) -> str:
    '''Convert a PNG file to a data URI.'''

    base64_utf8_str = base64.b64encode(output.content).decode('utf-8')

    ext     = output.name.split('.')[-1]
    dataurl = f'data:image/{ext};base64,{base64_utf8_str}'

    return dataurl

def replace_image_links(body: str, outputs: List[Output]) -> str:
    '''Replace image links in the Markdown body with data URIs.'''

    modified_body = ""
    for body_line in body.splitlines():
        if body_line.startswith('!['): # replace image links with data URIs
            for output in outputs:
                if body_line.find(output.name) != -1:
                    modified_body += f'![{output.name}]({png_to_data_uri(output)})\n'
        else:
            modified_body += body_line + '\n'

    return modified_body

def convert_to_markdown(input_file: str, output_directory: str) -> Tuple[str, List[Output]]:
    '''Convert the Jupyter Notebook to a Markdown file.'''

    exporter = MarkdownExporter()

    notebook = nbformat.read(input_file, as_version=4)

    (body, resources) = exporter.from_notebook_node(
        notebook,
        resources={'output_files_dir': os.path.join(output_directory)}
    )

    outputs = [
        Output(name=output_key, content=resources['outputs'][output_key])
        for output_key
        in resources['outputs']
    ]

    return replace_image_links(body, outputs), outputs


if __name__ != '__main__':
    sys.exit(0)

INPUT_FILE, OUTPUT_DIRECTORY = parse_args()

eprint(f'Converting `{INPUT_FILE}` to Markdown...')
eprint(f'Storing supporting image files in `{OUTPUT_DIRECTORY}`...')

image_directory = create_images_directory(OUTPUT_DIRECTORY, INPUT_FILE)

markdown, image_outputs = convert_to_markdown(INPUT_FILE, image_directory)

# Write Markdown to stdout
print(markdown)

# Store supporting image files
# for output in image_outputs:
#     eprint(f'Storing `{output.name}`...')
#     output_path = os.path.join(OUTPUT_DIRECTORY, output.name)
#     with open(output_path, 'wb') as file:
#         file.write(output.content)
