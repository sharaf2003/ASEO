"""add project member status

Revision ID: c797676797ea
Revises: 9c0d5162e50c
Create Date: 2026-07-31 18:35:47.932893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'c797676797ea'
down_revision: Union[str, Sequence[str], None] = '9c0d5162e50c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        'project_members',
        sa.Column(
            'status',
            sa.String(length=50),
            nullable=False,
            server_default='ACTIVE'
        )
    )


    op.alter_column(
        'project_members',
        'status',
        server_default=None
    )


def downgrade() -> None:

    op.drop_column(
        'project_members',
        'status'
    )