"""create projects table

Revision ID: f374afed9418
Revises:
Create Date: 2026-07-26 21:06:50.774807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'f374afed9418'

down_revision: Union[str, Sequence[str], None] = None

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:

    """
    Create projects table.
    """

    op.create_table(
        'projects',

        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            'name',
            sa.String(length=200),
            nullable=False
        ),

        sa.Column(
            'description',
            sa.Text(),
            nullable=True
        ),

        sa.Column(
            'organization_id',
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            'workspace_id',
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            'owner_id',
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            'status',
            sa.String(length=50),
            nullable=True
        ),

        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(

        op.f('ix_projects_id'),

        'projects',

        ['id'],

        unique=False

    )





def downgrade() -> None:

    op.drop_index(

        op.f('ix_projects_id'),

        table_name='projects'

    )


    op.drop_table(

        'projects'

    )