import requests
import re
from tqdm import tqdm 
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

def is_200(url):
    return requests.get(url).status_code == 200

def display_errors(errors):
    for k in sorted(errors.keys()):
        print((lambda e: f'Line {k} has errors: {e}')(','.join(errors[k])))

def check_line(errors, line, line_number):
    counter = 0
    for bracket in re.finditer(r'\(.*?\)', line):
        url = bracket.group(0)[1:-1]
        if url.startswith('https://'):
            counter += 1
            if not is_200(url):
                errors[line_number].append('Invalid link')
                break
    if counter < 3:
        errors[line_number].append('Missing links')

def check_links():
    errors = defaultdict(lambda: [])
    with open(ROOT.joinpath('README.md'), 'r', encoding='utf-8') as f:
        for i, line in tqdm(enumerate(f.readlines()[6:])):
            check_line(errors, line, i + 7)
    display_errors(errors)

# TODO: use threads
if __name__ == "__main__":
    check_links()