from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo.infrastructure.database.base import Base


class PickupPointModel(Base):
    __tablename__ = "pickup_points"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    carrier_id: Mapped[str] = mapped_column(
        ForeignKey("carriers.id"),
        nullable=False,
    )

    carrier_pickup_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    pickup_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    street_line_1: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    street_line_2: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    postal_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    state_or_region: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    country_code: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    opening_hours: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )