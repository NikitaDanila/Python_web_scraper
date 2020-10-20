import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import Base


class Email(Base):
    __tablename__ = 'email_table'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
