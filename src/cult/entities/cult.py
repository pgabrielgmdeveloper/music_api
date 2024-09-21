from typing import List
from src.configs.database import Base
from sqlalchemy.orm import mapped_column,Mapped, relationship
from datetime import date

from src.prase.entities.praise import Praise
class Cult(Base):

    __tablename__ = "cult"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(default=date.today)
    end_date: Mapped[date] = mapped_column(nullable=False)
    praises: Mapped[List[Praise]] = relationship()