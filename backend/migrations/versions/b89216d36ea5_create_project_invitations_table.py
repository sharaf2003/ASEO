"""create project invitations table

Revision ID: b89216d36ea5
Revises: c797676797ea
Create Date: 2026-07-31 19:05:15.514448

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b89216d36ea5"
down_revision: Union[str, Sequence[str], None] = "c797676797ea"
branch_labels = None
depends_on = None



def upgrade() -> None:

    op.create_table(

        "project_invitations",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            index=True
        ),


        sa.Column(
            "project_id",
            sa.Integer(),
            nullable=False
        ),


        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False
        ),


        sa.Column(
            "role",
            sa.String(length=50),
            nullable=False,
            server_default="MEMBER"
        ),


        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
            server_default="PENDING"
        ),


        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),


        sa.Column(
            "expires_at",
            sa.DateTime(timezone=True),
            nullable=True
        ),


        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE"
        )

    )


    op.create_index(
        "ix_project_invitations_project_id",
        "project_invitations",
        ["project_id"]
    )


    op.create_index(
        "ix_project_invitations_email",
        "project_invitations",
        ["email"]
    )



def downgrade() -> None:

    op.drop_index(
        "ix_project_invitations_email",
        table_name="project_invitations"
    )


    op.drop_index(
        "ix_project_invitations_project_id",
        table_name="project_invitations"
    )


    op.drop_table(
        "project_invitations"
    )