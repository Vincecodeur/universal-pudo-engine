"""add pickup point last_synced_at

Revision ID: 7b2c8f4a9d31
Revises: 2a99db1622c7
Create Date: 2026-07-20

"""

from typing import Sequence
from typing import Union

from alembic import op
import sqlalchemy as sa


revision: str = "7b2c8f4a9d31"
down_revision: Union[str, Sequence[str], None] = "2a99db1622c7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "pickup_points",
        sa.Column(
            "last_synced_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "pickup_points",
        "last_synced_at",
    )