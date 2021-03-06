import aiopg.sa
from sqlalchemy import MetaData, Table, Column, Integer, String, PrimaryKeyConstraint


meta = MetaData()

email = Table(
    'email', meta,
    Column('id', Integer, nullable=False),
    Column('email', String(100), nullable=False),

    PrimaryKeyConstraint('id', name='email_id_pkey')
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
