"""add evolution memory

Revision ID: d28dde30a23e
Revises: 9a126a5c1de6
Create Date: 2026-08-16 02:20:28.818900

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd28dde30a23e'

down_revision: Union[str, Sequence[str], None] = '9a126a5c1de6'

branch_labels = None

depends_on = None



def upgrade() -> None:
    """
    Add evolution memory enhancements.
    """


    op.add_column(
        'decision_memory',
        sa.Column(
            'adaptive_decision_score',
            sa.Float(),
            nullable=False,
            server_default='0'
        )
    )


    op.add_column(
        'decision_memory',
        sa.Column(
            'confidence',
            sa.Float(),
            nullable=False,
            server_default='0'
        )
    )


    op.add_column(
        'knowledge_patterns',
        sa.Column(
            'priority_score',
            sa.Float(),
            nullable=False,
            server_default='0.5'
        )
    )


def downgrade() -> None:

    op.drop_column(
        'knowledge_patterns',
        'priority_score'
    )


    op.drop_column(
        'decision_memory',
        'confidence'
    )


    op.drop_column(
        'decision_memory',
        'adaptive_decision_score'
    )