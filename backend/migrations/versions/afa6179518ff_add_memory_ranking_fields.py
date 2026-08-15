"""add memory ranking fields

Revision ID: afa6179518ff
Revises: 21363bbfb706
Create Date: 2026-08-13 02:35:20.172554

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afa6179518ff'

down_revision: Union[str, Sequence[str], None] = '21363bbfb706'

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""

    # Add memory ranking fields.
    # server_default is required because existing
    # records already exist in agent_memories table.

    op.add_column(
        'agent_memories',
        sa.Column(
            'success_score',
            sa.Float(),
            nullable=False,
            server_default='0.0'
        )
    )


    op.add_column(
        'agent_memories',
        sa.Column(
            'usage_count',
            sa.Integer(),
            nullable=False,
            server_default='0'
        )
    )


    op.add_column(
        'agent_memories',
        sa.Column(
            'last_used',
            sa.DateTime(timezone=True),
            nullable=True
        )
    )



def downgrade() -> None:
    """Downgrade schema."""


    op.drop_column(
        'agent_memories',
        'last_used'
    )


    op.drop_column(
        'agent_memories',
        'usage_count'
    )


    op.drop_column(
        'agent_memories',
        'success_score'
    )