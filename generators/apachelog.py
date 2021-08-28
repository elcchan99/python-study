import re
from typing import Iterator

from fieldmap import field_map

LOGPATS = r"(\S+) (\S+) (\S+) \[(.*?)\] " r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'
LOGPAT = re.compile(LOGPATS)

COL_NAMES = (
    "host",
    "referrer",
    "user",
    "datetime",
    "method",
    "request",
    "proto",
    "status",
    "bytes",
)


def apache_log(lines: Iterator[str]) -> Iterator[dict]:
    # Parse log
    groups = (LOGPAT.match(line) for line in lines)
    tuples = (g.groups() for g in groups if g)

    # Convert log line to dictionary
    log_dicts = (dict(zip(COL_NAMES, t)) for t in tuples)

    # Map fields type
    log_dicts = field_map(log_dicts, "bytes", lambda s: int(s) if s != "-" else 0)
    log_dicts = field_map(log_dicts, "status", int)
    return log_dicts
