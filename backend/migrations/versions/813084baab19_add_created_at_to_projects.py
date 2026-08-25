"""add created_at and updated_at to projects

Revision ID: 813084baab19
Revises: f374afed9418
Create Date: 2026-07-26 21:22:36.783647

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "813084baab19"

down_revision: Union[str, Sequence[str], None] = "f374afed9418"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """
    Add timestamps columns to projects table.
    """


    op.add_column(
        "projects",

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True
        )
    )



    op.add_column(
        "projects",

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True
        )
    )





def downgrade() -> None:
    """
    Remove timestamps columns from projects table.
    """


    op.drop_column(
        "projects",
        "updated_at"
    )


    op.drop_column(
        "projects",
        "created_at"
    )