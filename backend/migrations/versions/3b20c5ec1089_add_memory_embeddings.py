"""add memory embeddings

Revision ID: 3b20c5ec1089
Revises: afa6179518ff
Create Date: 2026-08-13 03:14:05.617864

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = '3b20c5ec1089'

down_revision: Union[str, Sequence[str], None] = 'afa6179518ff'

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'agent_memories',
        sa.Column(
            'embedding',
            Vector(1536),
            nullable=True
        )
    )



def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        'agent_memories',
        'embedding'
    )