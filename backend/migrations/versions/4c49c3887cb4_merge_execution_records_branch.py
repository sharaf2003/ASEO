"""merge execution records branch

Revision ID: 4c49c3887cb4
Revises: 7777ee04cf7e, 1ef742675a8b
Create Date: 2026-08-22 02:47:40.577304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c49c3887cb4'
down_revision: Union[str, Sequence[str], None] = ('7777ee04cf7e', '1ef742675a8b')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
