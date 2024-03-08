'''
Preprocess all the notebooks in the book's example directory to convert them to markdown
'''

import sys
import json
import subprocess


if __name__ != '__main__':
    sys.exit(0)

if len(sys.argv) > 1: # we check if we received any argument
    if sys.argv[1] == "supports":
        # then we are good to return an exit status code of 0,
        # since the other argument will just be the renderer's name
        sys.exit(0)

print("Input:", sys.argv, file=sys.stderr)

context, book = json.load(sys.stdin)

print("Context:", context, file=sys.stderr)
# print("Book:", json.dumps(book['sections'][8]), file=sys.stderr)

# Find example section:
for chapter in book['sections']:
    if not 'Chapter' in chapter:
        continue

    chapter = chapter['Chapter']
    if chapter['name'] == 'Examples':
        examples_chapter = chapter
        break

if examples_chapter is None:
    sys.exit(0)

# Convert ipynb to md
for section in examples_chapter['sub_items']:
    if not 'Chapter' in section:
        continue
    section = section['Chapter']

    # print("section:", section, file=sys.stderr)
    if section['source_path'].endswith('.ipynb'):
        print("Notebook:", section['source_path'], file=sys.stderr)
        section['content'] = subprocess.run(
            ["jupyter", "nbconvert", section['source_path'], "--to=markdown", "--stdout"],
            check=True,
            capture_output=True
        ).stdout.decode('utf-8')
        section['source_path'] = section['source_path'].replace('.ipynb', '.md')
        section['path'] = section['source_path'].replace('.ipynb', '.md')

# print("Book:", file=sys.stderr)
# print(json.dumps(book), file=sys.stderr)

print(json.dumps(book))
