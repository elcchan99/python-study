import bz2
import gzip
from typing import Callable, Iterator, NamedTuple

class OpenerConfig(NamedTuple):
    matcher: Callable[[str], bool]
    opener: Callable[[str], Iterator[str]]


OPENER_CONFIGS = {
    "gzip": OpenerConfig(matcher=lambda p: p.suffix == ".gz", opener=gzip.open),
    "bzip2": OpenerConfig(matcher=lambda p: p.suffix == ".bz2", opener=bz2.open),
    "default": OpenerConfig(matcher=lambda p: True, opener=open),
}

DEFAULT_OPEN_ARGS = ('rt', )

def _magic_opener(path: str):
    for config in OPENER_CONFIGS.values():
        if config.matcher(path):
            return config.opener
    return OPENER_CONFIGS["default"].opener


def gen_open(paths, *args):
    for path in paths:
        opener = _magic_opener(path)
        yield opener(path, *args)

