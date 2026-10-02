from modulo_common.core.base_entity import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from uuid import uuid4
from datetime import datetime

class UserEntity(Base):
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: f"usr_{uuid4()}")
    email: Mapped[str] = mapped_column(String)
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    provider: Mapped[str] = mapped_column(String)
    provider_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))