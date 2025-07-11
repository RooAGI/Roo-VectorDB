from .. import RooVector, RooHalfVector


async def register_roovector(conn, schema='public'):
    await conn.set_type_codec(
        'roovector',
        schema=schema,
        encoder=RooVector._to_db_binary,
        decoder=RooVector._from_db_binary,
        format='binary'
    )

    try:
        await conn.set_type_codec(
            'roohalfvec',
            schema=schema,
            encoder=RooHalfVector._to_db_binary,
            decoder=RooHalfVector._from_db_binary,
            format='binary'
        )

    except ValueError as e:
        if not str(e).startswith('unknown type:'):
            raise e
