#!/usr/bin/env python

'''
Preprocess all the notebooks in the book's example directory to convert them to markdown
'''

import sys
import json
import subprocess
from typing import List

def eprint(*args, **kwargs):
    '''Print to stderr.'''
    print(*args, file=sys.stderr, **kwargs)

def replace_ipynb_files(book_sections: List[dict]):
    '''Replace all the notebooks in the book with their markdown versions'''

    sections = [section['Chapter'] for section in book_sections if 'Chapter' in section]

    while len(sections) > 0:
        section = sections.pop()

        # add new sub-sections
        sections.extend([
            subsection['Chapter']
            for subsection in section['sub_items']
            if 'Chapter' in subsection
        ])

        if section['source_path'] is None or not section['source_path'].endswith('.ipynb'):
            continue

        eprint("Converting to markdown:", section['source_path'])

        notebook_to_md = subprocess.run(
            [
                "python3", "notebook_to_md.py", section['source_path'],
                "--output-dir=examples/",
            ],
            check=True,
            capture_output=True
        )
        # eprint("notebook_to_md:", notebook_to_md.stderr)
        section['content'] = notebook_to_md.stdout.decode('utf-8')
        section['source_path'] = section['source_path'].replace('.ipynb', '.md')
        section['path'] = section['path'].replace('.ipynb', '.md')

    return book

if __name__ != '__main__':
    sys.exit(0)

if len(sys.argv) > 1 and sys.argv[1] == "supports":
    # we need to ignore the supports call and just say we support everything
    sys.exit(0)

context, book = json.load(sys.stdin)

# eprint("Context:", context)
# eprint("Book:", json.dumps(book))

replace_ipynb_files(book['sections'])

print(json.dumps(book))
