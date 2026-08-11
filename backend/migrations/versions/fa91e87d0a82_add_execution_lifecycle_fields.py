"""add execution lifecycle fields

Revision ID: fa91e87d0a82
Revises: b89216d36ea5
Create Date: 2026-07-31 20:03:43.145255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fa91e87d0a82'
down_revision: Union[str, Sequence[str], None] = 'b89216d36ea5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        'execution_records',
        sa.Column(
            'started_at',
            sa.DateTime(timezone=True),
            nullable=True
        )
    )


    op.add_column(
        'execution_records',
        sa.Column(
            'finished_at',
            sa.DateTime(timezone=True),
            nullable=True
        )
    )

def downgrade() -> None:

    op.drop_column(
        'execution_records',
        'finished_at'
    )


    op.drop_column(
        'execution_records',
        'started_at'
    )