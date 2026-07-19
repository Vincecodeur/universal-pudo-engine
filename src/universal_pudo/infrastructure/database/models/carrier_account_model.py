from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo.infrastructure.database.base import Base


class CarrierAccountModel(Base):
    __tablename__ = "carrier_accounts"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    carrier_id: Mapped[str] = mapped_column(
        ForeignKey("carriers.id"),
        nullable=False,
    )

    account_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )