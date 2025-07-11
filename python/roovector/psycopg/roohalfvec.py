from psycopg.adapt import Loader, Dumper
from psycopg.pq import Format
from .. import RooHalfVector


class RooHalfVectorDumper(Dumper):

    format = Format.TEXT

    def dump(self, obj):
        return RooHalfVector._to_db(obj).encode('utf8')


class RooHalfVectorBinaryDumper(RooHalfVectorDumper):

    format = Format.BINARY

    def dump(self, obj):
        return RooHalfVector._to_db_binary(obj)


class RooHalfVectorLoader(Loader):

    format = Format.TEXT

    def load(self, data):
        if isinstance(data, memoryview):
            data = bytes(data)
        return RooHalfVector._from_db(data.decode('utf8'))


class RooHalfVectorBinaryLoader(RooHalfVectorLoader):

    format = Format.BINARY

    def load(self, data):
        if isinstance(data, memoryview):
            data = bytes(data)
        return RooHalfVector._from_db_binary(data)


def register_roohalfvec_info(context, info):
    info.register(context)

    # add oid to anonymous class for set_types
    text_dumper = type('', (RooHalfVectorDumper,), {'oid': info.oid})
    binary_dumper = type('', (RooHalfVectorBinaryDumper,), {'oid': info.oid})

    adapters = context.adapters
    adapters.register_dumper(RooHalfVector, text_dumper)
    adapters.register_dumper(RooHalfVector, binary_dumper)
    adapters.register_loader(info.oid, RooHalfVectorLoader)
    adapters.register_loader(info.oid, RooHalfVectorBinaryLoader)
