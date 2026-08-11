"""add permissions system

Revision ID: 29f0489ff4a3
Revises: 813084baab19
Create Date: 2026-07-30 00:43:31.176874

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "29f0489ff4a3"

down_revision: Union[str, Sequence[str], None] = "813084baab19"

branch_labels = None

depends_on = None



def upgrade() -> None:
    """Upgrade schema."""


    op.create_table(
        "permissions",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        )
    )


    op.create_index(
        "ix_permissions_id",
        "permissions",
        ["id"]
    )


    op.create_table(
        "role_permissions",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            "role",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "permission_id",
            sa.Integer(),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permissions.id"],
            ondelete="CASCADE"
        )
    )


    op.create_index(
        "ix_role_permissions_id",
        "role_permissions",
        ["id"]
    )



def downgrade() -> None:
    """Downgrade schema."""


    op.drop_index(
        "ix_role_permissions_id",
        table_name="role_permissions"
    )

    op.drop_table(
        "role_permissions"
    )


    op.drop_index(
        "ix_permissions_id",
        table_name="permissions"
    )

    op.drop_table(
        "permissions"
    )