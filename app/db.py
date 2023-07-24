import databases
import ormar
import sqlalchemy
from datetime import datetime

from app.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"
    
    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=100)
    firstname: str = ormar.String(max_length=100)
    lastname: str = ormar.String(max_length=100)
    is_admin: bool = ormar.Boolean(default=False)
    created_at: datetime = ormar.DateTime(default=datetime.utcnow)
    last_updated: datetime = ormar.DateTime(default=datetime.utcnow)

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
