import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import Base


class Phone(Base):
    __tablename__ = 'phone_number_table'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    phone_number = sa.Column(sa.String)
