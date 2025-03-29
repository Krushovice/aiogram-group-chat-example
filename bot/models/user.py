"""
User:
 - pk: Primary key
 - tg_id: Bigint, unique, index, not null
 - username: String, unique, index, nullable
 - first_name: String
 - last_name: String, nullable
 - favourite genre: String, unique, nullable
 - books many-to-many

"""

from sqlalchemy import Integer, BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    pk: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
    )

    tg_id: Mapped[int] = mapped_column(
        BigInteger(),
        unique=True,
        nullable=False,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
    )

    favourite_genre: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
    )
