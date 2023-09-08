import os
from typing import Tuple, Iterator, Literal, Optional

from git import Repo, Commit, Tree, Blob, Submodule


def get_repo_name(repo: Repo) -> str:
    """Gets the repo name from the origin's URL, or from the local path if there is None."""
    if isinstance(repo, str):
        repo = Repo(repo)
    if len(repo.remotes) == 0:
        return repo.git.rev_parse("--show-toplevel")
    remote = repo.remotes[0]
    return remote.url.split('.git')[0].split('/')[-1]

def iter_tree(
        tree: Tree,
    type_filter: Optional[Literal['blob', 'tree', 'submodule']] = None
) -> Iterator[Tuple[Tree | Blob | Submodule, str, Literal['blob', 'tree', 'submodule']]]:
    for entry in tree:
        if type_filter is not None and entry.type == type_filter:
            yield entry, entry.name, entry.type


def iter_folders(
        tree: Tree,
        names: list[str]
) -> Iterator[Tuple[Tree, str]]:
    for tree, name, _ in iter_tree(tree, type_filter='tree'):
        if name in names:
            yield tree, name

def iter_files(
        tree: Tree,
) -> Iterator[Tuple[Blob, str]]:
    for blob, name, _ in iter_tree(tree, type_filter='blob'):
        yield blob, name

def rename_tsv_files(repo: Repo):
    tree = repo.head.commit.tree
    for folder, facet_name in iter_folders(tree, ('measures', 'notes', 'harmonies')):
        for file, file_name in iter_files(folder):
            if not file_name.endswith('.tsv'):
                continue
            new_name = f"{facet_name}/{file_name[:-4]}.{facet_name}.tsv"
            repo.index.move([file, new_name])



if __name__ == '__main__':
    repo = Repo(os.getcwd())
    print(get_repo_name(repo))
    rename_tsv_files(repo)