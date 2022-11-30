from sqlalchemy import create_engine
from core.settings import settings

engine = create_engine(settings.DB_CONN, echo=True)
