from src.configs.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

class Praise(Base):
    __tablename__ = "praise"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cult_id:Mapped[int] = mapped_column(ForeignKey("cult.id"))
    music_id: Mapped[int] = mapped_column(ForeignKey("music.id"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id"))
    group: Mapped[str] = mapped_column(nullable=False)

    def __str__(self):
        return self.group