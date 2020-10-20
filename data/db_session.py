import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from data.modelbase import Base

__factory = None


def run():
    global __factory

    if __factory:
        return

    conn_str = 'sqlite:///test_db.db'
    print("Connecting to DB with {}".format(conn_str))

    engine = sa.create_engine(conn_str, echo=True)

    __factory = orm.sessionmaker(bind=engine, autoflush=False)

    # noinspection PyUnresolvedReferences
    import __all_models

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
