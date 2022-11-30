from db.base import Base
from db.connection import engine
from core.settings import settings
from api.routes import app
import uvicorn


if __name__ == "__main__":
    Base.metadata.create_all(engine, checkfirst=True)
    uvicorn.run(app, port=settings.PORT)
