from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, engine


class usuarios(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30),nullable=False)
    email:Mapped[str] = mapped_column(String(255),nullable=False, unique=True)
    senha:Mapped[str] = mapped_column(String(255),nullable=False)


Base.metadata.create_all(bind=engine)


