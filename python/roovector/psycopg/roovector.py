import psycopg
from psycopg.adapt import Loader, Dumper
from psycopg.pq import Format
from .. import RooVector


class RooVectorDumper(Dumper):

    format = Format.TEXT

    def dump(self, obj):
        return RooVector._to_db(obj).encode('utf8')


class RooVectorBinaryDumper(RooVectorDumper):

    format = Format.BINARY

    def dump(self, obj):
        return RooVector._to_db_binary(obj)


class RooVectorLoader(Loader):

    format = Format.TEXT

    def load(self, data):
        if isinstance(data, memoryview):
            data = bytes(data)
        return RooVector._from_db(data.decode('utf8'))


class RooVectorBinaryLoader(RooVectorLoader):

    format = Format.BINARY

    def load(self, data):
        if isinstance(data, memoryview):
            data = bytes(data)
        return RooVector._from_db_binary(data)


def register_roovector_info(context, info):
    if info is None:
        raise psycopg.ProgrammingError('roovector type not found in the database')
    info.register(context)

    # add oid to anonymous class for set_types
    text_dumper = type('', (RooVectorDumper,), {'oid': info.oid})
    binary_dumper = type('', (RooVectorBinaryDumper,), {'oid': info.oid})

    adapters = context.adapters
    adapters.register_dumper('numpy.ndarray', text_dumper)
    adapters.register_dumper('numpy.ndarray', binary_dumper)
    adapters.register_dumper(RooVector, text_dumper)
    adapters.register_dumper(RooVector, binary_dumper)
    adapters.register_loader(info.oid, RooVectorLoader)
    adapters.register_loader(info.oid, RooVectorBinaryLoader)
