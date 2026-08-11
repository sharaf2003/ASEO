"""add member update permission

Revision ID: 9c0d5162e50c
Revises: 3203669fd75a
Create Date: 2026-07-31 00:34:53.973556

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9c0d5162e50c"
down_revision: Union[str, Sequence[str], None] = "3203669fd75a"

branch_labels = None
depends_on = None



def upgrade() -> None:
    """Upgrade schema."""


    permissions = sa.table(

        "permissions",

        sa.column("id", sa.Integer),

        sa.column("name", sa.String),

        sa.column("description", sa.Text)

    )


    role_permissions = sa.table(

        "role_permissions",

        sa.column("role", sa.String),

        sa.column("permission_id", sa.Integer)

    )


    op.bulk_insert(

        permissions,

        [

            {

                "name": "member.update",

                "description": "Update project member role"

            }

        ]

    )


    permission_id = op.get_bind().execute(

        sa.text(
            """
            SELECT id
            FROM permissions
            WHERE name='member.update'
            """
        )

    ).scalar()



    op.bulk_insert(

        role_permissions,

        [

            {

                "role": "OWNER",

                "permission_id": permission_id

            }

        ]

    )





def downgrade() -> None:
    """Downgrade schema."""


    op.execute(

        """
        DELETE FROM role_permissions
        WHERE permission_id IN
        (
            SELECT id
            FROM permissions
            WHERE name='member.update'
        )
        """

    )


    op.execute(

        """
        DELETE FROM permissions
        WHERE name='member.update'
        """

    )