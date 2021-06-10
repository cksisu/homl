"""
Make it easy to setup and manage project artifacts, data, and metadata
"""
import re
import git
from pathlib import Path


def repo_root(fpath):
    """Returns absolute path for parent Git repository"""
    git_repo = git.Repo(fpath, search_parent_directories=True)
    return git_repo.git.rev_parse("--show-toplevel")


class Paths:
    """
    Common project path attributes and methods to manage paths and files
    """
    def __init__(self):
        fpath = Path(__file__).resolve()
        git_repo = git.Repo(fpath, search_parent_directories=True)
        git_root = git_repo.git.rev_parse("--show-toplevel")
        self.root = Path(git_root)

        root_subdirs = [x for x in self.root.iterdir() if x.is_dir()]
        root_subdirs = list(filter(
            lambda x: not bool(re.match(r"\..*", x.name)), root_subdirs))

        for x in root_subdirs:
            setattr(self, x.name, self.root.joinpath(x))

        if hasattr(self, "data"):
            data_subdirs = [x for x in self.data.iterdir() if x.is_dir()]
            for x in data_subdirs:
                setattr(self, x.name, self.root.joinpath(x))

        if hasattr(self, "docs"):
            docs_subdirs = [x for x in self.docs.iterdir() if x.is_dir()]
            for i, x in enumerate(docs_subdirs):
                if x.name == "images":
                    self.images = docs_subdirs[i]
