"""
BUGS FOUND:

1) Crashed when my tmp folder name was 'Divide by 100...'

"""

import requests
import json
import shutil
import sys
from tqdm import tqdm
from pathlib import Path
from urllib.parse import quote as urlify
from bs4 import BeautifulSoup

# Globals
ROOT = Path(__file__).resolve().parents[1]
INVALID = {'\\', '/', ':', '*', '?', '<', '>', '|'}

def add_problem_to_readme(f, repo, info):
    """Create a README row for the problem.

    Arguments:
        f {IO} -- The file object for the README file
        repo {string} -- The url for the repository being used
        info {dictionary} -- The information json for the problem
    """
    title_url = (lambda a: f'{repo}/{a}')(urlify(info['folder']))
    lang_urls = ','.join(list(map(lambda l: f'[{l}]({title_url}/{urlify(l)})', sorted(info['languages']))))
    title_url = (lambda a: f'[{a}]({title_url})')(info['title'])
    kattis_url = (lambda a: f'[![:cat:](https://open.kattis.com/favicon)]({a})')(info['url'])
    f.write(f'| {title_url} | {lang_urls} | {kattis_url} |\n')

def add_json_to_readme(f, repo):
    """Read problem's info json and convert it into README row.

    Arguments:
        f {IO} -- The file object for the README file
        repo {string} -- The url for the repository being used
    """
    for prob_folder in tqdm(sorted(ROOT.joinpath('src').glob('*'))):
        with open(ROOT.joinpath('src', prob_folder, 'info.json')) as json_f:
            info = json.loads(json_f.read())
            add_problem_to_readme(f, repo, info)

def create_readme(repo):
    pre = """# Kattis Solutions
Solutions to the [Kattis archives](https://open.kattis.com/).

## Problems
| Problem | Languages | :link: |
| - | - | - |
"""
    with open(ROOT.joinpath('README.md'), 'w', encoding='utf-8') as f:
        f.write(pre)
        add_json_to_readme(f, repo)

def create_json(prob_dir, title, url, languages):
    """Create an information json for the problem.

    Arguments:
        prob_dir {Path} -- The problem's path in src
        title {string} -- The problem's Kattis title
        url {string} -- The problem's Kattis url
        languages {list} -- The list of languages with solutions to the problem
    """
    with open(prob_dir.joinpath('info.json'), 'w') as f:
            json.dump({
                'title': title,
                'folder': prob_dir.name,
                'url': url,
                'languages': languages
            }, f, indent=2)

def create_folder(folder, title, url, fname):
    """Create a new folder in the src folder for a given problem.

    Arguments:
        folder {Path} -- The problem's directory (in tmp, or other)
        title {string} -- The problem's Kattis title
        url {string} -- The problem's Kattis url
        fname {string} -- The intended folder name for the problem in src
    """
    prob_dir = ROOT.joinpath('src', fname)
    prob_dir.mkdir()
    languages = []
    for sfolder in folder.glob('*'):
        languages.append(sfolder.name)
        shutil.move(str(sfolder), str(prob_dir.joinpath(sfolder.name)))
    create_json(prob_dir, title, url, languages)

def join_folders(folder, fname):
    """Combine with existing folder for same problem
    """
    # TODO
    # Will do when this scenario arises for myself...
    pass

def check_for_existing_and_duplicates(fname, url):
    """Check if the folder name already exists and in that case,
    check if it's the same problem by comparing urls (which are
    unique). If folder name exists but for a different problem,
    we append '(<version>)' to the fname, incremented as needed.

    Arguments:
        fname {string} -- The intended folder name for the problem
        url {string} -- The Kattis url for the problem

    Returns:
        Tuple -- The versioned name of the folder and True iff exists
    """
    version, exist = (1, False)
    while True:
        new_name = fname + ('' if version == 1 else f'({version})')
        if ROOT.joinpath('src', new_name).is_dir():
            with open(ROOT.joinpath('src', new_name, 'info.json')) as f:
                info = json.loads(f.read())
                if info['url'] == url:
                    exist = True
                    break
                else:
                    version += 1
        else:
            break
    return new_name if version > 1 else fname, exist

def folderify(name):
    """Return a copy of the input string without any invalid
    characters and not ending on a period.

    Arguments:
        name {string} -- The name of the problem on Kattis

    Returns:
        string -- A more suitable name for a folder
    """
    return ''.join(i for i in name if not i in INVALID).rstrip('.')

def get_kattis_title(url):
    """Scrape the problem's title from Kattis.

    Arguments:
        url {string} -- The Kattis url of the problem

    Returns:
        string -- The title of the problem
    """
    r=requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.select_one('h1').text

def process_problem_folder(folder, url):
    """Process a single solution folder, extracting needed info
    and moving into the src folder.

    Arguments:
        folder {Path} -- The full path to the new solution
        url {string} -- The Kattis url of the problem
    """
    title = get_kattis_title(url)
    fname = folderify(title)
    fname, exist, = check_for_existing_and_duplicates(fname, url)
    if exist:
        join_folders(folder, fname)
    else:
        create_folder(folder, title, url, fname)

def move_probs_to_src(folder, url_file):
    """Move content of the new solutions into the src folder.

    Arguments:
        folder {string} -- The name of the working folder for new solutions
        url_file {string} -- the name of the url file needed in each solution

    Raises:
        Exception: When url file is missing in any problem
    """
    for prob_folder in tqdm(ROOT.joinpath(folder).glob('*')):
        if not prob_folder.joinpath(url_file).is_file():
            raise Exception(f'Url file missing in {prob_folder}')
        with open(prob_folder.joinpath(url_file), 'r', encoding='utf-8') as f:
            url = f.read()
        prob_folder.joinpath(url_file).unlink()
        process_problem_folder(prob_folder, url)
        prob_folder.rmdir()

def main(args):
    """Main method, a starting point. Optional arguments
    are the name of the working folder of new solutions,
    the name of the file containing problem urls and the
    repository being used.

    Arguments:
        args {list} -- List of command line arguments
    """
    d_args = ['tmp', 'url.txt', 'https://github.com/JonSteinn/Kattis-Solutions']
    for i, a in enumerate(args):
        d_args[i] = a
    print('Moving folders')
    move_probs_to_src(d_args[0], d_args[1])
    print('Recreating README.md')
    create_readme(d_args[2].rstrip('/') + '/tree/master/src')

if __name__ == "__main__":
    main(sys.argv[1:])