import struct
import typing


def gen_records(record_format: str, thefile: typing.IO):
    """
    sweeps through a file and generates a sequence of unpacked records"""
    record_size = struct.calcsize(record_format)
    while True:
        raw_record = thefile.read(record_size)
        if not raw_record:
            break
        yield struct.unpack(record_format, raw_record)
