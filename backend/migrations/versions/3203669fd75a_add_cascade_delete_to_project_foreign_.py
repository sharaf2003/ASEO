"""add cascade delete to project foreign keys

Revision ID: 3203669fd75a
Revises: 2774ba35f0b7
Create Date: 2026-07-31 00:27:34.335328

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers
revision: str = "3203669fd75a"

down_revision: Union[str, Sequence[str], None] = "2774ba35f0b7"

branch_labels = None

depends_on = None



def upgrade() -> None:
    """
    Add cascade foreign keys to projects.
    """

    op.create_foreign_key(
        "fk_projects_organization",
        "projects",
        "organizations",
        ["organization_id"],
        ["id"],
        ondelete="CASCADE"
    )


    op.create_foreign_key(
        "fk_projects_owner",
        "projects",
        "users",
        ["owner_id"],
        ["id"],
        ondelete="CASCADE"
    )


    op.create_foreign_key(
        "fk_projects_workspace",
        "projects",
        "workspaces",
        ["workspace_id"],
        ["id"],
        ondelete="CASCADE"
    )




def downgrade() -> None:
    """
    Remove cascade foreign keys.
    """


    op.drop_constraint(
        "fk_projects_workspace",
        "projects",
        type_="foreignkey"
    )


    op.drop_constraint(
        "fk_projects_owner",
        "projects",
        type_="foreignkey"
    )


    op.drop_constraint(
        "fk_projects_organization",
        "projects",
        type_="foreignkey"
    )