from pathlib import Path
from typing import Iterator

from genopen import gen_open
from gencat import gen_cat


def lines_from_dir(filepattern: str, dirname: str) -> Iterator[str]:
    names = Path(dirname).rglob(filepattern)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines
