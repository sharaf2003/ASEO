"""create core tables

Revision ID: 5534dae6a939
Revises: 29f0489ff4a3
Create Date: 2026-07-30 12:48:31.926909

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5534dae6a939"

down_revision: Union[str, Sequence[str], None] = "29f0489ff4a3"

branch_labels = None

depends_on = None



def upgrade() -> None:
    """Upgrade schema."""


    op.create_table(
        "organizations",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "name",
            sa.String(length=200),
            nullable=False
        ),

        sa.Column(
            "plan",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False
        ),

        sa.PrimaryKeyConstraint("id"),

        sa.UniqueConstraint("name")
    )


    op.create_index(
        "ix_organizations_id",
        "organizations",
        ["id"],
        unique=False
    )



    op.create_table(
        "workspaces",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "organization_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "name",
            sa.String(length=200),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.id"]
        ),

        sa.PrimaryKeyConstraint("id")
    )


    op.create_index(
        "ix_workspaces_id",
        "workspaces",
        ["id"],
        unique=False
    )



    op.create_table(
        "users",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "organization_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "workspace_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "password_hash",
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            "role",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False
        ),

        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.id"]
        ),

        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspaces.id"]
        ),

        sa.PrimaryKeyConstraint("id")
    )


    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True
    )

    op.create_index(
        "ix_users_id",
        "users",
        ["id"],
        unique=False
    )

    op.create_index(
        "ix_users_organization_id",
        "users",
        ["organization_id"],
        unique=False
    )

    op.create_index(
        "ix_users_workspace_id",
        "users",
        ["workspace_id"],
        unique=False
    )



    op.create_table(
        "project_members",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "project_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "role",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE"
        ),

        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE"
        ),

        sa.PrimaryKeyConstraint("id")
    )


    op.create_index(
        "ix_project_members_id",
        "project_members",
        ["id"],
        unique=False
    )




def downgrade() -> None:
    """Downgrade schema."""


    op.drop_index(
        "ix_project_members_id",
        table_name="project_members"
    )

    op.drop_table(
        "project_members"
    )


    op.drop_index(
        "ix_users_workspace_id",
        table_name="users"
    )

    op.drop_index(
        "ix_users_organization_id",
        table_name="users"
    )

    op.drop_index(
        "ix_users_id",
        table_name="users"
    )

    op.drop_index(
        "ix_users_email",
        table_name="users"
    )

    op.drop_table(
        "users"
    )


    op.drop_index(
        "ix_workspaces_id",
        table_name="workspaces"
    )

    op.drop_table(
        "workspaces"
    )


    op.drop_index(
        "ix_organizations_id",
        table_name="organizations"
    )

    op.drop_table(
        "organizations"
    )