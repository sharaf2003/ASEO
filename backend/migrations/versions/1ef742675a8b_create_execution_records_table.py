"""create execution records table

Revision ID: xxxx
Revises: b89216d36ea5
Create Date: 2026-08-22

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "1ef742675a8b"

down_revision: Union[str, Sequence[str], None] = "b89216d36ea5"

branch_labels = None

depends_on = None



def upgrade() -> None:


    op.create_table(

        "execution_records",


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
            "request",
            sa.String(length=200),
            nullable=False
        ),


        sa.Column(
            "team",
            sa.JSON(),
            nullable=True
        ),


        sa.Column(
            "software",
            sa.JSON(),
            nullable=True
        ),


        sa.Column(
            "deployment",
            sa.JSON(),
            nullable=True
        ),


        sa.Column(
            "operations",
            sa.JSON(),
            nullable=True
        ),


        sa.Column(
            "status",
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

            ["projects.id"]

        ),


        sa.PrimaryKeyConstraint(
            "id"
        )

    )


    op.create_index(

        "ix_execution_records_id",

        "execution_records",

        ["id"],

        unique=False

    )


    op.create_index(

        "ix_execution_records_project_id",

        "execution_records",

        ["project_id"],

        unique=False

    )





def downgrade() -> None:


    op.drop_index(

        "ix_execution_records_project_id",

        table_name="execution_records"

    )


    op.drop_index(

        "ix_execution_records_id",

        table_name="execution_records"

    )


    op.drop_table(
        "execution_records"
    )