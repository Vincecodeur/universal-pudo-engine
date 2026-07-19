from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo.infrastructure.database.base import Base


class CarrierModel(Base):
    __tablename__ = "carriers"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    lifecycle: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    supported_countries: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False,
    )

    capabilities: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False,
    )