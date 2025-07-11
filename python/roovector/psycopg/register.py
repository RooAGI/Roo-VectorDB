from psycopg.types import TypeInfo
from .roohalfvec import register_roohalfvec_info
from .roovector import register_roovector_info


def register_roovector(context):
    info = TypeInfo.fetch(context, 'roovector')
    register_roovector_info(context, info)

    info = TypeInfo.fetch(context, 'roohalfvec')
    if info is not None:
        register_roohalfvec_info(context, info)

async def register_roovector_async(context):
    info = await TypeInfo.fetch(context, 'roovector')
    register_roovector_info(context, info)

    info = await TypeInfo.fetch(context, 'roohalfvec')
    if info is not None:
        register_roohalfvec_info(context, info)
